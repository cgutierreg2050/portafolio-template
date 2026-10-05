import importlib.util, pathlib, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('report',ROOT/'examples/wazuh-report/report.py')
report=importlib.util.module_from_spec(spec); spec.loader.exec_module(report)
def event(id='a',time='2026-01-05T00:00:00Z',level=8):
    return {'id':id,'timestamp':time,'agent':{'name':'fixture'},'rule':{'level':level}}
class ReportTests(unittest.TestCase):
    def test_duplicate_events_count_once(self):
        self.assertEqual(report.summarize([event(),event()])[0]['events'],1)
    def test_window_includes_start_excludes_end(self):
        rows=report.summarize([event(),event('b','2026-01-12T00:00:00Z')],report.timestamp('2026-01-05T00:00:00Z'),report.timestamp('2026-01-12T00:00:00Z'))
        self.assertEqual(sum(r['events'] for r in rows),1)
    def test_bad_severity_fails(self):
        with self.assertRaises(ValueError): report.summarize([event(level=16)])
    def test_naive_timestamp_fails(self):
        with self.assertRaises(ValueError): report.timestamp('2026-01-05T00:00:00')
    def test_timezone_normalization(self):
        self.assertEqual(report.timestamp('2026-01-04T18:00:00-06:00'),report.timestamp('2026-01-05T00:00:00Z'))
    def test_spreadsheet_formula_guard(self):
        self.assertEqual(report.csv_safe('=1+1'),"'=1+1")
