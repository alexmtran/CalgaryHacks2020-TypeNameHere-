import csv

courses = {}

with open('courses.csv', newline='') as file:
	coursesInFile = csv.DictReader(file, delimiter=',')
	
	for course in coursesInFile:
		courses[course['course_code']] = course

def getPrerequisitesDeep(selectedCourse, courses, tree):
	selectedCourse = courses[selectedCourse]

	if('prerequisites' not in selectedCourse.keys() or selectedCourse['prerequisites']  == ''):
		return selectedCourse['course_code']

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
		tree[prerequisite] = dict()
		
		if(prerequisite in courses):
			getPrerequisitesDeep(prerequisite, courses, tree[prerequisite])

def getPrerequisites(selectedCourse, courses):
	prerequisites = {
		selectedCourse: dict()
	}

	getPrerequisitesDeep(selectedCourse, courses, prerequisites[selectedCourse])

	return prerequisites

selectedCourse = input('select a course:')

prerequisitesTree = getPrerequisites(selectedCourse, courses)
print(prerequisitesTree)
