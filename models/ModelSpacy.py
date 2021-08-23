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
