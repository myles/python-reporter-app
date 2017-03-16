from dateutil.parser import parse as date_parse

REPORT_IMPETUS_DISPLAY = {
    0: 'Report button tapped',
    1: 'Report button tapped while Reporter is asleep',
    2: 'Report triggered by notification',
    3: 'Report triggered by setting app to sleep',
    4: 'Report triggered by waking up app'
}

CONNECTION_DISPLAY = {
    0: 'Device is connected via cellular network',
    1: 'Device is connected via WiFi',
    2: 'Device is not connected'
}

QUESTION_TYPE_DISPLAY = {
    0: 'Tokens',
    1: 'Multi-Choice',
    2: 'Yes / No',
    3: 'Location',
    4: 'People',
    5: 'Number',
    6: 'Note'
}


class ResultSet(list):
    """
    A list of like object that holds results.
    """

    def __init__(self):
        super(ResultSet, self).__init__()

    def uniqueIdentifiers(self):
        ids = []

        for item in self:
            if hasattr(item, 'uniqueIdentifier'):
                ids.append(item.uniqueIdentifier)

        return ids

    def get_by_prompt(self, prompt):
        result = None

        for item in self:
            if item.prompt == prompt:
                result = item

        return result


class Model(object):

    @classmethod
    def parse(cls, json):
        """Parse a JSON object into a model instance."""
        raise NotImplementedError

    @classmethod
    def parse_list(cls, json_list, *args):
        """
        Prase a list of JSON objects into a result set of model instances.
        """
        results = ResultSet()

        for obj in json_list:
            if obj:
                results.append(cls.parse(obj, *args))

        return results

    def __repr__(self):
        return '{0}({1})'.format(self.__class__.__name__,
                                 self.uniqueIdentifier)


class Snapshot(Model):
    """A Reporter App Snapshot."""

    @classmethod
    def parse(cls, json, questions):
        """Parse a JSON object into a Snapshot instance."""
        snapshot = cls()
        setattr(snapshot, '_json', json)

        for k, v in json.items():
            if k == 'date':
                setattr(snapshot, k, date_parse(v).replace(tzinfo=None))
            elif k == 'connection':
                setattr(snapshot, 'connectionDisplay', CONNECTION_DISPLAY[v])
            elif k == 'reportImpetus':
                setattr(snapshot, 'reportImpetusDisplay',
                        REPORT_IMPETUS_DISPLAY[v])
            elif k == 'battery':
                setattr(snapshot, 'batteryDisplay', '{:.0f}%'.format(v*100))
            elif k in ['background', 'draft']:
                setattr(snapshot, k, bool(v))
            elif k == 'responses':
                setattr(snapshot, k, Response.parse_list(v, questions))
            else:
                setattr(snapshot, k, v)

        return snapshot

    @classmethod
    def parse_list(cls, json_list, questions):
        """
        Prase a list of JSON objects into a result set of model instances.
        """
        results = ResultSet()

        for obj in json_list:
            if obj:
                results.append(cls.parse(obj, questions))

        return results


class Question(Model):
    """A Reporter App Question."""

    @classmethod
    def parse(cls, json):
        """Prase a JSON object into a Question instance."""
        question = cls()
        setattr(question, '_json', json)

        for k, v in json.items():
            if k == 'questionType':
                setattr(question, 'questionTypeDisplay',
                        QUESTION_TYPE_DISPLAY[v])
            else:
                setattr(question, k, v)

        return question


class Response(Model):
    """A Snapshot Response."""

    @classmethod
    def parse(cls, json, questions):
        """Prase a JSON object into a Response instance."""
        response = cls()
        setattr(response, '_json', json)

        for k, v in json.items():
            if k == 'questionPrompt':
                setattr(response, 'question',
                        questions.get_by_prompt(json['questionPrompt']))
            else:
                setattr(response, k, v)

        return response
