from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from ModelInterface import ModelInterface


class ModelSummarizer(ModelInterface):

    def __init__(self, model_name='t5-base', framework='pt'):
        ModelSummarizer.framework = framework
        ModelSummarizer.summarizer = pipeline("summarization")
        ModelSummarizer.tokenizer = AutoTokenizer.from_pretrained(model_name)
        ModelSummarizer.model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
        ModelSummarizer.min_tokens = 14
        ModelSummarizer.max_tokens = 512

    @staticmethod
    def summarize_with_pipeline(text, **kwargs):
        inputs = ModelSummarizer.tokenizer.encode('summarize: ' + text, return_tensors=ModelSummarizer.framework,
                                                  max_length=512, truncation=True)
        length = inputs.shape[1]
        if length < ModelSummarizer.min_tokens:
            return text
        elif length > ModelSummarizer.max_tokens:
            return text
        output = ModelSummarizer.model.generate(inputs, max_length=int(length * 1 / 2), min_length=40, length_penalty=2.0, num_beams=4,
                                       early_stopping=True)
        return ModelSummarizer.tokenizer.decode(output[0])

    @staticmethod
    def predict(input: str) -> str:
        return ModelSummarizer.summarize_with_pipeline(input)
