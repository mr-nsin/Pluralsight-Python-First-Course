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
#Variable length argument function are used when we don't know about number of arguments to be passed in function.
def var_args(name, *args):
	print (name)
	print (args)


add_student("nitin")
add_student (name = "Neha", student_id = 113)

var_args("Nitin", "Loves Python", None, "hello", True, "hello") #the last variable length aruments are taken in tuple by python.

#print_student_titlecase()

print (students)

# student_list = get_student_titlecase()
# print (student_list)