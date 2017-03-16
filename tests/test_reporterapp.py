import unittest
from os.path import abspath, dirname, join, realpath

from reporterapp import ReporterApp


class TestReporterApp(unittest.TestCase):

    def setUp(self):
        self.fixture_dir = abspath(join(dirname(realpath(__file__)),
                                        'fixtures'))
        self.fixture = join(self.fixture_dir,
                            '2017-01-01-reporter-export.json')

    def test_load_local_export(self):
        reporter = ReporterApp(self.fixture_dir)
        self.assertTrue(reporter.load_local_export(self.fixture))

    def test_load_local_exports_one(self):
        reporter = ReporterApp(self.fixture)
        self.assertTrue(reporter)

    def test_load_local_exports_multiple(self):
        reporter = ReporterApp(self.fixture_dir)
        self.assertTrue(reporter)
