from keybert import KeyBERT
from models.ModelInterface import ModelInterface


class ModelKeyBert(ModelInterface):

    def __init__(self):
        ModelKeyBert.model = KeyBERT('distilbert-base-nli-mean-tokens')
        ModelKeyBert.MIN_NGRAM = 1
        ModelKeyBert.MAX_NGRAM = 5
        ModelKeyBert.TOP_N = 1
        ModelKeyBert.KEYWORD_THRESHOLD = 0.65

    @staticmethod
    def key_bert(text):
        keys = ModelKeyBert.model.extract_keywords(
            text,
            keyphrase_ngram_range=(
                ModelKeyBert.MIN_NGRAM,
                ModelKeyBert.MAX_NGRAM),
            stop_words='english',
            top_n=ModelKeyBert.TOP_N)
        return [key for key in keys if key[1] > ModelKeyBert.KEYWORD_THRESHOLD]

    @staticmethod
    def predict(input: str) -> str:
        return ModelKeyBert.key_bert(input)
