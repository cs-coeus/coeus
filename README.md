# coeus
coeus project 

### Setup
    0.create virtual environment `python3 -m venv venv` and activate `source venv/bin/activate`
    1.install package according to requirement.txt `pip install transformers sentencepiece spacy[<cuda-version>] keybert nltk tensorflow requests scikit_learn numpy gensim pyemd torch`
    2.run `python -m spacy download en_core_web_lg`
    
### Contribution
    1.install pycodestyle and autopep8 `pip install --upgrade pycodestyle autopep8`
    2.run `autopep8 --in-place --aggressive --aggressive --exclude=<your-venv-folder> --recursive .`