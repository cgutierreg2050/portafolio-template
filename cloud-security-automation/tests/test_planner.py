import json, pathlib, shutil, subprocess, tempfile, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
@unittest.skipUnless(shutil.which('pwsh'),'PowerShell 7 is required')
class PlannerTests(unittest.TestCase):
    def run_plan(self,entries):
        with tempfile.TemporaryDirectory() as tmp:
            src=pathlib.Path(tmp)/'input.json'; dst=pathlib.Path(tmp)/'out.json'
            src.write_text(json.dumps(entries))
            result=subprocess.run(['pwsh','-NoProfile','-File',str(ROOT/'examples/key-vault-plan/plan.ps1'),'-InputPath',str(src),'-OutputPath',str(dst)],capture_output=True,text=True,timeout=30)
            output=json.loads(dst.read_text(encoding='utf-8-sig')) if dst.exists() else None
            return result,output
    def test_valid_metadata_plan(self):
        result,output=self.run_plan([{'id':'a','title':'Demo Alpha'}])
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(output['entries'][0]['proposedName'],'demo-alpha')
        self.assertFalse(output['entries'][0]['containsSecretValue'])
    def test_normalized_name_collision(self):
        result,output=self.run_plan([{'id':'a','title':'demo alpha'},{'id':'b','title':'demo-alpha'}])
        self.assertNotEqual(result.returncode,0); self.assertIsNone(output)
    def test_duplicate_source_ids(self):
        result,output=self.run_plan([{'id':'a','title':'alpha'},{'id':'a','title':'beta'}])
        self.assertNotEqual(result.returncode,0); self.assertIsNone(output)
