from keybert import KeyBERT
from ModelInterface import ModelInterface

class ModelKeyBert(ModelInterface):

    def __init__(self):
          ModelKeyBert.model = KeyBERT('distilbert-base-nli-mean-tokens')

    @staticmethod
    def keyBert(text):
      keys = ModelKeyBert.model.extract_keywords(text, keyphrase_ngram_range=(1, 5), stop_words='english', top_n=10)
      return [key for key in keys if key[1] > 0.65]

    @staticmethod
    def predict(input: str) -> str:
        return ModelKeyBert.keyBert(input)
