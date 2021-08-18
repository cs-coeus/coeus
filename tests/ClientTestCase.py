import unittest
from Client import Client
from repos.mocks.MockWikiRepo import MockWikiRepo


class ClientTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.client = Client()
        Client.wiki_repo = MockWikiRepo()

    def test_generate_mind_map_from_semi_structure_text(self):
        expected_result_output = {'nodes': [{'id': 1, 'text': "King Mongkut's University of Technology Thonburi"},
                                            {'id': 2, 'text': 'History'},
                                            {'id': 3, 'text': 'established february 1960 department vocational'},
                                            {'id': 4, 'text': 'Governance and organisation'},
                                            {'id': 5, 'text': 'regalia great crown victory sword'},
                                            {'id': 6, 'text': 'Faculties and Schools'},
                                            {'id': 7, 'text': 'School of Architecture and Design'},
                                            {'id': 8, 'text': 'school changed school architecture school'},
                                            {'id': 9, 'text': 'kmutt following faculties schools'},
                                            {'id': 10, 'text': 'KMUTT'}, {'id': 11, 'text': 'faculty engineering foe'},
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
                                            {'id': 36, 'text': 'Campuses'}, {'id': 37, 'text': 'Bangmod main campus'},
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
                                            {'id': 49, 'text': 'KMUTT'}, {'id': 50, 'text': 'KMUTT Library'},
                                            {'id': 51, 'text': 'october 2000 changed kmutt library'},
                                            {'id': 52, 'text': 'school seventh oldest university thailand'}],
                                  'edges': [{'parentId': 1, 'childId': 2}, {'parentId': 2, 'childId': 3},
                                            {'parentId': 1, 'childId': 4}, {'parentId': 4, 'childId': 5},
                                            {'parentId': 1, 'childId': 6}, {'parentId': 6, 'childId': 7},
                                            {'parentId': 7, 'childId': 8}, {'parentId': 6, 'childId': 9},
                                            {'parentId': 9, 'childId': 10}, {'parentId': 6, 'childId': 11},
                                            {'parentId': 6, 'childId': 12}, {'parentId': 12, 'childId': 13},
                                            {'parentId': 12, 'childId': 14}, {'parentId': 6, 'childId': 15},
                                            {'parentId': 6, 'childId': 16}, {'parentId': 6, 'childId': 17},
                                            {'parentId': 6, 'childId': 18}, {'parentId': 6, 'childId': 19},
                                            {'parentId': 6, 'childId': 20}, {'parentId': 20, 'childId': 21},
                                            {'parentId': 6, 'childId': 22}, {'parentId': 22, 'childId': 23},
                                            {'parentId': 22, 'childId': 24}, {'parentId': 6, 'childId': 25},
                                            {'parentId': 25, 'childId': 26}, {'parentId': 6, 'childId': 27},
                                            {'parentId': 6, 'childId': 28}, {'parentId': 28, 'childId': 29},
                                            {'parentId': 1, 'childId': 30}, {'parentId': 30, 'childId': 31},
                                            {'parentId': 30, 'childId': 32}, {'parentId': 32, 'childId': 33},
                                            {'parentId': 30, 'childId': 34}, {'parentId': 30, 'childId': 35},
                                            {'parentId': 1, 'childId': 36}, {'parentId': 36, 'childId': 37},
                                            {'parentId': 37, 'childId': 38}, {'parentId': 38, 'childId': 39},
                                            {'parentId': 36, 'childId': 40}, {'parentId': 40, 'childId': 41},
                                            {'parentId': 36, 'childId': 42}, {'parentId': 42, 'childId': 43},
                                            {'parentId': 43, 'childId': 44}, {'parentId': 36, 'childId': 45},
                                            {'parentId': 45, 'childId': 46}, {'parentId': 1, 'childId': 47},
                                            {'parentId': 47, 'childId': 48}, {'parentId': 48, 'childId': 49},
                                            {'parentId': 1, 'childId': 50}, {'parentId': 50, 'childId': 51},
                                            {'parentId': 1, 'childId': 52}]}
        actual_result = Client.generate_mind_map_from_semi_structure_text(
            """1""")
        expected_string = str(expected_result_output)
        actual_string = str(actual_result)
        self.assertEqual(expected_string, actual_string, 'structured: kmutt final output is not same as expected')

    def test_generate_mind_map_from_unstructured_text(self):
        expected_result_output = {'nodes': [
            {'id': 1, 'text': 'News - Apple helps Encircle expand its support for LGBTQ+ youth and their families'},
            {'id': 2, 'text': 'handful gay students high school'}, {'id': 3, 'text': 'micah really did save life'},
            {'id': 4, 'text': 'founded 2017 help young lgbtq'}, {'id': 5, 'text': 'Encircle'},
            {'id': 6, 'text': 'donations valued million help kickstart'},
            {'id': 7, 'text': 'handful gay students high school'}, {'id': 8, 'text': 'micah really did save life'},
            {'id': 9, 'text': 'founded 2017 help young lgbtq'}, {'id': 10, 'text': 'Encircle'},
            {'id': 11, 'text': 'donations valued million help kickstart'},
            {'id': 12, 'text': 'families number services including free'}, {'id': 13, 'text': 'Encircle'},
            {'id': 14, 'text': 'counselors school saving kids lives'}, {'id': 15, 'text': 'my school'},
            {'id': 16, 'text': 'micah toelupe'}, {'id': 17, 'text': 'Micah Toelupe'},
            {'id': 18, 'text': 'helped countless families utah chrisann'}, {'id': 19, 'text': 'Encircle'},
            {'id': 20, 'text': 'half lgbtq youth battling symptoms'}, {'id': 21, 'text': 'depression'},
            {'id': 22, 'text': 'Encircle'}, {'id': 23, 'text': 'understanding acceptance nonprofit prides communities'},
            {'id': 24, 'text': 'model worked 10 000 guests'},
            {'id': 25, 'text': 'daughter encircle khristian mission philippines'},
            {'id': 26, 'text': 'nonprofit helped foster deeper understanding'}, {'id': 27, 'text': 'Encircle'},
            {'id': 28, 'text': 'focus welcoming lifeline lgbtq youth'},
            {'id': 29, 'text': 'lovely chosen family savannah says'},
            {'id': 30, 'text': 'painting self portrait micah mom'},
            {'id': 31, 'text': 'micah encircle did blossomed micah'}, {'id': 32, 'text': 'Micah'},
            {'id': 33, 'text': 'encircle lgbtq youth family resource'}, {'id': 34, 'text': 'Encircle'},
            {'id': 35, 'text': 'counselors school saving kids lives'}, {'id': 36, 'text': 'my school'},
            {'id': 37, 'text': 'micah toelupe'}, {'id': 38, 'text': 'Micah Toelupe'},
            {'id': 39, 'text': 'helped countless families utah chrisann'}, {'id': 40, 'text': 'Encircle'},
            {'id': 41, 'text': 'half lgbtq youth battling symptoms'}, {'id': 42, 'text': 'depression'},
            {'id': 43, 'text': 'Encircle'}, {'id': 44, 'text': 'understanding acceptance nonprofit prides communities'},
            {'id': 45, 'text': 'model worked 10 000 guests'},
            {'id': 46, 'text': 'daughter encircle khristian mission philippines'},
            {'id': 47, 'text': 'nonprofit helped foster deeper understanding'}, {'id': 48, 'text': 'Encircle'},
            {'id': 49, 'text': 'focus welcoming lifeline lgbtq youth'},
            {'id': 50, 'text': 'lovely chosen family savannah says'},
            {'id': 51, 'text': 'painting self portrait micah mom'},
            {'id': 52, 'text': 'micah encircle did blossomed micah'}, {'id': 53, 'text': 'Micah'},
            {'id': 54, 'text': 'contribute visit encircle lgbtq youth'}],
                                  'edges': [{'parentId': 1, 'childId': 2}, {'parentId': 1, 'childId': 3},
                                            {'parentId': 1, 'childId': 4}, {'parentId': 4, 'childId': 5},
                                            {'parentId': 1, 'childId': 6}, {'parentId': 1, 'childId': 7},
                                            {'parentId': 1, 'childId': 8}, {'parentId': 1, 'childId': 9},
                                            {'parentId': 9, 'childId': 10}, {'parentId': 1, 'childId': 11},
                                            {'parentId': 1, 'childId': 12}, {'parentId': 12, 'childId': 13},
                                            {'parentId': 1, 'childId': 14}, {'parentId': 14, 'childId': 15},
                                            {'parentId': 1, 'childId': 16}, {'parentId': 16, 'childId': 17},
                                            {'parentId': 1, 'childId': 18}, {'parentId': 18, 'childId': 19},
                                            {'parentId': 1, 'childId': 20}, {'parentId': 20, 'childId': 21},
                                            {'parentId': 20, 'childId': 22}, {'parentId': 1, 'childId': 23},
                                            {'parentId': 1, 'childId': 24}, {'parentId': 1, 'childId': 25},
                                            {'parentId': 1, 'childId': 26}, {'parentId': 26, 'childId': 27},
                                            {'parentId': 1, 'childId': 28}, {'parentId': 1, 'childId': 29},
                                            {'parentId': 1, 'childId': 30}, {'parentId': 1, 'childId': 31},
                                            {'parentId': 31, 'childId': 32}, {'parentId': 1, 'childId': 33},
                                            {'parentId': 33, 'childId': 34}, {'parentId': 1, 'childId': 35},
                                            {'parentId': 35, 'childId': 36}, {'parentId': 1, 'childId': 37},
                                            {'parentId': 37, 'childId': 38}, {'parentId': 1, 'childId': 39},
                                            {'parentId': 39, 'childId': 40}, {'parentId': 1, 'childId': 41},
                                            {'parentId': 41, 'childId': 42}, {'parentId': 41, 'childId': 43},
                                            {'parentId': 1, 'childId': 44}, {'parentId': 1, 'childId': 45},
                                            {'parentId': 1, 'childId': 46}, {'parentId': 1, 'childId': 47},
                                            {'parentId': 47, 'childId': 48}, {'parentId': 1, 'childId': 49},
                                            {'parentId': 1, 'childId': 50}, {'parentId': 1, 'childId': 51},
                                            {'parentId': 1, 'childId': 52}, {'parentId': 52, 'childId': 53},
                                            {'parentId': 1, 'childId': 54}]}

        actual_result = Client.generate_mind_map_from_unstructured_text(
            'News - Apple helps Encircle expand its support for LGBTQ+ youth and their families', """In the summer of 2017, the Toelupe family heard about a little blue house in Provo, Utah, called Encircle. The nonprofit had a simple message, “No sides, only love” — and in the years to come, Encircle would prove to be part second home, part sanctuary, and the entry point to a community Micah Toelupe credits with saving his life.
As one of only a handful of gay students at his high school in rural Utah, Micah was struggling with depression, anxiety, and social isolation. That’s why stepping through the front doors of Encircle — where he felt like “one of a billion” instead of one of a few — felt so different.
“The effect it had here is so insane,” says Micah. “It really did save my life. You could walk right into the house and be surrounded by people who are going to love and respect who you are. It was always there, and you were always welcome.”
Encircle, a Utah-based nonprofit, was founded in 2017 to help young LGBTQ+ people and their families find support and a sense of belonging at community resource houses across the state. This month, the nonprofit launched a new campaign that leaders in business, music, and technology are rallying behind, with new donations from Apple, Qualtrics founder Ryan Smith and his wife, Ashley — who also own the Utah Jazz — and Imagine Dragons’s lead singer Dan Reynolds and his wife, musician Aja Volkman.
The donations — valued at $4 million — will help kickstart Encircle’s national expansion, with new community resource houses in Utah, Idaho, Nevada, and Arizona. In addition to a $1 million contribution, Apple will be donating iPads and other products to help expand Encircle’s virtual programming and inspire new pathways for digital connection, creativity, and education.

Encircle helps young people and their familiesIn the summer of 2017, the Toelupe family heard about a little blue house in Provo, Utah, called Encircle. The nonprofit had a simple message, “No sides, only love” — and in the years to come, Encircle would prove to be part second home, part sanctuary, and the entry point to a community Micah Toelupe credits with saving his life.
As one of only a handful of gay students at his high school in rural Utah, Micah was struggling with depression, anxiety, and social isolation. That’s why stepping through the front doors of Encircle — where he felt like “one of a billion” instead of one of a few — felt so different.
“The effect it had here is so insane,” says Micah. “It really did save my life. You could walk right into the house and be surrounded by people who are going to love and respect who you are. It was always there, and you were always welcome.”
Encircle, a Utah-based nonprofit, was founded in 2017 to help young LGBTQ+ people and their families find support and a sense of belonging at community resource houses across the state. This month, the nonprofit launched a new campaign that leaders in business, music, and technology are rallying behind, with new donations from Apple, Qualtrics founder Ryan Smith and his wife, Ashley — who also own the Utah Jazz — and Imagine Dragons’s lead singer Dan Reynolds and his wife, musician Aja Volkman.
The donations — valued at $4 million — will help kickstart Encircle’s national expansion, with new community resource houses in Utah, Idaho, Nevada, and Arizona. In addition to a $1 million contribution, Apple will be donating iPads and other products to help expand Encircle’s virtual programming and inspire new pathways for digital connection, creativity, and education.

Encircle helps young people and their families through a number of services, including free and subsidized therapy sessions, Friendship Circles that create safe spaces and foster community, and an open door policy that helps everyone who walks through their doors feel welcomed and accepted.
The pandemic has meant moving many of those services online, but it hasn’t dulled the urgency or importance of support systems that help young people who are cut off from their friends, often feeling more isolated than ever. The technology donations will make a meaningful difference in the nonprofit’s ability to reach LGBTQ+ youth where they are, helping create community beyond the four walls of an Encircle home.
I started going and it saved my life, and then my counselors at my school found out about it. It was saving other kids’ lives.
Micah Toelupe
Encircle has already helped countless families across Utah. Chrisann and Packard Toelupe have two LGBTQ-identified children — their son Micah and their daughter, Khristian. When Khristian shared her gender identity with her parents, Encircle helped the Toelupes find supportive resources and connect with other families looking to build community.
“Encircle gave me the confidence to be an advocate for my child, because I saw so many other parents being advocates for their children,” says Chrisann. “It was very lonely at first. But here was this whole network of people that I could call. You meet these other families, and you realize you’re not alone.”
Encircle is helping to meet an urgent need. More than half of LGBTQ youth are battling symptoms of depression, and four out of 10 LGBTQ+ people report having seriously considered suicide in the past 12 months. Still, nearly half of LGBTQ+ young people say they’ve been unable to access mental health counseling over the last year.
Encircle has taken on a supportive role not just for young people, but for their families — making space for love, understanding, and acceptance. The nonprofit prides itself on being a part of the communities it serves, even and especially in areas where LGBTQ+ youth feel uncomfortable or afraid to share their full selves.

By any measure, Encircle’s model has worked — more than 10,000 guests visit each Encircle home every year. With counseling services, music nights, community service projects, and other bonding activities, Encircle has been a crucial lifeline to young people facing isolation or depression.
Luckily for the Toelupes, Encircle opened a house in Provo in 2017, just 20 minutes from their home. And while there were some local resources for young LGBTQ+ people, few had such a profound impact on their family and neighbors across Utah County.
When the Toelupes first told their daughter about Encircle, Khristian was on her mission in the Philippines. When she returned home, she found a support system unlike anything she could’ve imagined — and a community that accepted and supported her for who she is.
“I was just bawling,” Khristian says. “I thought, ‘Wow, I didn’t think that I could feel all this love at once.’ Every time that I go to Encircle it’s time that I can actually breathe. I can just be — without having to worry about opinions or my own safety.”
Encircle’s mission is not only to serve families but also be a great neighbor and community member. The nonprofit has helped foster a deeper understanding and appreciation for a diversity of experiences and identities. According to Micah, it isn’t uncommon for students to drive hours at a time just to spend a little while at an Encircle house.
“Encircle had this snowball effect,” Micah says. “I started going and it saved my life, and then my counselors at my school found out about it. It was saving other kids’ lives. The Friendship Circles grew from two people in the first group to 20 kids in the room.”
Not everyone who visits has the support of their family, but Encircle’s focus on welcoming everyone has made it a lifeline for LGBTQ+ youth with a range of experiences. Savannah Harman interned at Encircle’s Salt Lake City house, where Friendship Circles and other community-building activities helped her find supportive friends from all walks of life.
“I found a lovely chosen family,” Savannah says. “Because Encircle is family oriented, it allows space for you even if you don’t bring your family. You will find your family there.”

For Micah, Encircle helped him gain the confidence and skills to grow as an artist, with classes and exhibitions that helped him share his work with the world. One of those pieces — a watercolor painting — is something of a self-portrait. Micah’s mom was an enthusiastic first customer, and the piece, which Micah never named, now hangs in the Toelupes’ living room.
“Every time I walk past it, I just think, ‘Becoming,’” Chrisann says. “Because it’s like Micah becoming himself. And that’s what Encircle, to me, did for him. He blossomed into Micah — his authentic self.”

To learn more about Encircle or find out how to contribute, visit Encircle | An LGBTQ+ Youth & Family Resource . through a number of services, including free and subsidized therapy sessions, Friendship Circles that create safe spaces and foster community, and an open door policy that helps everyone who walks through their doors feel welcomed and accepted.
The pandemic has meant moving many of those services online, but it hasn’t dulled the urgency or importance of support systems that help young people who are cut off from their friends, often feeling more isolated than ever. The technology donations will make a meaningful difference in the nonprofit’s ability to reach LGBTQ+ youth where they are, helping create community beyond the four walls of an Encircle home.
I started going and it saved my life, and then my counselors at my school found out about it. It was saving other kids’ lives.
Micah Toelupe
Encircle has already helped countless families across Utah. Chrisann and Packard Toelupe have two LGBTQ-identified children — their son Micah and their daughter, Khristian. When Khristian shared her gender identity with her parents, Encircle helped the Toelupes find supportive resources and connect with other families looking to build community.
“Encircle gave me the confidence to be an advocate for my child, because I saw so many other parents being advocates for their children,” says Chrisann. “It was very lonely at first. But here was this whole network of people that I could call. You meet these other families, and you realize you’re not alone.”
Encircle is helping to meet an urgent need. More than half of LGBTQ youth are battling symptoms of depression, and four out of 10 LGBTQ+ people report having seriously considered suicide in the past 12 months. Still, nearly half of LGBTQ+ young people say they’ve been unable to access mental health counseling over the last year.
Encircle has taken on a supportive role not just for young people, but for their families — making space for love, understanding, and acceptance. The nonprofit prides itself on being a part of the communities it serves, even and especially in areas where LGBTQ+ youth feel uncomfortable or afraid to share their full selves.

By any measure, Encircle’s model has worked — more than 10,000 guests visit each Encircle home every year. With counseling services, music nights, community service projects, and other bonding activities, Encircle has been a crucial lifeline to young people facing isolation or depression.
Luckily for the Toelupes, Encircle opened a house in Provo in 2017, just 20 minutes from their home. And while there were some local resources for young LGBTQ+ people, few had such a profound impact on their family and neighbors across Utah County.
When the Toelupes first told their daughter about Encircle, Khristian was on her mission in the Philippines. When she returned home, she found a support system unlike anything she could’ve imagined — and a community that accepted and supported her for who she is.
“I was just bawling,” Khristian says. “I thought, ‘Wow, I didn’t think that I could feel all this love at once.’ Every time that I go to Encircle it’s time that I can actually breathe. I can just be — without having to worry about opinions or my own safety.”
Encircle’s mission is not only to serve families but also be a great neighbor and community member. The nonprofit has helped foster a deeper understanding and appreciation for a diversity of experiences and identities. According to Micah, it isn’t uncommon for students to drive hours at a time just to spend a little while at an Encircle house.
“Encircle had this snowball effect,” Micah says. “I started going and it saved my life, and then my counselors at my school found out about it. It was saving other kids’ lives. The Friendship Circles grew from two people in the first group to 20 kids in the room.”
Not everyone who visits has the support of their family, but Encircle’s focus on welcoming everyone has made it a lifeline for LGBTQ+ youth with a range of experiences. Savannah Harman interned at Encircle’s Salt Lake City house, where Friendship Circles and other community-building activities helped her find supportive friends from all walks of life.
“I found a lovely chosen family,” Savannah says. “Because Encircle is family oriented, it allows space for you even if you don’t bring your family. You will find your family there.”

For Micah, Encircle helped him gain the confidence and skills to grow as an artist, with classes and exhibitions that helped him share his work with the world. One of those pieces — a watercolor painting — is something of a self-portrait. Micah’s mom was an enthusiastic first customer, and the piece, which Micah never named, now hangs in the Toelupes’ living room.
“Every time I walk past it, I just think, ‘Becoming,’” Chrisann says. “Because it’s like Micah becoming himself. And that’s what Encircle, to me, did for him. He blossomed into Micah — his authentic self.”

To learn more about Encircle or find out how to contribute, visit Encircle | An LGBTQ+ Youth & Family Resource .""")
        expected_string = str(expected_result_output)
        actual_string = str(actual_result)
        self.assertEqual(expected_string, actual_string, 'unstructured :apple final output is not same as expected')


if __name__ == '__main__':
    unittest.main()
