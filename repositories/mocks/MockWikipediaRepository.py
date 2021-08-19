import os

from repositories.DataRepository import DataRepository


class MockWikipediaRepository(DataRepository):

    def __init__(self):
        PATH_TO_MOCK_DATA = 'coeus/articles/kmutt/text.txt'
        cwd = os.getcwd()
        user_path = cwd.split('coeus')[0]
        data_path = os.path.join(user_path, PATH_TO_MOCK_DATA)
        file = open(data_path, 'r')
        MockWikipediaRepository.mock_data = file.read()
        file.close()

    @staticmethod
    def getData(input: str) -> str:
        return MockWikipediaRepository.mock_data
