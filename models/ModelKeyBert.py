from keybert import KeyBERT
from models.ModelInterface import ModelInterface


class ModelKeyBert(ModelInterface):

    def __init__(self):
        ModelKeyBert.model = KeyBERT('distilbert-base-nli-mean-tokens')
        ModelKeyBert.min_ngram = 1
        ModelKeyBert.max_ngram = 5
        ModelKeyBert.top_n = 1
        ModelKeyBert.keyword_threshold = 0.65

    @staticmethod
    def key_bert(text):
        keys = ModelKeyBert.model.extract_keywords(text, keyphrase_ngram_range=(
            ModelKeyBert.min_ngram, ModelKeyBert.max_ngram), stop_words='english', top_n=ModelKeyBert.top_n)
        return [key for key in keys if key[1] > ModelKeyBert.keyword_threshold]

    @staticmethod
    def predict(input: str) -> str:
        return ModelKeyBert.key_bert(input)
