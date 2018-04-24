students = []

class Student:

	school_name = "SpringField Elementary"  #declaring class or static attributes.

	def __init__(self, name, student_id = 222):
		self.name = name                  #declaring instance attributes.
		self.student_id = student_id
		students.append(self)

	def __str__(self):
		return "Student " + self.name

	def get_name_capitalize(self):
		return self.name.capitalize()

	def get_school_name(self):
		return self.school_name


class HighSchoolStudent(Student):
	school_name = "SpringField High School"

	def get_name_capitalize(self):
		original_value = super().get_name_capitalize()
		return original_value + "-HS"

james = HighSchoolStudent("james")
print (james.get_name_capitalize())