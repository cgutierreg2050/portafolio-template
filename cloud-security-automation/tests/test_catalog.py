"""Behavior, failure-mode and publication-contract tests for synthetic labs."""
import copy
import json
import pathlib
import re
import subprocess
import sys
import unittest
from unittest.mock import patch
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from demo import run
from lab.registry import HANDLERS


def fixture(name):
    return json.loads((ROOT/'projects'/name/'input.json').read_text())


def evaluate(name, edit=None):
    data = fixture(name)
    if edit: edit(data)
    return HANDLERS[name](data)


class BehaviorTests(unittest.TestCase):
    def test_dmarc_requires_aligned_authentication(self):
        rows=evaluate('dmarc')['messages']
        self.assertEqual([r['strict_dmarc'] for r in rows],['pass','pass','fail'])
        self.assertEqual(rows[2]['review'],'forwarding-review')
        self.assertFalse(any(r['allowlist_change'] for r in rows))

    def test_dmarc_strict_alignment_rejects_subdomain(self):
        r=evaluate('dmarc',lambda d:d['messages'][0].update(mail_from='sub.sender.example.test'))
        self.assertEqual(r['messages'][0]['strict_dmarc'],'fail')

    def test_key_vault_returns_metadata_and_rejects_collisions(self):
        r=evaluate('key-vault')
        self.assertEqual(len(r['plan']),3)
        self.assertEqual(r['azure_writes'],0)
        with self.assertRaises(ValueError):
            evaluate('key-vault',lambda d:d['entries'].append({'id':'X','title':'Demo-Reporting'}))

    def test_key_vault_refuses_secret_fields(self):
        with self.assertRaises(ValueError):
            evaluate('key-vault',lambda d:d['entries'][0].update(password='FICTIONAL-DO-NOT-USE'))

    def test_transcription_batches_respect_budget(self):
        r=evaluate('transcription')
        self.assertTrue(all(b['estimated_mb']<=r['capacity_mb'] for b in r['batches']))
        self.assertEqual(r['rejected'],['DEMO-A4'])
        self.assertEqual(sorted(j for b in r['batches'] for j in b['jobs']),['DEMO-A1','DEMO-A2','DEMO-A3'])

    def test_relocation_parallel_tasks_do_not_sum(self):
        r=evaluate('relocation')
        self.assertEqual(r['critical_path_days'],8)
        self.assertEqual(r['schedule']['validation']['start_day'],7)

    def test_relocation_cycle_and_missing_dependency_rejected(self):
        for dependency in ['validation','unknown']:
            with self.subTest(dependency=dependency), self.assertRaises(ValueError):
                evaluate('relocation',lambda d:d['tasks'][0].update(depends_on=[dependency]))

    def test_terraform_destructive_changes_and_exposure_flagged(self):
        r=evaluate('terraform')
        self.assertFalse(r['review_passed'])
        self.assertEqual({f['reason'] for f in r['findings']},{'destructive-change-needs-review','public-management-exposure','missing-tags'})
        self.assertFalse(r['terraform_executed'])

    def test_graph_deduplicates_and_escapes_html(self):
        r=evaluate('graph-mail')
        self.assertEqual(len(r['batches'][0]),2)
        self.assertEqual(r['invalid_recipients'],['DEMO-R4'])
        self.assertIn('&lt;Demo&gt;',r['batches'][0][0]['html'])
        self.assertEqual(r['sent'],0)

    def test_graph_tracking_keys_stable_across_order(self):
        a=evaluate('graph-mail');b=evaluate('graph-mail',lambda d:d['recipients'].reverse())
        self.assertEqual({r['id'] for batch in a['batches'] for r in batch},
                         {r['id'] for batch in b['batches'] for r in batch})

    def test_container_jobs_assigned_exactly_once(self):
        r=evaluate('docker-selenium');ids=[j for batch in r['assignments'].values() for j in batch]
        self.assertEqual(len(ids),len(set(ids)))
        self.assertEqual(set(ids),{j['id'] for j in fixture('docker-selenium')['jobs']})
        self.assertEqual(r['containers_started'],0)

    def test_archive_holds_override_old_activity(self):
        r=evaluate('data-lifecycle')
        self.assertEqual([d['id'] for d in r['candidates']],['DEMO-D1'])
        self.assertIn({'id':'DEMO-D2','reason':'legal-hold'},r['excluded'])
        self.assertEqual(r['files_moved'],0)

    def test_archive_cutoff_and_active_retention_excluded(self):
        r=evaluate('data-lifecycle',lambda d:d['documents'][0].update(last_activity=d['cutoff']))
        self.assertEqual(r['candidates'],[])
        r=evaluate('data-lifecycle',lambda d:d['documents'][0].update(retain_until='2030-01-01T00:00:00Z'))
        self.assertEqual(r['candidates'],[])

    def test_app_control_deny_precedence_and_audit(self):
        r=evaluate('applocker-wdac')['decisions']
        self.assertEqual([a['decision'] for a in r],['allow','deny','deny'])
        self.assertTrue(all(a['effective_action']=='log-only' for a in r))
        r=evaluate('applocker-wdac',lambda d:d.update(mode='enforce'))
        self.assertEqual(r['decisions'][2]['effective_action'],'deny')

    def test_vpn_overlap_missing_route_and_good_topology(self):
        self.assertTrue(evaluate('azure-vpn')['topology_checks_pass'])
        r=evaluate('azure-vpn',lambda d:d.update(azure=d['on_prem'],routes_to_on_prem=[]))
        self.assertIn('address-space-overlap',r['issues'])
        self.assertIn('on-prem-route-missing',r['issues'])
        self.assertFalse(r['tunnel_tested'])

    def test_n8n_access_and_persistence_required(self):
        r=evaluate('n8n-kubernetes',lambda d:d.update(cloudflare_access=False,persistent_storage=False))
        self.assertEqual(set(r['issues']),{'access-policy-missing','persistent-storage-missing'})
        self.assertFalse(r['high_availability_validated'])

    def test_sharepoint_preserves_owners_and_pilot_scope(self):
        r=evaluate('sharepoint')
        self.assertEqual(r['changes'][0]['after'],['demo-owner','demo-reviewer'])
        self.assertEqual(len(r['changes']),1)
        self.assertEqual({x['reason'] for x in r['deferred']},{'target-not-active','outside-pilot'})
        self.assertEqual(r['writes'],0)

    def test_sharepoint_backup_required(self):
        r=evaluate('sharepoint',lambda d:d['sites'][0].update(backup_verified=False))
        self.assertEqual(r['changes'],[])
        self.assertIn('backup-unverified',{x['reason'] for x in r['deferred']})

    def test_purview_hold_and_label_preserved_without_echoing_text(self):
        r=evaluate('purview-dlp')['documents']
        self.assertEqual(r[0]['retention'],'preserve-legal-hold')
        self.assertEqual(r[0]['external_share'],'block-proposal')
        self.assertEqual(r[1]['external_share'],'no-change')
        self.assertEqual(r[2]['label'],'Confidential')
        self.assertNotIn('text',r[0])

    def test_hardening_approved_forwarding_retained(self):
        r=evaluate('m365-hardening')
        self.assertEqual(len(r['findings']),3)
        self.assertNotIn('DEMO-F2',{f['entity'] for f in r['findings']})
        self.assertFalse(r['automatic_deletion'])

    def test_arc_stale_and_absent_differ(self):
        r=evaluate('azure-arc')
        self.assertEqual([x['state'] for x in r['devices']],['recently-observed','stale','not-observed-in-arc'])
        self.assertFalse(r['enrollment_performed'])

    def test_ai_weight_estimate_is_not_runtime_validation(self):
        r=evaluate('ai-lab')
        self.assertAlmostEqual(r['weights_gib'],3.260,places=3)
        self.assertFalse(r['inference_validated'])
        self.assertIn('kv-cache',r['excluded'])
        self.assertFalse(evaluate('ai-lab',lambda d:d.update(parameters_billions=100))['weights_fit'])

    def test_pgp_context_and_key_material_both_required(self):
        r=evaluate('openpgp')
        self.assertEqual(set(r['reasons']),{'execution-context-mismatch','private-key-unavailable-in-context'})
        self.assertFalse(r['metadata_ready'])

    def test_pgp_expiry_revocation_and_missing_subkey(self):
        def edit(d):
            d['keys'][0].update(context='SYSTEM',private_material_available=True,expires=d['as_of'],revoked=True)
        r=evaluate('openpgp',edit)
        self.assertEqual(set(r['reasons']),{'key-expired','key-revoked'})
        self.assertFalse(r['decryption_performed'])
        self.assertEqual(evaluate('openpgp',lambda d:d.update(keys=[]))['reasons'],['recipient-subkey-unavailable'])

    def test_retrieval_acl_precedes_citations(self):
        r=evaluate('lexrag')
        self.assertEqual([m['id'] for m in r['matches']],['DEMO-DOC1'])
        self.assertEqual(r['matches'][0]['citation'],'fixture://document-1#p1')
        self.assertFalse(r['answer_generated'])

    def test_retrieval_no_sources_does_not_invent_answer(self):
        r=evaluate('lexrag',lambda d:d.update(query='unknown fictional term'))
        self.assertEqual(r['status'],'no-evidence')
        self.assertEqual(r['matches'],[])

    def test_glpi_inventory_mismatch_differs_from_protection_gap(self):
        r=evaluate('glpi-defender')['endpoints']
        self.assertTrue(r[0]['protection_evidence']);self.assertTrue(r[0]['inventory_mismatch'])
        self.assertFalse(r[1]['protection_evidence']);self.assertTrue(r[1]['stale_signatures'])

    def test_glpi_table_loss_reported(self):
        r=evaluate('glpi-defender',lambda d:d.update(schema_after=['demo_assets']))
        self.assertEqual(r['missing_tables'],['demo_users'])
        self.assertFalse(r['schema_preserved'])

    def test_ad_health_and_fsmo_checks_keep_migration_in_planning(self):
        r=evaluate('active-directory')
        self.assertIn('DEMO-DC2:replication',r['issues'])
        self.assertFalse(r['prechecks_clear'])
        self.assertEqual(r['migration_state'],'planning')
        r=evaluate('active-directory',lambda d:d['fsmo'].update(pdc='UNKNOWN-DEMO'))
        self.assertIn('pdc:unknown-owner',r['issues'])
        self.assertFalse(r['roles_transferred'])

    def test_monitoring_alerts_only_affected_hosts(self):
        r=evaluate('monitoring')['alerts']
        self.assertEqual({a['host'] for a in r},{'DEMO-H1','DEMO-H2'})
        self.assertEqual(r[1]['priority'],'critical')

    def test_patch_closure_requires_installed_kb_and_clear_scan(self):
        r=evaluate('patch-pilot')['findings']
        self.assertEqual([x['status'] for x in r],['candidate-for-reviewed-job','defer-pending-reboot','verified-closed'])
        r=evaluate('patch-pilot',lambda d:d['findings'][2].update(post_scan_clear=False))
        self.assertEqual(r['findings'][2]['status'],'await-post-validation')
        self.assertEqual(r['jobs_submitted'],0)

    def test_patch_pilot_scope_and_unknown_mapping(self):
        r=evaluate('patch-pilot',lambda d:d['devices'][0].update(in_pilot=False))
        self.assertEqual(r['findings'][0]['status'],'out-of-scope')
        r=evaluate('patch-pilot',lambda d:d.update(cve_to_kb={}))
        self.assertTrue(all(x['status']=='manual-mapping-required' for x in r['findings']))

    def test_patch_duplicate_findings_do_not_duplicate_candidates(self):
        r=evaluate('patch-pilot',lambda d:d['findings'].append(copy.deepcopy(d['findings'][0])))
        self.assertEqual(len(r['findings']),3)

    def test_patch_conflicting_closure_evidence_requires_review(self):
        def edit(d):
            changed=copy.deepcopy(d['findings'][0]);changed['post_scan_clear']=True
            d['findings'].append(changed)
        with self.assertRaises(ValueError):evaluate('patch-pilot',edit)

    def test_app_control_invalid_mode_rejected(self):
        with self.assertRaises(ValueError):evaluate('applocker-wdac',lambda d:d.update(mode='typo'))

    def test_iis_origin_bypass_and_expiry_reported(self):
        r=evaluate('iis-cloudflare')['portals']
        self.assertTrue(r[0]['fixture_checks_pass'])
        self.assertEqual(set(r[1]['review']),{'origin-tls-missing','access-policy-missing','origin-bypass-exposure','certificate-expired'})

    def test_kvm_disk_proposal_requires_single_candidate(self):
        r=evaluate('kvm-recovery')
        self.assertEqual(r['proposed_path'],'/demo/images/DEMO-VM.qcow2')
        self.assertFalse(r['vm_modified']);self.assertFalse(r['ad_trust_resolved'])
        r=evaluate('kvm-recovery',lambda d:d['available_disks'].append('/demo/backup/DEMO-VM.qcow2'))
        self.assertIsNone(r['proposed_path'])

    def test_kvm_entity_declarations_rejected(self):
        with self.assertRaises(ValueError):evaluate('kvm-recovery',lambda d:d.update(domain_xml='<!DOCTYPE x><domain/>'))

    def test_weekly_window_half_open_and_agent_identity_separate(self):
        r=evaluate('wazuh-reporting')
        self.assertEqual(r['event_count'],2);self.assertEqual(r['duplicates'],1)
        self.assertEqual(r['by_agent'],{'DEMO-AG1':1,'DEMO-AG2':1})
        self.assertEqual(r['high_or_critical'],1)

    def test_weekly_conflicting_duplicate_and_naive_time_rejected(self):
        with self.assertRaises(ValueError):evaluate('wazuh-reporting',lambda d:d['events'][1].update(level=1))
        with self.assertRaises(ValueError):evaluate('wazuh-reporting',lambda d:d.update(start='2026-09-21T00:00:00'))


