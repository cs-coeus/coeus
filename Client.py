from sklearn.metrics import pairwise_distances
from InputPreparator import InputPreparator
from ModelSummarizer import ModelSummarizer
from ModelQA import ModelQA
from ModelKeyBert import ModelKeyBert
from ModelClustering import ModelClustering
from ModelSpacy import ModelSpacy
from WikiRepository import WikiRepository
import numpy as np


class Client:

    def __init__(self):
        Client.input_preparator = InputPreparator()
        Client.summarize_model = ModelSummarizer()
        Client.qa_model = ModelQA()
        Client.keybert_model = ModelKeyBert()
        Client.clustering_model = ModelClustering()
        Client.spacy_model = ModelSpacy()
        Client.wiki_repo = WikiRepository()
        Client.paragraph_escape_character = '_paragraph'

    @staticmethod
    def generate_mind_map_from_semi_structure_text(wiki_url):
        input_dictionary = Client.input_preparator.normalize_text_from_wikipedia(
            Client.wiki_repo.getData(wiki_url))

        return Client.transform_original_text_to_mind_map(
            Client.generate_original_text_dictionary_from_normalize_input(input_dictionary))

    @staticmethod
    def generate_mind_map_from_unstructured_text(title, paragraphs):
        input_dictionary = {title: {
            Client.paragraph_escape_character: [para.strip() for para in paragraphs.split("\n") if
                                                len(para.strip()) > 0]
        }}
        return Client.transform_original_text_to_mind_map(
            input_dictionary)

    @staticmethod
    def generate_original_text_dictionary_from_normalize_input(input_data):

        def helper_function(article_path, dictionary, is_topic=True, current_text_in_paragraph=[]):
            if len(article_path) == 1:
                if is_topic:
                    dictionary[article_path[0]] = dict()
                elif not is_topic:
                    dictionary[article_path[0]][Client.paragraph_escape_character] = current_text_in_paragraph
            elif len(article_path) > 1:
                curr_dict = dictionary.get(article_path[0])
                helper_function(article_path[1:], curr_dict, is_topic, current_text_in_paragraph)

        topic_escape_char = '='
        root = dict()
        curr_path = []
        last_level = 0
        for line in input_data:
            if isinstance(line, str):
                new_level = line.count(topic_escape_char) / 2
                new_topic = line.replace(topic_escape_char, '').strip()
                if last_level == new_level:
                    curr_path = curr_path[:-1] + [new_topic]
                    helper_function(curr_path, root)
                elif last_level < new_level:
                    curr_path += [new_topic]
                    helper_function(curr_path, root)
                elif last_level > new_level:
                    curr_path = curr_path[:int(new_level) - 1] + [new_topic]
                    helper_function(curr_path, root)
                last_level = new_level
            else:
                helper_function(curr_path, root, False, line)
        return root

    @staticmethod
    def transform_original_text_to_mind_map(input_dictionary):

        def helper_function(input_dict):
            all_key = list(input_dict.keys())
            if len(all_key) == 1 and all_key[0] == Client.paragraph_escape_character:
                result = list(
                    map(lambda paragraph: Client.algorithm(paragraph, paragraph),
                        input_dict[Client.paragraph_escape_character]))
                input_dict[Client.paragraph_escape_character] = list(
                    filter(lambda paragraph_result: (paragraph_result is not None), result))
            else:
                for key in filter(lambda x: x != Client.paragraph_escape_character, all_key):
                    helper_function(input_dict[key])
                if Client.paragraph_escape_character in all_key:
                    result = list(
                        map(lambda paragraph: Client.algorithm(paragraph, paragraph),
                            input_dict[Client.paragraph_escape_character]))
                    input_dict[Client.paragraph_escape_character] = list(filter(lambda x: (x is not None), result))

        topic_dict = input_dictionary.get(list(input_dictionary.keys())[0])
        helper_function(topic_dict)
        return input_dictionary

    @staticmethod
    def algorithm(original_text, curr_sentence):
        min_sentence_threshold = 7
        summary = Client.summarize_model.predict(curr_sentence)
        doc = Client.spacy_model.predict(summary)
        sentences = list(doc.sents)
        if len(sentences) <= min_sentence_threshold:
            keys = Client.keybert_model.predict(curr_sentence)
            all_keys_child = []
            if keys:
                for key in keys:
                    result_of_q = Client.qa_model.predict((original_text, key, ['What is ', 'Where is ']))
                    key_map = {'keywords': key, '_child': result_of_q}
                    all_keys_child += [key_map]
                return all_keys_child
            else:
                return

        else:
            data = [sent.text for sent in sentences]
            X = np.arange(len(data)).reshape(-1, 1)

            def distance(x, y):
                return Client.clustering_model.wmd.wmdistance(Client.input_preparator.preprocess(data[int(x[0])]),
                                                              Client.input_preparator.preprocess(data[int(y[0])]))

            proximity_matrix = pairwise_distances(X, X, metric=distance)
            best_k, best_cluster = Client.clustering_model.predict(X, len(sentences), proximity_matrix)
            if np.all(best_cluster == best_cluster[0]):
                keys = Client.keybert_model.predict(curr_sentence)
                all_keys_child = []
                if keys:
                    for key in keys:
                        result_of_q = Client.qa_model.predict((original_text, key, ['What is ', 'Where is ']))
                        key_map = {'keywords': key, '_child': result_of_q}
                        all_keys_child += [key_map]
                    return all_keys_child
            return Client.algorithm(original_text, sentences.join('. '))
