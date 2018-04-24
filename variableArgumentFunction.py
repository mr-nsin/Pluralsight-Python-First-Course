students = []

def get_student_titlecase():
	student_titlecase = []
	for student in students:
		student_titlecase.append(student.title())
	return student_titlecase

def print_student_titlecase():
	student_titlecase = []
	for student in students:
		student_titlecase = student.title()
		print (student_titlecase)
	

def add_student(name, student_id = 112):
	student = {"name" : name, "student_id" : student_id}
	students.append(student)

#Example of variable length argument
#keywords Arguments function example/
def var_args(name, **kwargs):
	print (name)
	print (kwargs["description"], kwargs["feedback"])


add_student("nitin")
add_student (name = "Nikita", student_id = 113)

var_args("Nitin", description = "Loves Python!", feedback = None, pluralsight_subscription = True) #the last variable length aruments are taken in dictionary by python.

#print_student_titlecase()

print (students)

# student_list = get_student_titlecase()
# print (student_list)