class CatalogTests(unittest.TestCase):
    def test_exactly_25_distinct_linkedin_cases(self):
        rows=json.loads((ROOT/'projects/catalog.json').read_text())
        self.assertEqual(len(rows),25)
        self.assertEqual(len({r['linkedin_id'] for r in rows}),25)
        self.assertEqual({r['slug'] for r in rows},set(HANDLERS))

    def test_examples_without_network_match_published_outputs(self):
        with patch('socket.socket',side_effect=AssertionError('network forbidden')):
            for name in HANDLERS:
                with self.subTest(project=name):
                    result=run(name)
                    expected=json.loads((ROOT/'projects'/name/'output.example.json').read_text())
                    self.assertEqual(result,expected)
                    self.assertTrue(result['synthetic']);self.assertFalse(result['production_validation'])

    def test_all_25_cli_commands_complete(self):
        for name in HANDLERS:
            with self.subTest(project=name):
                result=subprocess.run([sys.executable,str(ROOT/'demo.py'),name],capture_output=True,text=True,timeout=10)
                self.assertEqual(result.returncode,0,result.stderr)
                self.assertEqual(json.loads(result.stdout)['project'],name)

    def test_inputs_are_not_mutated(self):
        for name,handler in HANDLERS.items():
            data=fixture(name);before=copy.deepcopy(data);handler(data)
            self.assertEqual(data,before,name)

    def test_non_synthetic_inputs_rejected(self):
        from lab.common import synthetic
        with self.assertRaises(ValueError):synthetic({'synthetic':False})
        with self.assertRaises(ValueError):synthetic({})

    def test_fixtures_exclude_original_people_and_company_names(self):
        forbidden=['kristhian_gutierrez','pom cobranzas','zurcher','gutierrez','sociedaddesegurosdevida']
        for name in HANDLERS:
            text=(ROOT/'projects'/name/'input.json').read_text().lower()
            self.assertFalse(any(value in text for value in forbidden),name)
            for email in re.findall(r'[\w.+-]+@[\w.-]+',text):
                self.assertTrue(email.endswith('@example.test'),email)

if __name__=='__main__':unittest.main()
