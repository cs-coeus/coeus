import gensim.downloader as api
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from ModelInterface import ModelInterface
from typing import Any, Tuple


class ModelClustering(ModelInterface):

    def __init__(self):
        ModelClustering.wmd = api.load('word2vec-google-news-300')

    @staticmethod
    def clustering(X, total_sent, proximity_matrix):
        best_k = -1
        best_cluster = []
        total = int(total_sent / 2)
        best_score = -100
        min_cluster = 2
        for n in range(min_cluster, total):
            algorithm = AgglomerativeClustering(n_clusters=n, affinity='precomputed',
                                                linkage='average')
            clusters = algorithm.fit_predict(proximity_matrix)
            score = silhouette_score(X, algorithm.labels_)
            if score > best_score:
                best_score = score
                best_k = n
                best_cluster = clusters
        return best_k, best_cluster

    @staticmethod
    def predict(input: Tuple[Any, int, Any]) -> Tuple[int, Any]:
        return ModelClustering.clustering(input[0], input[1], input[2])
