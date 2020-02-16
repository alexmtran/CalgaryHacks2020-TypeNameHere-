import csv
from anytree.importer import DictImporter
from anytree.dotexport import RenderTreeGraph
from anytree import RenderTree

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

		tree.append({
			prerequisite: prerequisite,
			'name': prerequisite,
			'children': []
		})

		if(prerequisite in courses):
			print(prerequisite)

			print('the tree at:' + str(index))
			print(tree[index])

			getPrerequisitesDeep(prerequisite, courses, tree[index]['children'])

def getPrerequisites(selectedCourse, courses):
	prerequisites = {
		selectedCourse: selectedCourse,
		'name': selectedCourse,
		'children': []
	}

	getPrerequisitesDeep(selectedCourse, courses, prerequisites['children'])

	return prerequisites

selectedCourse = input('select a course:')

prerequisitesTree = getPrerequisites(selectedCourse, courses)
print(prerequisitesTree)

importer = DictImporter()
root = importer.import_(prerequisitesTree)
print(RenderTree(root))

RenderTreeGraph(root).to_picture("tree.png")
