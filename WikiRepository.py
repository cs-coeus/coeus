from DataRepository import DataRepository
import requests
from typing import Any, List


class WikiRepository(DataRepository):
    @staticmethod
    def get_text_from_wiki(title):
        page = requests.get(
            "https://en.wikipedia.org/w/api.php?action=query&format=json&titles=%s"
            "&prop=extracts&explaintext" % title).json()["query"]["pages"]
        if len(page.keys()) == 1:
            return "= " + title.replace('_', ' ') + " =\n" + next(iter(page.values()))["extract"]
        raise Exception("No article found")

    @staticmethod
    def getData(input: str) -> List[Any]:
        return  WikiRepository.get_text_from_wiki(input)
