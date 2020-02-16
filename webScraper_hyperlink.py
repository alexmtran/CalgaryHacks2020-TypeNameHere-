from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

#downloads the webpage and closes it. saves it as page_html
my_url = "https://www.ucalgary.ca/pubs/calendar/current/course-desc-main.html"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"item-container"})
course_codes = containers[0].findAll("a",{"class":"link-text"})

my_dict = {}
for course in course_codes:
    course.string = course.string.rstrip(" ")
    course.string = course.string.lstrip(" ")
    if "," in course.string:
        continue
    if (len(course.string) > 1):
        
        my_dict[course.string[0:course.string.rindex(' ')]] = [course.string[course.string.rindex(' ')+1:], course['href']]

del my_dict['Course']

print(my_dict)




        



#Looking for hyperlink



        
