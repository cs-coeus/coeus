import spacy
from typing import Any
from spacy.pipeline import merge_entities
from models.ModelInterface import ModelInterface
from nltk.corpus import stopwords
import torch


class ModelSpacy(ModelInterface):

    def __init__(self):
        if torch.cuda.is_available():
            spacy.require_gpu()
        ModelSpacy.nlp = spacy.load('en_core_web_lg')
        ModelSpacy.nlp.add_pipe('merge_entities', last=True)
        ModelSpacy.stop_words = set(stopwords.words('english'))

    @staticmethod
    def get_spacy_instance(text):
        return ModelSpacy.nlp(text)

    @staticmethod
    def predict(input: str) -> Any:
        return ModelSpacy.get_spacy_instance(input)

    @staticmethod
    def convert_spacy_object_to_word_part_of_speech_dictionary(spacy_doc):
        dictionary = dict()
        for token in spacy_doc:
            dictionary[token] = token.pos_
        return dictionary

    @staticmethod
    def convert_spacy_object_to_noun_chunk_and_entity_type_array(spacy_doc):
        dictionary = dict()
        for chunk in spacy_doc.noun_chunks:
            if chunk.text not in ModelSpacy.stop_words:
                dictionary[chunk.text] = chunk.root.ent_type_
        array = list(dictionary.items())
        return array
