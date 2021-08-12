import re
from nltk import download
from nltk.corpus import stopwords


class InputPreparator:

    def __init__(self):
        download('stopwords')
        InputPreparator.stop_words = stopwords.words('english')

    @staticmethod
    def normalize_text_from_wikipedia(text):
        Lines = text.split('\n')
        count = 0
        CurrentText = []
        data = []
        for line in Lines:
            count += 1
            txt = line
            x = re.sub("((=)+)", "=====", txt)
            if x.count("=====") == 2:
                if x.count("References") > 0:
                    break
                level = txt.count('=')
                if len(CurrentText) > 0:
                    data.append(CurrentText)
                data.append(txt)
                CurrentText = []
            else:
                if len(line.strip()) > 0:
                    CurrentText += [line.strip().replace("\n", " ")]
        if len(CurrentText) > 0:
            data.append(CurrentText)
        return data

    @staticmethod
    def preprocess_senetence_to_arr(sentence):
        return [w for w in sentence.lower().split() if w not in InputPreparator.stop_words]
