from transformers import pipeline
from models.ModelInterface import ModelInterface
from typing import Any, List, Tuple
import torch


class ModelQA(ModelInterface):

    def __init__(self, framework='pt'):
        ModelQA.device = torch.cuda.current_device() if torch.cuda.is_available() else -1
        ModelQA.qa = pipeline(
            'question-answering',
            device=ModelQA.device,
            framework=framework)
        ModelQA.ANSWER_THRESHOLD = 0.8

    @staticmethod
    def QA(original, keyword, questions):
        ans_of_key = []
        for question in questions:
            q = question + keyword[0] + ' ?'
            result = ModelQA.qa(question=q, context=original)
            if round(result['score'], 4) > ModelQA.ANSWER_THRESHOLD:
                ans_of_key += [(q, result['answer'])]
        return ans_of_key

    @staticmethod
    def predict(input: Tuple[str, Tuple[str, int], List[str]]) -> List[Any]:
        return ModelQA.QA(input[0], input[1], input[2])
