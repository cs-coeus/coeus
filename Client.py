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
        Client.id_key_string = 'id'
        Client.text_key_string = 'text'
        Client.parent_id_key_string = 'parentId'
        Client.child_id_key_string = 'childId'
        Client.keywords_escape_character = 'keywords'
        Client.child_escape_character = '_child'
        Client.current_id_key_string = 'current_id'

    @staticmethod
    def generate_mind_map_from_semi_structure_text(wiki_url):
        input_array = Client.input_preparator.normalize_text_from_wikipedia(
            Client.wiki_repo.getData(wiki_url))

        return Client.transform_intermediate_json_to_final(Client.transform_original_text_to_intermediate_json_mind_map(
            Client.generate_original_text_dictionary_from_normalize_input(input_array)))

    @staticmethod
    def generate_mind_map_from_unstructured_text(title, paragraphs):
        input_dictionary = {title: {
            Client.paragraph_escape_character: [para.strip() for para in paragraphs.split("\n") if
                                                len(para.strip()) > 0]
        }}
        return Client.transform_intermediate_json_to_final(Client.transform_original_text_to_intermediate_json_mind_map(
            input_dictionary))

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
    def transform_original_text_to_intermediate_json_mind_map(input_dictionary):
        common_data = {
            Client.current_id_key_string: 0
        }

        def get_node(_id, _text, _parent_id):
            return {
                Client.id_key_string: _id,
                Client.text_key_string: _text,
                Client.parent_id_key_string: _parent_id
            }

        def get_id(_common_data):
            _common_data[Client.current_id_key_string] = _common_data[Client.current_id_key_string] + 1
            return _common_data[Client.current_id_key_string]

        def helper_function(input_dict, _common_data, _array_of_nodes, _parent_id):
            all_key = list(input_dict.keys())
            if len(all_key) == 1 and all_key[0] == Client.paragraph_escape_character:
                this_paragraph_dictionary = dict()
                result = list(
                    map(lambda paragraph: Client.algorithm(paragraph, paragraph, this_paragraph_dictionary,
                                                           _common_data, _array_of_nodes, _parent_id, get_id, get_node),
                        input_dict[Client.paragraph_escape_character]))
                input_dict[Client.paragraph_escape_character] = this_paragraph_dictionary
            else:
                for key in filter(lambda x: x != Client.paragraph_escape_character, all_key):
                    current_node = get_node(get_id(common_data), key, _parent_id)
                    _array_of_nodes.append(current_node)
                    helper_function(input_dict[key], _common_data, _array_of_nodes, current_node[Client.id_key_string])
                if Client.paragraph_escape_character in all_key:
                    this_paragraph_dictionary = dict()
                    result = list(
                        map(lambda paragraph: Client.algorithm(paragraph, paragraph, this_paragraph_dictionary,
                                                               _common_data, _array_of_nodes, _parent_id, get_id,
                                                               get_node),
                            input_dict[Client.paragraph_escape_character]))
                    input_dict[Client.paragraph_escape_character] = this_paragraph_dictionary

        topic_dict = input_dictionary.get(list(input_dictionary.keys())[0])
        root_node = get_node(get_id(common_data), list(input_dictionary.keys())[0], -1)
        array_of_nodes = [root_node]
        helper_function(topic_dict, common_data, array_of_nodes, root_node[Client.id_key_string])
        return array_of_nodes

    @staticmethod
    def algorithm(original_text, curr_sentence, _this_paragraph_dictionary, _common_data, _array_of_nodes, _parent_id,
                  _get_id, _get_node):
        min_sentence_threshold = 7
        summary = Client.summarize_model.predict(curr_sentence)
        doc = Client.spacy_model.predict(summary)
        sentences = list(doc.sents)
        if len(sentences) <= min_sentence_threshold:
            keys = Client.keybert_model.predict(curr_sentence)
            if keys:
                for key in keys:
                    current_level_node = _get_node(_get_id(_common_data), key[0], _parent_id)
                    _array_of_nodes.append(current_level_node)
                    if key[0] not in list(_this_paragraph_dictionary.keys()):
                        _this_paragraph_dictionary[key[0]] = dict()
                    result_of_q = Client.qa_model.predict((original_text, key, ['What is ', 'Where is ']))
                    result_answer = list(map(lambda tuple_of_question_answer: tuple_of_question_answer[1], result_of_q))
                    for ans in result_answer:
                        _array_of_nodes.append(
                            _get_node(_get_id(_common_data), ans, current_level_node[Client.id_key_string]))
                        _this_paragraph_dictionary[key[0]][ans] = dict()
                return
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
                if keys:
                    for key in keys:
                        current_level_node = _get_node(_get_id(_common_data), key[0], _parent_id)
                        _array_of_nodes.append(current_level_node)
                        if key[0] not in list(_this_paragraph_dictionary.keys()):
                            _this_paragraph_dictionary[key[0]] = dict()
                        result_of_q = Client.qa_model.predict((original_text, key, ['What is ', 'Where is ']))
                        result_answer = list(
                            map(lambda tuple_of_question_answer: tuple_of_question_answer[1], result_of_q))
                        for ans in result_answer:
                            _array_of_nodes.append(
                                _get_node(_get_id(_common_data), ans, current_level_node[Client.id_key_string]))
                            _this_paragraph_dictionary[key[0]][ans] = dict()
                    return
            return Client.algorithm(original_text, sentences.join('. '))

    @staticmethod
    def transform_intermediate_json_to_final(intermediate_json):
        final_json = {
            'nodes': [
                {Client.id_key_string: node[Client.id_key_string], Client.text_key_string: node[Client.text_key_string]}
                for node in intermediate_json],
            'edges': [{Client.parent_id_key_string: node[Client.parent_id_key_string],
                       Client.child_id_key_string: node[Client.id_key_string]} for node in intermediate_json if
                      node[Client.parent_id_key_string] != -1]
        }
        return final_json
