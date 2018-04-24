students = []

def get_student_titlecase():
	student_titlecase = []
	for student in students:
		student_titlecase.append(student["name"].title())
	return student_titlecase

def print_student_titlecase():
	student_titlecase = get_student_titlecase()
	print (student_titlecase)
	

def add_student(name, student_id = 112):
	student = {"name" : name, "student_id" : student_id}
	students.append(student)


user_choice = input("You want to add student, type Yes/No and hit enter.")
while(user_choice == "Yes"):
	student_name = input("Enter Student Name : ")
	student_id = input("Enter Student ID : ")
	add_student(student_name, student_id)
	user_choice = input("You want to add student, type Yes/No and hit enter.")

print_student_titlecase()
   