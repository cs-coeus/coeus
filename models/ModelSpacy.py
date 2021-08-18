import spacy
from typing import Any
from models.ModelInterface import ModelInterface


class ModelSpacy(ModelInterface):

    def __init__(self):
        ModelSpacy.nlp = spacy.load('en_core_web_sm')

    @staticmethod
    def get_spacy_instance(text):
        return ModelSpacy.nlp(text)

    @staticmethod
    def predict(input: str) -> Any:
        return ModelSpacy.get_spacy_instance(input)
