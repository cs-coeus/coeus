import os

from repositories.DataRepository import DataRepository


class MockWikiRepo(DataRepository):

    def __init__(self):
        PATH_TO_MOCK_DATA = 'coeus/articles/kmutt/text.txt'
        cwd = os.getcwd()
        user_path = cwd.split('coeus')[0]
        data_path = os.path.join(user_path,PATH_TO_MOCK_DATA)
        file = open(data_path, 'r')
        MockWikiRepo.mock_data = file.read()

    @staticmethod
    def getData(input: str) -> str:
        return MockWikiRepo.mock_data
