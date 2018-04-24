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

def save_file(student):
	try:
		f = open("students.txt", "a")
		f.write(student + "\n")
		f.close()
	except Exception:
		print ("Couldn't save the file.")

def read_file():
	try:
		f = open("students.txt", "r")
		for student_name in f.readlines():
			add_student(student_name)
		f.close()
	except Exception:
		print ("Couldn't read file.")	

read_file()
print_student_titlecase()

student_name = input("Enter Student Name : ")
student_id = input("Enter Student ID : ")

add_student(student_name, student_id)

save_file(student_name)

print(students)