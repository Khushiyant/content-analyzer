# import pandas as pd
from gingerit.gingerit import GingerIt


class language_analyse:
    def __init__(self, text):
        parser = GingerIt()
        self.processed_json = parser.parse(text)

        # pd.set_option('max_colwidth', 520)
        # processed_json = pd.DataFrame(processed_json)
        # for data in self.processed_json['corrections']:
        #     print("Incorrect: ",data['text'],"\nCorrect: ",data['correct'],"\nDefinition: ",data['definition'],end='\n\n')
        print(self.processed_json)

    def getCorrect(self):
        return self.processed_json['result']

    def getAnalysis(self):
        return self.processed_json['corrections']


if __name__ == "__main__":
    # text = "I hve a bd memary and I want to fx ths situetian. Als, I con't wroote carractli in Englash."
    text = "Hello, I am good"
    language_analyse(text)
