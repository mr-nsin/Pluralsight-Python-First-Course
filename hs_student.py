from student import Student

class HighSchoolStudent(Student):
	school_name = "SpringField High School"

	def get_name_capitalize(self):
		original_value = super().get_name_capitalize()
		return original_value + "-HS"