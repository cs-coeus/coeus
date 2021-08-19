from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from models.ModelInterface import ModelInterface


class ModelSummarizer(ModelInterface):

    def __init__(self, model_name='t5-base', framework='pt'):
        ModelSummarizer.framework = framework
        ModelSummarizer.tokenizer = AutoTokenizer.from_pretrained(model_name)
        ModelSummarizer.model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
        ModelSummarizer.MIN_TOKENS = 14
        ModelSummarizer.MIN_LENGTH = 40
        ModelSummarizer.MAX_TOKENS = 512
        ModelSummarizer.LENGTH_PENALTY = 2.0
        ModelSummarizer.NUM_BEAMS = 4

    @staticmethod
    def summarize_with_pipeline(text, **kwargs):
        inputs = ModelSummarizer.tokenizer.encode('summarize: ' + text, return_tensors=ModelSummarizer.framework,
                                                  max_length=ModelSummarizer.MAX_TOKENS, truncation=True)
        length = inputs.shape[1]
        if length < ModelSummarizer.MIN_TOKENS:
            return text
        elif length > ModelSummarizer.MAX_TOKENS:
            return text
        output = ModelSummarizer.model.generate(inputs, max_length=int(length * 1 / 2),
                                                min_length=ModelSummarizer.MIN_LENGTH,
                                                length_penalty=ModelSummarizer.LENGTH_PENALTY,
                                                num_beams=ModelSummarizer.NUM_BEAMS,
                                                early_stopping=True)
        return ModelSummarizer.tokenizer.decode(output[0])

    @staticmethod
    def predict(input: str) -> str:
        return ModelSummarizer.summarize_with_pipeline(input)
