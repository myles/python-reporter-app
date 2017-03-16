import json
from glob import glob
from os.path import expanduser, isfile, join

from .models import Question, Snapshot


class ReporterApp(object):

    def __init__(self, path=expanduser('~/Dropbox/Apps/Reporter-App'),
                 dropbox=None):
        self.snapshots = []
        self.questions = []

        if dropbox:
            self.load_dropbox_exports(dropbox)
        else:
            self.load_local_exports(path)

    # Private Methods
    def load_dropbox_exports(self, access_token):
        """
        Private function for loading exports from Dropbox.
        """
        snapshots = []
        questions = []

        from dropbox import Dropbox

        dbx = Dropbox(access_token)

        for entry in dbx.files_list_folder('/Apps/Reporter-App').entries:
            meta, resp = dbx.files_download(entry.path_lower)
            data = json.loads(resp.content)

            snapshots += data['snapshots']
            questions += data['questions']

        self.questions = Question.parse_list(questions)
        self.snapshots = Snapshot.parse_list(snapshots, self.questions)

    def load_local_exports(self, path):
        """
        Private function for loading multiple export files.
        """
        snapshots = []
        questions = []

        if isfile(path):
            data = self.load_local_export(path)

            snapshots = data['snapshots']
            questions = data['questions']
        else:
            export_files = glob(join(path, '*-reporter-export.json'))

            for export_file in export_files:
                data = self.load_local_export(export_file)

                snapshots += data['snapshots']
                questions += data['questions']

        self.questions = Question.parse_list(questions)
        self.snapshots = Snapshot.parse_list(snapshots, self.questions)

    def load_local_export(self, export_file):
        """
        Private function for loading an export file.
        """
        with open(export_file) as fobj:
            data = json.loads(fobj.read())

        return data

    # Public Methods
    def get_by_prompt(self, prompt):
        return self.snapshot.get_by_prompt(prompt)
