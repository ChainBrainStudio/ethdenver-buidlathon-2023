import json


class GraphPromptBase:
    def __init__(self, q, o):
        self.question = q
        self.output = o

    def to_str(self):
        return json.dumps({'Question': self.question, 'Output': self.output})
