from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#downloads the webpage and closes it. saves it as page_html
my_url = "https://www.ucalgary.ca/pubs/calendar/current/computer-science.html"
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
for course in course_codes:
    course_count += 1
    course = str(course)
    print("CPSC",course[-7:-4])

#grabs all prerequistes
all_prerequisites = page_soup.findAll("td", {"class":"myCell"})

#prints out the prerequisites on a seperate line
prerequisite_count = 0
for course in range(len(all_prerequisites)):
    prerequisite_count += 1
    prerequisites = all_prerequisites[course].find('span',{'class':'course-prereq'})
    for m in (prerequisites.contents):
        print(m.string, end = "")
    print()


