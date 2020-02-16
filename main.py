import csv

courses = {}

with open('courses.csv', newline='') as file:
	coursesInFile = csv.DictReader(file, delimiter=',')
	
	for course in coursesInFile:
		courses[course['course_code']] = course


result = []

def getPrerequisitesDeep(selectedCourse, courses):
	selectedCourse = courses[selectedCourse]

	if('prerequisites' not in selectedCourse.keys() or selectedCourse['prerequisites']  == ''):
		return

	choices = selectedCourse['prerequisites'].split('|')

	# If there's only one choice, automatically select that one.
	if len(choices) > 1:
		print(choices)
		choice = input('Select a choice (starting at 0 from left to right):')
	else:
		choice = 0

	choice = choices[int(choice)]

	prerequisites = choice.split(';')

	for prerequisite in prerequisites:
		global result
		result.append(prerequisite)
		
		if(prerequisite in courses):
			getPrerequisitesDeep(prerequisite, courses)


selectedCourse = input('select a course:')

getPrerequisitesDeep(selectedCourse, courses)

print(result)
