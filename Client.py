from sklearn.metrics import pairwise_distances
from utils.InputPreparator import InputPreparator
from utils.OutputPreparator import OutputPreparator
from models.ModelSummarizer import ModelSummarizer
from models.ModelQA import ModelQA
from models.ModelClustering import ModelClustering
from models.ModelSpacy import ModelSpacy
from models.ModelGensim import ModelGensim
from repositories.WikipediaRepository import WikipediaRepository
from functools import reduce
import numpy as np


class Client:

    def __init__(self):
        Client.gensim_model = ModelGensim()
        Client.input_preparator = InputPreparator()
        Client.summarize_model = ModelSummarizer()
        Client.qa_model = ModelQA()
        Client.clustering_model = ModelClustering()
        Client.spacy_model = ModelSpacy()
        Client.wikipedia_repository = WikipediaRepository()
        Client.output_preparator = OutputPreparator()
        Client.paragraph_escape_character = '_paragraph'
        Client.ID_KEY_STRING = 'id'
        Client.TEXT_KEY_STRING = 'text'
        Client.PARENT_ID_KEY_STRING = 'parentId'
        Client.CHILD_ID_KEY_STRING = 'childId'
        Client.KEYWORDS_ESCAPE_CHARACTER = 'keywords'
        Client.CURRENT_ID_KEY_STRING = 'current_id'
        Client.ENTITIES_QUESTION = {
            '': ['What is'],
            'CARDINAL': [],
            'DATE': ['What happend on'],
            'EVENT': ['What is the', 'When is the', 'Where is the'],
            'FAC': ['What is', 'Where is'],
            'GPE': [],
            'LANGUAGE': [],
            'LAW': ['What is'],
            'LOC': ['What is', 'Where is'],
            'MONEY': [],
            'NORP': ['What is'],
            'ORDINAL': [],
            'ORG': ['What is', 'Where is'],
            'PERCENT': [],
            'PERSON': ['Who is'],
            'PRODUCT': ['What is', 'How expensive is the', 'How to use'],
            'QUANTITY': [],
            'TIME': [],
            'WORK_OF_ART': ['What is']
        }

    @staticmethod
    def generate_mind_map_from_semi_structure_text(
            wikipedia_article_title_url):
        wikipedia_text = Client.wikipedia_repository.getData(
            wikipedia_article_title_url)
        input_array = Client.input_preparator.normalize_wikipedia_data(
            wikipedia_text)

        paragraph_array_of_array = filter(
            lambda array_of_paragraph: not isinstance(
                array_of_paragraph, str), input_array)
        paragraph_text_array = ['\n'.join(paragraph)
                                for paragraph in paragraph_array_of_array]
        full_text = reduce(
            lambda body_1,
            body_2: body_1 + '\n' + body_2,
            paragraph_text_array)

        output = Client.convert_to_final_json(
            Client.convert_to_intermediate_json(
                Client.generate_original_text_dictionary_from_normalized_input(
                    input_array),
                full_text))

        post_processed = OutputPreparator.post_processing(output)
        return post_processed

    @staticmethod
    def generate_mind_map_from_unstructured_text(title, paragraphs):
        input_dictionary = {
            title: {
                Client.paragraph_escape_character: [
                    paragraph.strip() for paragraph in paragraphs.split('\n') if len(
                        paragraph.strip()) > 0]}}

        output = Client.convert_to_final_json(
            Client.convert_to_intermediate_json(input_dictionary, paragraphs))

        post_processed = OutputPreparator.post_processing(output)
        return post_processed

    @staticmethod
    def generate_original_text_dictionary_from_normalized_input(input_data):

        def recursive_generate_dictionary_from_paragraphs_array(
                article_path, dictionary, is_topic=True, current_text_in_paragraph=[]):
            if len(article_path) == 1:
                if is_topic:
                    dictionary[article_path[0]] = dict()
                elif not is_topic:
                    dictionary[article_path[0]
                               ][Client.paragraph_escape_character] = current_text_in_paragraph
            elif len(article_path) > 1:
                curr_dict = dictionary.get(article_path[0])
                recursive_generate_dictionary_from_paragraphs_array(
                    article_path[1:], curr_dict, is_topic, current_text_in_paragraph)

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
                    recursive_generate_dictionary_from_paragraphs_array(
                        curr_path, root)
                elif last_level < new_level:
                    curr_path += [new_topic]
                    recursive_generate_dictionary_from_paragraphs_array(
                        curr_path, root)
                elif last_level > new_level:
                    curr_path = curr_path[:int(new_level) - 1] + [new_topic]
                    recursive_generate_dictionary_from_paragraphs_array(
                        curr_path, root)
                last_level = new_level
            else:
                recursive_generate_dictionary_from_paragraphs_array(
                    curr_path, root, False, line)
        return root

    @staticmethod
    def convert_to_intermediate_json(original_text_dict, full_text):
        common_data = {
            Client.CURRENT_ID_KEY_STRING: 0
        }

        def generate_node(_id, _text, _parent_id):
            return {
                Client.ID_KEY_STRING: _id,
                Client.TEXT_KEY_STRING: _text,
                Client.PARENT_ID_KEY_STRING: _parent_id
            }

        def get_next_id(_common_data):
            _common_data[Client.CURRENT_ID_KEY_STRING] = _common_data[Client.CURRENT_ID_KEY_STRING] + 1
            return _common_data[Client.CURRENT_ID_KEY_STRING]

        def recursive_apply_algorithm_to_paragraph(
                input_dict, _common_data, _array_of_nodes, _parent_id):
            all_key = list(input_dict.keys())
            if len(
                    all_key) == 1 and all_key[0] == Client.paragraph_escape_character:
                current_paragraph_dictionary = dict()
                result = list(
                    map(lambda paragraph: Client.algorithm(paragraph, paragraph, full_text,
                                                           current_paragraph_dictionary,
                                                           _common_data, _array_of_nodes, _parent_id, get_next_id,
                                                           generate_node),
                        input_dict[Client.paragraph_escape_character]))
                input_dict[Client.paragraph_escape_character] = current_paragraph_dictionary
            else:
                for key in filter(
                        lambda x: x != Client.paragraph_escape_character,
                        all_key):
                    current_node = generate_node(
                        get_next_id(common_data), key, _parent_id)
                    _array_of_nodes.append(current_node)
                    recursive_apply_algorithm_to_paragraph(input_dict[key], _common_data, _array_of_nodes,
                                                           current_node[Client.ID_KEY_STRING])
                if Client.paragraph_escape_character in all_key:
                    current_paragraph_dictionary = dict()
                    result = list(
                        map(lambda paragraph: Client.algorithm(paragraph, paragraph, full_text,
                                                               current_paragraph_dictionary,
                                                               _common_data, _array_of_nodes, _parent_id, get_next_id,
                                                               generate_node),
                            input_dict[Client.paragraph_escape_character]))
                    input_dict[Client.paragraph_escape_character] = current_paragraph_dictionary

        topic_dict = original_text_dict.get(list(original_text_dict.keys())[0])
        root_node = generate_node(
            get_next_id(common_data), list(
                original_text_dict.keys())[0], -1)
        array_of_nodes = [root_node]
        recursive_apply_algorithm_to_paragraph(
            topic_dict, common_data, array_of_nodes, root_node[Client.ID_KEY_STRING])
        return array_of_nodes

    @staticmethod
    def algorithm(
            original_text,
            curr_sentence,
            full_text,
            _this_paragraph_dictionary,
            _common_data,
            _array_of_nodes,
            _parent_id,
            _get_id,
            _get_node):
        MIN_SENTENCE_THRESHOLD = 7
        summary = Client.summarize_model.predict(curr_sentence)
        spacy_doc_from_summary = Client.spacy_model.predict(summary)
        sentences = list(spacy_doc_from_summary.sents)
        if len(sentences) <= MIN_SENTENCE_THRESHOLD:
            noun_ent_type_array = Client.spacy_model.convert_spacy_object_to_noun_chunk_and_entity_type_array(
                spacy_doc_from_summary)
            for noun, entity_type in noun_ent_type_array:
                current_level_node = _get_node(
                    _get_id(_common_data), noun, _parent_id)
                _array_of_nodes.append(current_level_node)
                if noun not in list(_this_paragraph_dictionary.keys()):
                    _this_paragraph_dictionary[noun] = dict()
                questions = Client.ENTITIES_QUESTION[entity_type]

                qa_model_result = [] if len(questions) == 0 else Client.qa_model.predict(
                    (original_text, noun, questions))
                result_answer = list(map(
                    lambda tuple_of_question_answer: tuple_of_question_answer[1], qa_model_result))
                for answer in result_answer:
                    _array_of_nodes.append(_get_node(
                        _get_id(_common_data), answer, current_level_node[Client.ID_KEY_STRING]))
                    _this_paragraph_dictionary[noun][answer] = dict()
            return
        else:
            data = [sent.text for sent in sentences]
            X = np.arange(len(data)).reshape(-1, 1)

            def distance(x, y):
                return Client.gensim_model.get_wmd_distance(Client.input_preparator.preprocess(
                    data[int(x[0])]), Client.input_preparator.preprocess(data[int(y[0])]))

            proximity_matrix = pairwise_distances(X, X, metric=distance)
            best_k, best_cluster = Client.clustering_model.predict(
                X, len(sentences), proximity_matrix)
            if np.all(best_cluster == best_cluster[0]):
                noun_ent_type_array = Client.spacy_model.convert_spacy_object_to_noun_chunk_and_entity_type_array(
                    spacy_doc_from_summary)
                for noun, entity_type in noun_ent_type_array:
                    current_level_node = _get_node(
                        _get_id(_common_data), noun, _parent_id)
                    _array_of_nodes.append(current_level_node)
                    if noun not in list(
                            _this_paragraph_dictionary.keys()):
                        _this_paragraph_dictionary[noun] = dict()
                    questions = Client.ENTITIES_QUESTION[entity_type]
                    qa_model_result = [] if len(questions) == 0 else Client.qa_model.predict(
                        (original_text, noun, questions))
                    result_answer = list(map(
                        lambda tuple_of_question_answer: tuple_of_question_answer[1], qa_model_result))
                    for answer in result_answer:
                        _array_of_nodes.append(_get_node(
                            _get_id(_common_data), answer, current_level_node[Client.ID_KEY_STRING]))
                        _this_paragraph_dictionary[noun][answer] = dict()
            return Client.algorithm(
                original_text,
                sentences.join('. '),
                full_text,
                _this_paragraph_dictionary,
                _common_data,
                _array_of_nodes,
                _parent_id,
                _get_id,
                _get_node)

    @staticmethod
    def convert_to_final_json(intermediate_json):
        final_json = {
            'nodes': [
                {
                    Client.ID_KEY_STRING: node[Client.ID_KEY_STRING],
                    Client.TEXT_KEY_STRING: node[Client.TEXT_KEY_STRING]
                }
                for node in intermediate_json
            ],
            'edges': [
                {
                    Client.PARENT_ID_KEY_STRING: node[Client.PARENT_ID_KEY_STRING],
                    Client.CHILD_ID_KEY_STRING: node[Client.ID_KEY_STRING]
                }
                for node in intermediate_json if node[Client.PARENT_ID_KEY_STRING] != -1
            ]
        }
        return final_json
