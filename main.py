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

input_p = InputPreparator()
print(input_p.normalize_text_from_wikipedia("""= test1 = \n 123"""))

summarizer_model = ModelSummarizer()
print(summarizer_model.predict(test_text))

qa_model = ModelQA()
tuple_test = (test_text_qa, ('Apple', 0.6), ['What is '])
print(tuple_test)
print(qa_model.predict(tuple_test))

keybert_model = ModelKeyBert()
print(keybert_model.predict(test_text_key))

sents = ['Obama speaks to the media in Illinois', 'The president greets the press in Chicago',
         'Obama speaks to the media in Illinois', 'The president greets the press in Chicago',
         'Obama speaks to the media in Illinois', 'The president greets the press in Chicago',
         'Obama speaks to the media in Illinois', 'The president greets the press in Chicago',
         'The president greets the press in Chicago', 'The president greets the press in Chicago',
         'Oranges are my favorite fruit']

clustering_model = ModelClustering()
# data = [sent.text for sent in sents]
data = sents
X = np.arange(len(data)).reshape(-1, 1)


def distance(x, y):
    return ModelClustering.wmd.wmdistance(input_p.preprocess_senetence_to_arr(data[int(x[0])]),
                                          input_p.preprocess_senetence_to_arr(data[int(y[0])]))


proximity_matrix = pairwise_distances(X, X, metric=distance)
best_k, best_cluster = clustering_model.predict((X, len(sents), proximity_matrix))

print(best_k, best_cluster)

spacy_model = ModelSpacy()
print(list(spacy_model.predict(test_text).sents))

wiki_repo = WikiRepository()
print(InputPreparator.normalize_text_from_wikipedia(
    WikiRepository.getData("""King_Mongkut's_University_of_Technology_Thonburi""")))
