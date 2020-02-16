from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

#downloads the webpage and closes it. saves it as page_html
my_url = "https://www.ucalgary.ca/pubs/calendar/current/architectural-studies.html"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each course
containers = page_soup.findAll("div",{"class":"item-container"})
course_codes = containers[0].findAll("a",{"class":"link-text"})

#Prints out the courses on a seperate line
course_count = 0

courses = {}

for course in course_codes:
    course_count += 1
    course = str(course)

    courses[course_count-1] = dict()
    courses[course_count-1]['course_name'] = "Architectural Studies " + course[-7:-4]
    courses[course_count-1]['course_code'] = "ARST " + course[-7:-4]

#grabs all prerequistes
all_prerequisites = page_soup.findAll("td", {"class":"myCell"})

#prints out the prerequisites on a seperate line
prerequisite_count = 0
for course in range(len(all_prerequisites)):
    prerequisite_count += 1
    prerequisites = all_prerequisites[course].find('span',{'class':'course-prereq'})
    prerequisite = ''
    for m in (prerequisites.contents):
        # print(m.string, end = "")
        prerequisite += m.string
    print(prerequisite)
    try: 
        courses[prerequisite_count-1]['prerequisites'] = prerequisite
    except:
        continue
    print()

with open('courses.csv', 'w', newline='') as file:
	fields = ['course_name','course_code', 'prerequisites']
	writer = csv.DictWriter(file, delimiter=',', fieldnames=fields)

	writer.writeheader()

	for courseCode, course in courses.items():
		writer.writerow(course)


