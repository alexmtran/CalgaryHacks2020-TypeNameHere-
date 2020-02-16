import csv

courses = {}

with open('courses.csv', newline='') as file:
	coursesInFile = csv.DictReader(file, delimiter=',')
	
	for course in coursesInFile:
		courses[course['course_code']] = course

def getPrerequisitesDeep(selectedCourse, courses, tree):
	selectedCourse = courses[selectedCourse]

	if('prerequisites' not in selectedCourse.keys() or selectedCourse['prerequisites']  == ''):
		print(selectedCourse['course_code'])
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

	for index, prerequisite in enumerate(prerequisites):
		if(prerequisite in courses):
			tree.append({
				prerequisite: prerequisite,
				'children': []
			})

			print('the tree at:' + str(index-1))
			print(tree[index-1])

			getPrerequisitesDeep(prerequisite, courses, tree[index-1]['children'])

def getPrerequisites(selectedCourse, courses):
	prerequisites = {
		selectedCourse: selectedCourse,
		'children': []
	}

	getPrerequisitesDeep(selectedCourse, courses, prerequisites['children'])

	return prerequisites

selectedCourse = input('select a course:')

prerequisitesTree = getPrerequisites(selectedCourse, courses)
print(prerequisitesTree)
