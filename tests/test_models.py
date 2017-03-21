import json
import unittest
from os.path import abspath, dirname, join, realpath

from reporterapp.models import Model, Question, ResultSet, Snapshot


class TestResultSet(unittest.TestCase):

    def setUp(self):
        model_one = Model()
        setattr(model_one, 'uniqueIdentifier', 1)
        setattr(model_one, 'prompt', 'Prompt 1')

        model_two = Model()
        setattr(model_two, 'uniqueIdentifier', 2)
        setattr(model_two, 'prompt', 'Prompt 2')

        self.result_set = ResultSet()
        self.result_set += [model_one, model_two]

    def test_uniqueIdentifiers(self):
        self.assertEquals(self.result_set.uniqueIdentifiers(), [1, 2])


class TestModel(unittest.TestCase):

    def setUp(self):
        self.model = Model()
        setattr(self.model, 'uniqueIdentifier', 1)
        setattr(self.model, 'prompt', 'Prompt 1')

    def test_parse(self):
        with self.assertRaises(NotImplementedError):
            Model.parse({'test': 'test'})

    def test_repr(self):
        self.assertEquals(self.model.__repr__(), 'Model(1)')


class TestSnapshot(unittest.TestCase):

    def setUp(self):
        fixture_dir = abspath(join(dirname(realpath(__file__)),
                                   'fixtures'))
        self.fixture = join(fixture_dir, '2017-01-01-reporter-export.json')

        with open(self.fixture) as fobj:
            self.data = json.loads(fobj.read())

        self.questions = Question.parse_list(self.data['questions'])

    def test_parse(self):
        s = Snapshot.parse(self.data['snapshots'][0], self.questions)
        self.assertIs(type(s), Snapshot)

    def test_parse_list(self):
        s = Snapshot.parse_list(self.data['snapshots'], self.questions)
        self.assertIs(type(s), ResultSet)
