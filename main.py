from Client import Client
from datetime import datetime

from repositories.WikipediaRepository import WikipediaRepository
from utils.InputPreparator import InputPreparator

test_text = """King Mongkut's University of Technology Thonburi can trace its origin to the Thonburi Technical College (TTC) which was established on 4 February 1960, by the Department of Vocational Education, Ministry of Education. TTC had the mission of training technicians, technical instructors, and technologists. By virtue of the Technology Act, enacted 21 April 1971, three technical institutes are under the Department of Vocational Education: Thonburi Technical Institute (TTI), North Bangkok Technical Institute, and Nonthaburi Telecommunication Institute. They were combined to form one degree-granting institution under the name King Mongkut's Institute of Technology (KMIT) spread across three campuses. TTC thus became KMIT Thonburi campus. In 1974, KMIT was transferred from the Ministry of Education to the Ministry of University Affairs.A new technology act was enacted 19 February 1986: the three campuses of KMIT became three autonomous institutes, each having university status. KMIT Thonburi campus became King Mongkut's Institute of Technology Thonburi (KMITT)."""
#
# test_text_qa = 'Apple is a fruit. Apple is red. Apple is delicious.'
# test_text_key = 'KMUTT is a university'
#
# input_p = InputPreparator()
# print(input_p.normalize_text_from_wikipedia("""= test1 = \n 123"""))
#
# summarizer_model = ModelSummarizer()
# print(summarizer_model.predict(test_text))
#
# qa_model = ModelQA()
# tuple_test = (test_text_qa, ('Apple', 0.6), ['What is '])
# print(tuple_test)
# print(qa_model.predict(tuple_test))
#
# keybert_model = ModelKeyBert()
# print(keybert_model.predict(test_text_key))
#
# sents = ['Obama speaks to the media in Illinois', 'The president greets the press in Chicago',
#          'Obama speaks to the media in Illinois', 'The president greets the press in Chicago',
#          'Obama speaks to the media in Illinois', 'The president greets the press in Chicago',
#          'Obama speaks to the media in Illinois', 'The president greets the press in Chicago',
#          'The president greets the press in Chicago', 'The president greets the press in Chicago',
#          'Oranges are my favorite fruit']
#
# clustering_model = ModelClustering()
# # data = [sent.text for sent in sents]
# data = sents
# X = np.arange(len(data)).reshape(-1, 1)
#
#
# def distance(x, y):
#     return ModelClustering.wmd.wmdistance(input_p.preprocess_senetence_to_arr(data[int(x[0])]),
#                                           input_p.preprocess_senetence_to_arr(data[int(y[0])]))
#
#
# proximity_matrix = pairwise_distances(X, X, metric=distance)
# best_k, best_cluster = clustering_model.predict((X, len(sents), proximity_matrix))
#
# print(best_k, best_cluster)
#
# spacy_model = ModelSpacy()
# print(list(spacy_model.predict(test_text).sents))
#
# print("""start""")
# wiki_repo = WikiRepository()
# print(
#     WikiRepository.getData("""King_Mongkut's_University_of_Technology_Thonburi"""))
# print("""end""")
client = Client()
present_date_with_time = datetime.now()
print(Client.generate_mind_map_from_semi_structure_text(
    """King_Mongkut's_University_of_Technology_Thonburi"""))
