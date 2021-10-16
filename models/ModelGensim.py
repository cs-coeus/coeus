import gensim.downloader as api

from models.ModelInterface import ModelInterface


class ModelGensim(ModelInterface):

    def __init__(self):
        ModelGensim.model = api.load('word2vec-google-news-300')

    @staticmethod
    def get_similarity_two_word_by_w2v(word1, word2):
        try:
            similarity = ModelGensim.model.similarity(word1, word2)
        except KeyError:
            similarity = 0
        return similarity

    @staticmethod
    def get_wmd_distance(word1, word2):
        return ModelGensim.model.wmdistance(word1, word2)

    @staticmethod
    def predict(input: str) -> None:
        return
