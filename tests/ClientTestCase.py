import os
import unittest
from Client import Client
from repositories.mocks.MockWikipediaRepository import MockWikipediaRepository


class ClientTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.client = Client()
        Client.wiki_repo = MockWikipediaRepository()

    def test_generate_mind_map_from_semi_structure_text(self):
        expected_result_output = {
            'nodes': [
                {'id': 1, 'text': "King Mongkut's University of Technology Thonburi"},
                {'id': 2, 'text': 'History'},
                {'id': 3, 'text': 'established february 1960 department vocational'},
                {'id': 4, 'text': 'Governance and organisation'},
                {'id': 5, 'text': 'regalia great crown victory sword'},
                {'id': 6, 'text': 'Faculties and Schools'},
                {'id': 7, 'text': 'School of Architecture and Design'},
                {'id': 8, 'text': 'school changed school architecture school'},
                {'id': 9, 'text': 'kmutt following faculties schools'},
                {'id': 10, 'text': 'KMUTT'},
                {'id': 11, 'text': 'faculty engineering foe'},
                {'id': 12, 'text': 'science fsci'},
                {'id': 13, 'text': 'Faculty of Science'},
                {'id': 14, 'text': 'Faculty of Science'},
                {'id': 15, 'text': 'faculty industrial education technology fiet'},
                {'id': 16, 'text': 'school liberal arts sola'},
                {'id': 17, 'text': 'school information technology sit'},
                {'id': 18, 'text': 'school architecture design soa'},
                {'id': 19, 'text': 'school energy environment materials'},
                {'id': 20, 'text': 'school bioresources technology sbt'},
                {'id': 21, 'text': 'School of Bioresources and Technology'},
                {'id': 22, 'text': 'graduate school energy environment jgsee'},
                {'id': 23, 'text': 'Join Graduate School of Energy and Environment'},
                {'id': 24, 'text': 'Join'},
                {'id': 25, 'text': 'institute field robotics fibo'},
                {'id': 26, 'text': 'Institute of Field Robotics'},
                {'id': 27, 'text': 'graduate school management innovation gmi'},
                {'id': 28, 'text': 'college multidisciplinary sciences'},
                {'id': 29, 'text': 'College of Multidisciplinary Sciences'},
                {'id': 30, 'text': 'Student life'},
                {'id': 31, 'text': 'sports complex includes facilities gymnasium'},
                {'id': 32, 'text': 'support mission university provide education'},
                {'id': 33, 'text': 'information technology'},
                {'id': 34, 'text': 'kmutt residence independent non profit'},
                {'id': 35, 'text': 'student activities sports services sports'},
                {'id': 36, 'text': 'Campuses'},
                {'id': 37, 'text': 'Bangmod main campus'},
                {'id': 38, 'text': 'area main campus 52 acres'},
                {'id': 39, 'text': 'Bang Mot'},
                {'id': 40, 'text': 'Bang Khun Thian Campus'},
                {'id': 41, 'text': 'khun thian campus 80 acres'},
                {'id': 42, 'text': 'Ratchaburi Campus'},
                {'id': 43, 'text': 'bangmod campus bangkok 500 million'},
                {'id': 44, 'text': 'Bangkok'},
                {'id': 45, 'text': 'Main campus dormitories'},
                {'id': 46, 'text': 'dormitory completed 130 million baht'},
                {'id': 47, 'text': 'Transportation'},
                {'id': 48, 'text': 'free bus service bangmod campus'},
                {'id': 49, 'text': 'KMUTT'},
                {'id': 50, 'text': 'KMUTT Library'},
                {'id': 51, 'text': 'october 2000 changed kmutt library'},
                {'id': 52, 'text': 'school seventh oldest university thailand'}
            ],
            'edges': [
                {'parentId': 1, 'childId': 2},
                {'parentId': 2, 'childId': 3},
                {'parentId': 1, 'childId': 4},
                {'parentId': 4, 'childId': 5},
                {'parentId': 1, 'childId': 6},
                {'parentId': 6, 'childId': 7},
                {'parentId': 7, 'childId': 8},
                {'parentId': 6, 'childId': 9},
                {'parentId': 9, 'childId': 10},
                {'parentId': 6, 'childId': 11},
                {'parentId': 6, 'childId': 12},
                {'parentId': 12, 'childId': 13},
                {'parentId': 12, 'childId': 14},
                {'parentId': 6, 'childId': 15},
                {'parentId': 6, 'childId': 16},
                {'parentId': 6, 'childId': 17},
                {'parentId': 6, 'childId': 18},
                {'parentId': 6, 'childId': 19},
                {'parentId': 6, 'childId': 20},
                {'parentId': 20, 'childId': 21},
                {'parentId': 6, 'childId': 22},
                {'parentId': 22, 'childId': 23},
                {'parentId': 22, 'childId': 24},
                {'parentId': 6, 'childId': 25},
                {'parentId': 25, 'childId': 26},
                {'parentId': 6, 'childId': 27},
                {'parentId': 6, 'childId': 28},
                {'parentId': 28, 'childId': 29},
                {'parentId': 1, 'childId': 30},
                {'parentId': 30, 'childId': 31},
                {'parentId': 30, 'childId': 32},
                {'parentId': 32, 'childId': 33},
                {'parentId': 30, 'childId': 34},
                {'parentId': 30, 'childId': 35},
                {'parentId': 1, 'childId': 36},
                {'parentId': 36, 'childId': 37},
                {'parentId': 37, 'childId': 38},
                {'parentId': 38, 'childId': 39},
                {'parentId': 36, 'childId': 40},
                {'parentId': 40, 'childId': 41},
                {'parentId': 36, 'childId': 42},
                {'parentId': 42, 'childId': 43},
                {'parentId': 43, 'childId': 44},
                {'parentId': 36, 'childId': 45},
                {'parentId': 45, 'childId': 46},
                {'parentId': 1, 'childId': 47},
                {'parentId': 47, 'childId': 48},
                {'parentId': 48, 'childId': 49},
                {'parentId': 1, 'childId': 50},
                {'parentId': 50, 'childId': 51},
                {'parentId': 1, 'childId': 52}
            ]
        }
        actual_result = Client.generate_mind_map_from_semi_structure_text(
            """King_Mongkut's_University_of_Technology_Thonburi""")
        expected_string = str(expected_result_output)
        actual_string = str(actual_result)
        self.assertEqual(
            expected_string,
            actual_string,
            'structured: kmutt final output is not same as expected')

    def test_generate_mind_map_from_unstructured_text(self):
        expected_result_output = {
            'nodes': [
                {'id': 1, 'text': 'News - Apple helps Encircle expand its support for LGBTQ+ youth and their families'},
                {'id': 2, 'text': 'handful gay students high school'},
                {'id': 3, 'text': 'micah really did save life'},
                {'id': 4, 'text': 'founded 2017 help young lgbtq'},
                {'id': 5, 'text': 'Encircle'},
                {'id': 6, 'text': 'donations valued million help kickstart'},
                {'id': 7, 'text': 'handful gay students high school'},
                {'id': 8, 'text': 'micah really did save life'},
                {'id': 9, 'text': 'founded 2017 help young lgbtq'},
                {'id': 10, 'text': 'Encircle'},
                {'id': 11, 'text': 'donations valued million help kickstart'},
                {'id': 12, 'text': 'families number services including free'},
                {'id': 13, 'text': 'Encircle'},
                {'id': 14, 'text': 'counselors school saving kids lives'},
                {'id': 15, 'text': 'my school'},
                {'id': 16, 'text': 'micah toelupe'},
                {'id': 17, 'text': 'Micah Toelupe'},
                {'id': 18, 'text': 'helped countless families utah chrisann'},
                {'id': 19, 'text': 'Encircle'},
                {'id': 20, 'text': 'half lgbtq youth battling symptoms'},
                {'id': 21, 'text': 'depression'},
                {'id': 22, 'text': 'Encircle'},
                {'id': 23, 'text': 'understanding acceptance nonprofit prides communities'},
                {'id': 24, 'text': 'model worked 10 000 guests'},
                {'id': 25, 'text': 'daughter encircle khristian mission philippines'},
                {'id': 26, 'text': 'nonprofit helped foster deeper understanding'},
                {'id': 27, 'text': 'Encircle'},
                {'id': 28, 'text': 'focus welcoming lifeline lgbtq youth'},
                {'id': 29, 'text': 'lovely chosen family savannah says'},
                {'id': 30, 'text': 'painting self portrait micah mom'},
                {'id': 31, 'text': 'micah encircle did blossomed micah'},
                {'id': 32, 'text': 'Micah'},
                {'id': 33, 'text': 'encircle lgbtq youth family resource'},
                {'id': 34, 'text': 'Encircle'},
                {'id': 35, 'text': 'counselors school saving kids lives'},
                {'id': 36, 'text': 'my school'},
                {'id': 37, 'text': 'micah toelupe'},
                {'id': 38, 'text': 'Micah Toelupe'},
                {'id': 39, 'text': 'helped countless families utah chrisann'},
                {'id': 40, 'text': 'Encircle'},
                {'id': 41, 'text': 'half lgbtq youth battling symptoms'},
                {'id': 42, 'text': 'depression'},
                {'id': 43, 'text': 'Encircle'},
                {'id': 44, 'text': 'understanding acceptance nonprofit prides communities'},
                {'id': 45, 'text': 'model worked 10 000 guests'},
                {'id': 46, 'text': 'daughter encircle khristian mission philippines'},
                {'id': 47, 'text': 'nonprofit helped foster deeper understanding'},
                {'id': 48, 'text': 'Encircle'},
                {'id': 49, 'text': 'focus welcoming lifeline lgbtq youth'},
                {'id': 50, 'text': 'lovely chosen family savannah says'},
                {'id': 51, 'text': 'painting self portrait micah mom'},
                {'id': 52, 'text': 'micah encircle did blossomed micah'},
                {'id': 53, 'text': 'Micah'},
                {'id': 54, 'text': 'contribute visit encircle lgbtq youth'}
            ],
            'edges': [
                {'parentId': 1, 'childId': 2},
                {'parentId': 1, 'childId': 3},
                {'parentId': 1, 'childId': 4},
                {'parentId': 4, 'childId': 5},
                {'parentId': 1, 'childId': 6},
                {'parentId': 1, 'childId': 7},
                {'parentId': 1, 'childId': 8},
                {'parentId': 1, 'childId': 9},
                {'parentId': 9, 'childId': 10},
                {'parentId': 1, 'childId': 11},
                {'parentId': 1, 'childId': 12},
                {'parentId': 12, 'childId': 13},
                {'parentId': 1, 'childId': 14},
                {'parentId': 14, 'childId': 15},
                {'parentId': 1, 'childId': 16},
                {'parentId': 16, 'childId': 17},
                {'parentId': 1, 'childId': 18},
                {'parentId': 18, 'childId': 19},
                {'parentId': 1, 'childId': 20},
                {'parentId': 20, 'childId': 21},
                {'parentId': 20, 'childId': 22},
                {'parentId': 1, 'childId': 23},
                {'parentId': 1, 'childId': 24},
                {'parentId': 1, 'childId': 25},
                {'parentId': 1, 'childId': 26},
                {'parentId': 26, 'childId': 27},
                {'parentId': 1, 'childId': 28},
                {'parentId': 1, 'childId': 29},
                {'parentId': 1, 'childId': 30},
                {'parentId': 1, 'childId': 31},
                {'parentId': 31, 'childId': 32},
                {'parentId': 1, 'childId': 33},
                {'parentId': 33, 'childId': 34},
                {'parentId': 1, 'childId': 35},
                {'parentId': 35, 'childId': 36},
                {'parentId': 1, 'childId': 37},
                {'parentId': 37, 'childId': 38},
                {'parentId': 1, 'childId': 39},
                {'parentId': 39, 'childId': 40},
                {'parentId': 1, 'childId': 41},
                {'parentId': 41, 'childId': 42},
                {'parentId': 41, 'childId': 43},
                {'parentId': 1, 'childId': 44},
                {'parentId': 1, 'childId': 45},
                {'parentId': 1, 'childId': 46},
                {'parentId': 1, 'childId': 47},
                {'parentId': 47, 'childId': 48},
                {'parentId': 1, 'childId': 49},
                {'parentId': 1, 'childId': 50},
                {'parentId': 1, 'childId': 51},
                {'parentId': 1, 'childId': 52},
                {'parentId': 52, 'childId': 53},
                {'parentId': 1, 'childId': 54}
            ]
        }
        PATH_TO_MOCK_DATA = 'coeus/articles/apple'
        PATH_TO_TOPIC = 'topic.txt'
        PATH_TO_TEXT = 'text.txt'
        cwd = os.getcwd()
        user_path = cwd.split('coeus')[0]
        topic_path = os.path.join(user_path, PATH_TO_MOCK_DATA, PATH_TO_TOPIC)
        text_path = os.path.join(user_path, PATH_TO_MOCK_DATA, PATH_TO_TEXT)
        topic_file = open(topic_path, 'r')
        text_file = open(text_path, 'r')
        actual_result = Client.generate_mind_map_from_unstructured_text(
            topic_file.read(), text_file.read())
        text_file.close()
        topic_file.close()
        expected_string = str(expected_result_output)
        actual_string = str(actual_result)
        self.assertEqual(
            expected_string,
            actual_string,
            'unstructured :apple final output is not same as expected')


if __name__ == '__main__':
    unittest.main()