present_date_with_time_end = datetime.now()
print('total,', present_date_with_time_end - present_date_with_time)
#
# present_date_with_time = datetime.now()
# print(Client.generate_mind_map_from_unstructured_text('News - Apple helps Encircle expand its support for LGBTQ+ youth and their families',"""In the summer of 2017, the Toelupe family heard about a little blue house in Provo, Utah, called Encircle. The nonprofit had a simple message, “No sides, only love” — and in the years to come, Encircle would prove to be part second home, part sanctuary, and the entry point to a community Micah Toelupe credits with saving his life.
# As one of only a handful of gay students at his high school in rural Utah, Micah was struggling with depression, anxiety, and social isolation. That’s why stepping through the front doors of Encircle — where he felt like “one of a billion” instead of one of a few — felt so different.
# “The effect it had here is so insane,” says Micah. “It really did save my life. You could walk right into the house and be surrounded by people who are going to love and respect who you are. It was always there, and you were always welcome.”
# Encircle, a Utah-based nonprofit, was founded in 2017 to help young LGBTQ+ people and their families find support and a sense of belonging at community resource houses across the state. This month, the nonprofit launched a new campaign that leaders in business, music, and technology are rallying behind, with new donations from Apple, Qualtrics founder Ryan Smith and his wife, Ashley — who also own the Utah Jazz — and Imagine Dragons’s lead singer Dan Reynolds and his wife, musician Aja Volkman.
# The donations — valued at $4 million — will help kickstart Encircle’s national expansion, with new community resource houses in Utah, Idaho, Nevada, and Arizona. In addition to a $1 million contribution, Apple will be donating iPads and other products to help expand Encircle’s virtual programming and inspire new pathways for digital connection, creativity, and education.
#
# Encircle helps young people and their familiesIn the summer of 2017, the Toelupe family heard about a little blue house in Provo, Utah, called Encircle. The nonprofit had a simple message, “No sides, only love” — and in the years to come, Encircle would prove to be part second home, part sanctuary, and the entry point to a community Micah Toelupe credits with saving his life.
# As one of only a handful of gay students at his high school in rural Utah, Micah was struggling with depression, anxiety, and social isolation. That’s why stepping through the front doors of Encircle — where he felt like “one of a billion” instead of one of a few — felt so different.
# “The effect it had here is so insane,” says Micah. “It really did save my life. You could walk right into the house and be surrounded by people who are going to love and respect who you are. It was always there, and you were always welcome.”
# Encircle, a Utah-based nonprofit, was founded in 2017 to help young LGBTQ+ people and their families find support and a sense of belonging at community resource houses across the state. This month, the nonprofit launched a new campaign that leaders in business, music, and technology are rallying behind, with new donations from Apple, Qualtrics founder Ryan Smith and his wife, Ashley — who also own the Utah Jazz — and Imagine Dragons’s lead singer Dan Reynolds and his wife, musician Aja Volkman.
# The donations — valued at $4 million — will help kickstart Encircle’s national expansion, with new community resource houses in Utah, Idaho, Nevada, and Arizona. In addition to a $1 million contribution, Apple will be donating iPads and other products to help expand Encircle’s virtual programming and inspire new pathways for digital connection, creativity, and education.
#
# Encircle helps young people and their families through a number of services, including free and subsidized therapy sessions, Friendship Circles that create safe spaces and foster community, and an open door policy that helps everyone who walks through their doors feel welcomed and accepted.
# The pandemic has meant moving many of those services online, but it hasn’t dulled the urgency or importance of support systems that help young people who are cut off from their friends, often feeling more isolated than ever. The technology donations will make a meaningful difference in the nonprofit’s ability to reach LGBTQ+ youth where they are, helping create community beyond the four walls of an Encircle home.
# I started going and it saved my life, and then my counselors at my school found out about it. It was saving other kids’ lives.
# Micah Toelupe
# Encircle has already helped countless families across Utah. Chrisann and Packard Toelupe have two LGBTQ-identified children — their son Micah and their daughter, Khristian. When Khristian shared her gender identity with her parents, Encircle helped the Toelupes find supportive resources and connect with other families looking to build community.
# “Encircle gave me the confidence to be an advocate for my child, because I saw so many other parents being advocates for their children,” says Chrisann. “It was very lonely at first. But here was this whole network of people that I could call. You meet these other families, and you realize you’re not alone.”
# Encircle is helping to meet an urgent need. More than half of LGBTQ youth are battling symptoms of depression, and four out of 10 LGBTQ+ people report having seriously considered suicide in the past 12 months. Still, nearly half of LGBTQ+ young people say they’ve been unable to access mental health counseling over the last year.
# Encircle has taken on a supportive role not just for young people, but for their families — making space for love, understanding, and acceptance. The nonprofit prides itself on being a part of the communities it serves, even and especially in areas where LGBTQ+ youth feel uncomfortable or afraid to share their full selves.
#
# By any measure, Encircle’s model has worked — more than 10,000 guests visit each Encircle home every year. With counseling services, music nights, community service projects, and other bonding activities, Encircle has been a crucial lifeline to young people facing isolation or depression.
# Luckily for the Toelupes, Encircle opened a house in Provo in 2017, just 20 minutes from their home. And while there were some local resources for young LGBTQ+ people, few had such a profound impact on their family and neighbors across Utah County.
# When the Toelupes first told their daughter about Encircle, Khristian was on her mission in the Philippines. When she returned home, she found a support system unlike anything she could’ve imagined — and a community that accepted and supported her for who she is.
# “I was just bawling,” Khristian says. “I thought, ‘Wow, I didn’t think that I could feel all this love at once.’ Every time that I go to Encircle it’s time that I can actually breathe. I can just be — without having to worry about opinions or my own safety.”
# Encircle’s mission is not only to serve families but also be a great neighbor and community member. The nonprofit has helped foster a deeper understanding and appreciation for a diversity of experiences and identities. According to Micah, it isn’t uncommon for students to drive hours at a time just to spend a little while at an Encircle house.
# “Encircle had this snowball effect,” Micah says. “I started going and it saved my life, and then my counselors at my school found out about it. It was saving other kids’ lives. The Friendship Circles grew from two people in the first group to 20 kids in the room.”
# Not everyone who visits has the support of their family, but Encircle’s focus on welcoming everyone has made it a lifeline for LGBTQ+ youth with a range of experiences. Savannah Harman interned at Encircle’s Salt Lake City house, where Friendship Circles and other community-building activities helped her find supportive friends from all walks of life.
# “I found a lovely chosen family,” Savannah says. “Because Encircle is family oriented, it allows space for you even if you don’t bring your family. You will find your family there.”
#
# For Micah, Encircle helped him gain the confidence and skills to grow as an artist, with classes and exhibitions that helped him share his work with the world. One of those pieces — a watercolor painting — is something of a self-portrait. Micah’s mom was an enthusiastic first customer, and the piece, which Micah never named, now hangs in the Toelupes’ living room.
# “Every time I walk past it, I just think, ‘Becoming,’” Chrisann says. “Because it’s like Micah becoming himself. And that’s what Encircle, to me, did for him. He blossomed into Micah — his authentic self.”
#
# To learn more about Encircle or find out how to contribute, visit Encircle | An LGBTQ+ Youth & Family Resource . through a number of services, including free and subsidized therapy sessions, Friendship Circles that create safe spaces and foster community, and an open door policy that helps everyone who walks through their doors feel welcomed and accepted.
# The pandemic has meant moving many of those services online, but it hasn’t dulled the urgency or importance of support systems that help young people who are cut off from their friends, often feeling more isolated than ever. The technology donations will make a meaningful difference in the nonprofit’s ability to reach LGBTQ+ youth where they are, helping create community beyond the four walls of an Encircle home.
# I started going and it saved my life, and then my counselors at my school found out about it. It was saving other kids’ lives.
# Micah Toelupe
# Encircle has already helped countless families across Utah. Chrisann and Packard Toelupe have two LGBTQ-identified children — their son Micah and their daughter, Khristian. When Khristian shared her gender identity with her parents, Encircle helped the Toelupes find supportive resources and connect with other families looking to build community.
# “Encircle gave me the confidence to be an advocate for my child, because I saw so many other parents being advocates for their children,” says Chrisann. “It was very lonely at first. But here was this whole network of people that I could call. You meet these other families, and you realize you’re not alone.”
# Encircle is helping to meet an urgent need. More than half of LGBTQ youth are battling symptoms of depression, and four out of 10 LGBTQ+ people report having seriously considered suicide in the past 12 months. Still, nearly half of LGBTQ+ young people say they’ve been unable to access mental health counseling over the last year.
# Encircle has taken on a supportive role not just for young people, but for their families — making space for love, understanding, and acceptance. The nonprofit prides itself on being a part of the communities it serves, even and especially in areas where LGBTQ+ youth feel uncomfortable or afraid to share their full selves.
#
# By any measure, Encircle’s model has worked — more than 10,000 guests visit each Encircle home every year. With counseling services, music nights, community service projects, and other bonding activities, Encircle has been a crucial lifeline to young people facing isolation or depression.
# Luckily for the Toelupes, Encircle opened a house in Provo in 2017, just 20 minutes from their home. And while there were some local resources for young LGBTQ+ people, few had such a profound impact on their family and neighbors across Utah County.
# When the Toelupes first told their daughter about Encircle, Khristian was on her mission in the Philippines. When she returned home, she found a support system unlike anything she could’ve imagined — and a community that accepted and supported her for who she is.
# “I was just bawling,” Khristian says. “I thought, ‘Wow, I didn’t think that I could feel all this love at once.’ Every time that I go to Encircle it’s time that I can actually breathe. I can just be — without having to worry about opinions or my own safety.”
# Encircle’s mission is not only to serve families but also be a great neighbor and community member. The nonprofit has helped foster a deeper understanding and appreciation for a diversity of experiences and identities. According to Micah, it isn’t uncommon for students to drive hours at a time just to spend a little while at an Encircle house.
# “Encircle had this snowball effect,” Micah says. “I started going and it saved my life, and then my counselors at my school found out about it. It was saving other kids’ lives. The Friendship Circles grew from two people in the first group to 20 kids in the room.”
# Not everyone who visits has the support of their family, but Encircle’s focus on welcoming everyone has made it a lifeline for LGBTQ+ youth with a range of experiences. Savannah Harman interned at Encircle’s Salt Lake City house, where Friendship Circles and other community-building activities helped her find supportive friends from all walks of life.
# “I found a lovely chosen family,” Savannah says. “Because Encircle is family oriented, it allows space for you even if you don’t bring your family. You will find your family there.”
#
# For Micah, Encircle helped him gain the confidence and skills to grow as an artist, with classes and exhibitions that helped him share his work with the world. One of those pieces — a watercolor painting — is something of a self-portrait. Micah’s mom was an enthusiastic first customer, and the piece, which Micah never named, now hangs in the Toelupes’ living room.
# “Every time I walk past it, I just think, ‘Becoming,’” Chrisann says. “Because it’s like Micah becoming himself. And that’s what Encircle, to me, did for him. He blossomed into Micah — his authentic self.”
#
# To learn more about Encircle or find out how to contribute, visit Encircle | An LGBTQ+ Youth & Family Resource ."""))
# present_date_with_time_end = datetime.now()
# print('total,', present_date_with_time_end - present_date_with_time)

