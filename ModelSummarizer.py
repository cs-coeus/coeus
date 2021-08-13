from transformers import pipeline, AutoTokenizer
from ModelInterface import ModelInterface


class ModelSummarizer(ModelInterface):

    def __init__(self, model_name='t5-base', framework='tf'):
        ModelSummarizer.framework = framework
        ModelSummarizer.summarizer = pipeline('summarization', model=model_name, tokenizer=model_name,
                                              framework=framework)
        ModelSummarizer.tokenizer = AutoTokenizer.from_pretrained(model_name)
        ModelSummarizer.min_tokens = 14
        ModelSummarizer.max_tokens = 1024

    @staticmethod
    def summarize_with_pipeline(text, **kwargs):
        inputs = ModelSummarizer.tokenizer.encode(text, return_tensors=ModelSummarizer.framework)
        length = inputs.shape[1]
        if length < ModelSummarizer.min_tokens:
            return text
        elif length > ModelSummarizer.max_tokens:
            return ''
        output = ModelSummarizer.summarizer(text, max_length=int(length * 1 / 2), min_length=int(length * 1 / 10),
                                            **kwargs)
        return output[0]['summary_text']

    @staticmethod
    def predict(input: str) -> str:
        return ModelSummarizer.summarize_with_pipeline(input)
