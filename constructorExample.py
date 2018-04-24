students = []
class Student:
	"""docstring for Student"""
	def __init__(self, name, student_id = 111):
		student = {'name' : name, 'student_id' : student_id}
		students.append(student)
	
	def __str__(self):
		return "Student"	

mark = Student("Mark Jukerberg")
print (mark)
