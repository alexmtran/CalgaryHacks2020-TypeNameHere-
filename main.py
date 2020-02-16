import csv
from anytree.importer import DictImporter
from anytree.dotexport import RenderTreeGraph
from anytree import RenderTree

courses = {}

def displayChoices(choices):
	for index, choice in enumerate(choices):
		print(f'{index+1}. {choice.strip()}')


def getPrerequisitesDeep(selectedCourse, courses, tree):
	selectedCourse = courses[selectedCourse]

	if('prerequisites' not in selectedCourse.keys() or selectedCourse['prerequisites']  == ''):
		return selectedCourse['course_code']

	choices = selectedCourse['prerequisites'].split('|')

	# If there's only one choice, automatically select that one.
	name = ''
	try:
		name = selectedCourse['course_name']
	except:
		name = selectedCourse['course_code']
	print('Prerequisites for: ' + name)

	displayChoices(choices)

	if len(choices) > 1:
		choiceIndex = int(input('Select a course that you\'re gonna/you have finished:'))
		choiceIndex -= 1

		numberOfOptions = len(choices)

		while choiceIndex > numberOfOptions - 1 or choiceIndex < 0:
			choiceIndex = int(input('Invalid option. Select a course that you\'re gonna/you have finished:'))
			choiceIndex -= 1
	else:
		choiceIndex = 0

	choice = choices[choiceIndex].strip()
	prerequisites = choice.split(';')

	for index, prerequisite in enumerate(prerequisites):

		tree.append({
			prerequisite: prerequisite,
			'name': prerequisite,
			'children': []
		})

		if(prerequisite in courses):
			getPrerequisitesDeep(prerequisite, courses, tree[index]['children'])

def getPrerequisites(selectedCourse, courses):
	prerequisites = {
		selectedCourse: selectedCourse,
		'name': selectedCourse,
		'children': []
	}

	getPrerequisitesDeep(selectedCourse, courses, prerequisites['children'])

	return prerequisites

with open('courses.csv', newline='') as file:
	coursesInFile = csv.DictReader(file, delimiter=',')
	
	for course in coursesInFile:
		courses[course['course_code']] = course


selectedCourse = ''

print('--------------Welcome to the UCalgary Prerequisites Wizard!-----------')
selectedCourse = input('Select a UCalgary course you want to generate a prerequisites-tree from:')

prerequisitesTree = getPrerequisites(selectedCourse, courses)

importer = DictImporter()
root = importer.import_(prerequisitesTree)

RenderTreeGraph(root).to_picture("tree.png")
print('`tree.png` has been generated.')

while selectedCourse in courses:
	selectedCourse = input('Select a UCalgary course you want to generate a prerequisites-tree from:')
	prerequisitesTree = getPrerequisites(selectedCourse, courses)

	importer = DictImporter()
	root = importer.import_(prerequisitesTree)

	RenderTreeGraph(root).to_picture("tree.png")
	print('`tree.png` has been generated.')
