from transformers import pipeline
from models.ModelInterface import ModelInterface
from typing import Any, List, Tuple


class ModelQA(ModelInterface):

    def __init__(self):
        ModelQA.qa = pipeline('question-answering')
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
