from repos.DataRepository import DataRepository
import requests
from typing import Any, List


class MockWikiRepo(DataRepository):
    def __init__(self):
        MockWikiRepo.mock_data = """= King Mongkut's University of Technology Thonburi =
King Mongkut's University of Technology Thonburi (KMUTT, Thai: มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี; RTGS: maha witthayalai theknoloyi phrachomklao thonburi ) or colloquially "Bangmod" (Thai: บางมด; RTGS: bang mot ) is an engineering and technology university in Thailand, focusing on teaching and research. It is one of nine national research universities (NRU) in Thailand. It is in Bang Mot Sub-district, Thung Khru District, Bangkok. It was founded on 18 April 1960, making it the third oldest engineering school and seventh oldest university in Thailand.


== History ==
King Mongkut's University of Technology Thonburi can trace its origin to the Thonburi Technical College (TTC) which was established on 4 February 1960, by the Department of Vocational Education, Ministry of Education. TTC had the mission of training technicians, technical instructors, and technologists. By virtue of the Technology Act, enacted 21 April 1971, three technical institutes are under the Department of Vocational Education: Thonburi Technical Institute (TTI), North Bangkok Technical Institute, and Nonthaburi Telecommunication Institute. They were combined to form one degree-granting institution under the name King Mongkut's Institute of Technology (KMIT) spread across three campuses. TTC thus became KMIT Thonburi campus. In 1974, KMIT was transferred from the Ministry of Education to the Ministry of University Affairs.A new technology act was enacted 19 February 1986: the three campuses of KMIT became three autonomous institutes, each having university status. KMIT Thonburi campus became King Mongkut's Institute of Technology Thonburi (KMITT).
KMITT purchased 460 acres (1.9 km2) of land to expand the campus.


== Governance and organisation ==

The university's formal seal is the personal seal of Phra Bat Somdet Phra Poramenthra Maha Mongkut Phra Chom Klao Chao Yu Hua, or Rama IV, also known as King Mongkut. In the middle of the seal is a Pra Maha Mongkut or Great Crown of Victory, the most important of the five regalia: the great crown of victory; the sword of victory; the royal staff; the royal slippers; and the royal fan and royal fly whisk) It has a white tiered umbrella of kingship bracing both sides. All of the symbols are displayed in a two-layered circle with text both in Thai and English showing the name of the university. This seal is used for announcements and official documents and is included in all of the ceremonies of the university.The flower of King Mongkut's University of Technology Thonburi is "Thammaruksa", a flower that can easily be found on campus. The university color imitates that of the flower.


== Faculties and Schools ==
KMUTT has the following Faculties and Schools:
Faculty of Engineering (FoE)
Faculty of Science (FSci)
Faculty of Industrial Education and Technology (FIET)
School of Liberal Arts (SoLA)
School of Information Technology (SIT)
School of Architecture and Design (SoA+D)
School of Energy Environment and Materials (SEEM)
School of Bioresources and Technology (SBT)
Join Graduate School of Energy and Environment (JGSEE)
Institute of Field Robotics (FIBO)
Graduate School of Management and Innovation (GMI)
College of Multidisciplinary Sciences


=== School of Architecture and Design ===
The KMUTT's School of Architecture and Design was established in 1995, to provide for architectural study in the English language. The current bachelor's degree programs are architecture, interior architecture, and industrial design. Communications design was added in 2003.  The school focuses on research and development of applied technology in art and design disciplines. In 2002, the school's name was changed from the "School of Architecture" to "School of Architecture and Design" (SoA+D).


== Student life ==
The sports complex includes, among other facilities, a gymnasium, a basketball court, a football field, a table tennis facility and a tennis court.
Library of King Mongkut's University of Technology Thonburi is the management Central Office library, and information technology to support the mission of the university to provide education, promote research, development, technical education and service to the society.
KMUTT residence is an independent, non-profit organization in cooperation with the University administration.
There are student activities and sports services, sports equipment borrowing services such as football, volleyball etc., outdoor sports fields and indoor sports field.


== Campuses ==


=== Bangmod main campus ===
Bang Mot is the main campus of KMUTT, in Thonburi on Prachauthit Road. The area of the main campus is 52 acres (0.21 km2). The Faculty of Engineering; Faculty of Science; Faculty of Industrial Education and Technology; School of Energy, Environmental and Materials; the School of Information Technology; the School of Liberal Arts; the Joint Graduate School of Energy and Environment; Graduate School of Management and Innovation; Institute of Field Robotics; Institute for Scientific and Technological Research and Services; Computer Center; and KMUTT Library are all present on this campus.


=== Bang Khun Thian Campus ===
The Bang Khun Thian Campus, 80 acres (0.32 km2) in size, contains the School of Architecture and Design, the School of Bioresources and Technology, the Pilot Plant Development and Training Institute, and the Industrial Park. It is in Bangkok's Bang Khun Thian District.


=== Ratchaburi Campus ===
The Ratchaburi campus is located in Ratchaburi province, 150 kilometers to the west of the main Bangmod campus in Bangkok. A 500 million baht budget was allocated for construction in 2010.


=== Main campus dormitories ===
In the fiscal year 1995–1997, the government granted a budget of 190.8 million baht to King Mongkut's University of Technology Thonburi to construct the dormitory. The male dormitory, completed for 130.7 million baht, was a 23 m (75 ft) x  69 m (226 ft) eleven-story building, composed of 264 rooms that accommodate 944 students. The female dormitory, completed at the amount of 60.1 million baht, was a 23 m (75 ft) x 35.7 m (117 ft) ten-story building, composed of 110 rooms that accommodate 388 students.


== Transportation ==
KMUTT provides a free bus service between the Bangmod campus and the Bang Khun Thian campus for students, staff, and visitors. The first trip from the Bangmod campus to the Bang Khun Thian campus is at 7:30 A.M. and the last trip is at 6:00 P.M. The first trip in the opposite direction from the Bang Khun Thian campus to the Bangmod campus starts at 8:00 A.M. and the last trip is at 7:00 P.M.


== KMUTT Library ==
The "KMUTT Library and Information Center" was founded on 5 May 1988. On 19 October 2000 its name was changed to "KMUTT Library".


== References =="""

    @staticmethod
    def getData(input: str) -> str:
        return MockWikiRepo.mock_data
