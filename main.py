courses = {
	'CPSC 481' : {
		'course_name': 'Computer Science 481',
		'course_code': 'CPSC 481',
		'prerequisites': 'SENG 300|DATA 311'
	},
	'SENG 300' : {
		'course_name': 'Software Engineering 300',
		'course_code': 'CPSC 481',
		'prerequisites': 'CPSC 319|CPSC 331'
	},

	'CPSC 331' : {
		'course_name': 'Computer Science 331',
		'course_code': 'CPSC 331',
		'prerequisites': 'CPSC 233;MATH 271|CPSC 233;MATH 273|CPSC 219;MATH 271|CPSC 219; MATH 273'
	},

	'CPSC 319': {
		'course_name': 'Computer Science 319',
		'course_code': 'CPSC 319',
		'prerequisites': 'CPSC 219|CPSC 233'
	},

	'CPSC 219': {
		'course_name': 'Computer Science 219',
		'course_code': 'CPSC 219',
		'prerequisites': 'CPSC 217'
	},

	'CPSC 217': {
		'course_name': 'Computer Science 219',
		'course_code': 'CPSC 217',
		'prerequisites': ''
	},

	'CPSC 233': {
		'course_name': 'Computer Science 233',
		'course_code': 'CPSC 233',
		'prerequisites': 'CPSC 231'
	},

	'CPSC 231': {
		'course_name': 'Computer Science 231',
		'course_code': 'CPSC 231',
		'prerequisites': ''
	},
}

result = []

def getPrerequisitesDeep(selectedCourse, courses):
	selectedCourse = courses[selectedCourse]

	if('prerequisites' not in selectedCourse.keys()):
		return

	choices = selectedCourse['prerequisites'].split('|')

	print(choices)
	choice = input('Select a choice (starting at 0 from left to right):')

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
