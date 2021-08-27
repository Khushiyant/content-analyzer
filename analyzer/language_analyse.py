# import pandas as pd
from gingerit.gingerit import GingerIt


class language_analyse:
    def __init__(self, text):
        parser = GingerIt()
        self.processed_json = parser.parse(text)
        print(self.processed_json)

    def getCorrect(self):
        return self.processed_json['result']

    def getAnalysis(self):
        return self.processed_json['corrections']