general_format = t = {"King Mongkut's University of Technology Thonburi": {
    '_paragraph': {'school seventh oldest university thailand': {}},
    'History': {'_paragraph': {'established february 1960 department vocational': {}}},
    'Governance and organisation': {'_paragraph': {'regalia great crown victory sword': {}}}, 'Faculties and Schools': {
        '_paragraph': {'kmutt following faculties schools': {'KMUTT': {}}, 'faculty engineering foe': {},
                       'science fsci': {'Faculty of Science': {}}, 'faculty industrial education technology fiet': {},
                       'school liberal arts sola': {}, 'school information technology sit': {},
                       'school architecture design soa': {}, 'school energy environment materials': {},
                       'school bioresources technology sbt': {'School of Bioresources and Technology': {}},
                       'graduate school energy environment jgsee': {
                           'Join Graduate School of Energy and Environment': {}, 'Join': {}},
                       'institute field robotics fibo': {'Institute of Field Robotics': {}},
                       'graduate school management innovation gmi': {},
                       'college multidisciplinary sciences': {'College of Multidisciplinary Sciences': {}}},
        'School of Architecture and Design': {'_paragraph': {'school changed school architecture school': {}}}},
    'Student life': {'_paragraph': {'sports complex includes facilities gymnasium': {},
                                    'support mission university provide education': {'information technology': {}},
                                    'kmutt residence independent non profit': {},
                                    'student activities sports services sports': {}}},
    'Campuses': {'Bangmod main campus': {'_paragraph': {'area main campus 52 acres': {'Bang Mot': {}}}},
                 'Bang Khun Thian Campus': {'_paragraph': {'khun thian campus 80 acres': {}}},
                 'Ratchaburi Campus': {'_paragraph': {'bangmod campus bangkok 500 million': {'Bangkok': {}}}},
                 'Main campus dormitories': {'_paragraph': {'dormitory completed 130 million baht': {}}}},
    'Transportation': {'_paragraph': {'free bus service bangmod campus': {'KMUTT': {}}}},
    'KMUTT Library': {'_paragraph': {'october 2000 changed kmutt library': {}}}}}

