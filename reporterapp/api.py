import json
from glob import glob
from os.path import expanduser, isfile, join

from .models import Question, Snapshot


class Reporter(object):

    def __init__(self, path=expanduser('~/Dropbox/Apps/Reporter-App')):
        self.path = path

        self.snapshots = []
        self.questions = []

        self._load_exports()

    # Private Methods
    def _load_exports(self):
        """
        Private function for loading multiple export files.
        """
        snapshots = []
        questions = []

        if isfile(self.path):
            data = self._load_export(self.path)

            snapshots = data['snapshots']
            questions = data['questions']
        else:
            export_files = glob(join(self.path, '*-reporter-export.json'))

            for export_file in export_files:
                data = self._load_export(export_file)

                snapshots += data['snapshots']
                questions += data['questions']

        self.questions = Question.parse_list(questions)
        self.snapshots = Snapshot.parse_list(snapshots, self.questions)

    def _load_export(self, export_file):
        """
        Private function for loading an export file.
        """
        with open(export_file) as fobj:
            data = json.loads(fobj.read())

        return data
