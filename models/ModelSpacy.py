import spacy
from typing import Any
from models.ModelInterface import ModelInterface
import torch


class ModelSpacy(ModelInterface):

    def __init__(self):
        if torch.cuda.is_available():
            spacy.require_gpu()
        ModelSpacy.nlp = spacy.load('en_core_web_sm')

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
    def convert_spacy_object_to_noun_chunk_array(spacy_doc):
        array = []
        for chunk in spacy_doc.noun_chunks:
            array.append(chunk.text)
        return array