kmutt_intermediate_form = [{'id': 1, 'text': "King Mongkut's University of Technology Thonburi", 'parentId': -1},
                           {'id': 2, 'text': 'History', 'parentId': 1},
                           {'id': 3, 'text': 'established february 1960 department vocational', 'parentId': 2},
                           {'id': 4, 'text': 'Governance and organisation', 'parentId': 1},
                           {'id': 5, 'text': 'regalia great crown victory sword', 'parentId': 4},
                           {'id': 6, 'text': 'Faculties and Schools', 'parentId': 1},
                           {'id': 7, 'text': 'School of Architecture and Design', 'parentId': 6},
                           {'id': 8, 'text': 'school changed school architecture school', 'parentId': 7},
                           {'id': 9, 'text': 'kmutt following faculties schools', 'parentId': 6},
                           {'id': 10, 'text': 'KMUTT', 'parentId': 9},
                           {'id': 11, 'text': 'faculty engineering foe', 'parentId': 6},
                           {'id': 12, 'text': 'science fsci', 'parentId': 6},
                           {'id': 13, 'text': 'Faculty of Science', 'parentId': 12},
                           {'id': 14, 'text': 'Faculty of Science', 'parentId': 12},
                           {'id': 15, 'text': 'faculty industrial education technology fiet', 'parentId': 6},
                           {'id': 16, 'text': 'school liberal arts sola', 'parentId': 6},
                           {'id': 17, 'text': 'school information technology sit', 'parentId': 6},
                           {'id': 18, 'text': 'school architecture design soa', 'parentId': 6},
                           {'id': 19, 'text': 'school energy environment materials', 'parentId': 6},
                           {'id': 20, 'text': 'school bioresources technology sbt', 'parentId': 6},
                           {'id': 21, 'text': 'School of Bioresources and Technology', 'parentId': 20},
                           {'id': 22, 'text': 'graduate school energy environment jgsee', 'parentId': 6},
                           {'id': 23, 'text': 'Join Graduate School of Energy and Environment', 'parentId': 22},
                           {'id': 24, 'text': 'Join', 'parentId': 22},
                           {'id': 25, 'text': 'institute field robotics fibo', 'parentId': 6},
                           {'id': 26, 'text': 'Institute of Field Robotics', 'parentId': 25},
                           {'id': 27, 'text': 'graduate school management innovation gmi', 'parentId': 6},
                           {'id': 28, 'text': 'college multidisciplinary sciences', 'parentId': 6},
                           {'id': 29, 'text': 'College of Multidisciplinary Sciences', 'parentId': 28},
                           {'id': 30, 'text': 'Student life', 'parentId': 1},
                           {'id': 31, 'text': 'sports complex includes facilities gymnasium', 'parentId': 30},
                           {'id': 32, 'text': 'support mission university provide education', 'parentId': 30},
                           {'id': 33, 'text': 'information technology', 'parentId': 32},
                           {'id': 34, 'text': 'kmutt residence independent non profit', 'parentId': 30},
                           {'id': 35, 'text': 'student activities sports services sports', 'parentId': 30},
                           {'id': 36, 'text': 'Campuses', 'parentId': 1},
                           {'id': 37, 'text': 'Bangmod main campus', 'parentId': 36},
                           {'id': 38, 'text': 'area main campus 52 acres', 'parentId': 37},
                           {'id': 39, 'text': 'Bang Mot', 'parentId': 38},
                           {'id': 40, 'text': 'Bang Khun Thian Campus', 'parentId': 36},
                           {'id': 41, 'text': 'khun thian campus 80 acres', 'parentId': 40},
                           {'id': 42, 'text': 'Ratchaburi Campus', 'parentId': 36},
                           {'id': 43, 'text': 'bangmod campus bangkok 500 million', 'parentId': 42},
                           {'id': 44, 'text': 'Bangkok', 'parentId': 43},
                           {'id': 45, 'text': 'Main campus dormitories', 'parentId': 36},
                           {'id': 46, 'text': 'dormitory completed 130 million baht', 'parentId': 45},
                           {'id': 47, 'text': 'Transportation', 'parentId': 1},
                           {'id': 48, 'text': 'free bus service bangmod campus', 'parentId': 47},
                           {'id': 49, 'text': 'KMUTT', 'parentId': 48},
                           {'id': 50, 'text': 'KMUTT Library', 'parentId': 1},
                           {'id': 51, 'text': 'october 2000 changed kmutt library', 'parentId': 50},
                           {'id': 52, 'text': 'school seventh oldest university thailand', 'parentId': 1}]

# print(client.transform_mind_map_to_intermediate_json_data_structure(kmutt_dict))
#
# print(client.transform_intermediate_json_to_final(client.transform_mind_map_to_intermediate_json_data_structure(kmutt_dict)))
