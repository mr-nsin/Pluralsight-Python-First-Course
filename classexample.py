students = []
class Student:
	def add_student(self, name, student_id = 222):
		student = {'name' : name, 'student_id' : student_id}
		students.append(student)

student = Student()

student.add_student("Mark")

print(students)