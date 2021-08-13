from sklearn.metrics import pairwise_distances

from InputPreparator import InputPreparator
from ModelSummarizer import ModelSummarizer
from ModelQA import ModelQA
from ModelKeyBert import ModelKeyBert
from ModelClustering import ModelClustering
from ModelSpacy import ModelSpacy
import numpy as np
from WikiRepository import WikiRepository

test_text = 'When completed in 2023, the CENI facility will become a prototype "future internet" connecting to almost everything - from computers at home to cars on the street - for seamless communications in an AI-driven society.KMUTT is a university.'

test_text_qa = 'Apple is a fruit. Apple is red. Apple is delicious.'
test_text_key = 'KMUTT is a university'

inputP = InputPreparator()
print(inputP.normalize_text_from_wikipedia("""= test1 = \n 123"""))

summarizerModel = ModelSummarizer()
print(summarizerModel.predict(test_text))

qaModel = ModelQA()
tuple_test = (test_text_qa, ('Apple', 0.6), ['What is '])
print(tuple_test)
print(qaModel.predict(tuple_test))

keybertModel = ModelKeyBert()
print(keybertModel.predict(test_text_key))

sents = ['Obama speaks to the media in Illinois', 'The president greets the press in Chicago',
         'Obama speaks to the media in Illinois', 'The president greets the press in Chicago',
         'Obama speaks to the media in Illinois', 'The president greets the press in Chicago',
         'Obama speaks to the media in Illinois', 'The president greets the press in Chicago',
         'The president greets the press in Chicago', 'The president greets the press in Chicago',
         'Oranges are my favorite fruit']

clusteringModel = ModelClustering()
# data = [sent.text for sent in sents]
data = sents
X = np.arange(len(data)).reshape(-1, 1)


def distance(x, y):
    return ModelClustering.wmd.wmdistance(inputP.preprocess_senetence_to_arr(data[int(x[0])]),
                                          inputP.preprocess_senetence_to_arr(data[int(y[0])]))


proximity_matrix = pairwise_distances(X, X, metric=distance)
best_k, best_cluster = clusteringModel.predict((X, len(sents), proximity_matrix))

print(best_k, best_cluster)

spacyModel = ModelSpacy()
print(list(spacyModel.predict(test_text).sents))

wikiRepo = WikiRepository()
print(InputPreparator.normalize_text_from_wikipedia(
    WikiRepository.getData("""King_Mongkut's_University_of_Technology_Thonburi""")))
