import re
from nltk import download
from nltk.corpus import stopwords


class InputPreparator:

    def __init__(self):
        download('stopwords')
        InputPreparator.stop_words = stopwords.words('english')

    @staticmethod
    def normalize_wikipedia_data(text):
        lines = text.split('\n')
        count = 0
        current_text = []
        data = []
        topic_pattern = '((=)+)'
        escape_topic_pattern = '====='
        for line in lines:
            count += 1
            txt = line
            x = re.sub(topic_pattern, escape_topic_pattern, txt)
            if x.count(escape_topic_pattern) == 2:
                if x.count('References') > 0:
                    break
                if len(current_text) > 0:
                    data.append(current_text)
                data.append(txt)
                current_text = []
            else:
                if len(line.strip()) > 0:
                    current_text += [line.strip().replace('\n', ' ')]
        if len(current_text) > 0:
            data.append(current_text)
        return data

    @staticmethod
    def preprocess_senetence_to_arr(sentence):
        return [w for w in sentence.lower().split() if w not in InputPreparator.stop_words]
