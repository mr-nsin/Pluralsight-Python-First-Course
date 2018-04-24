import hs_student

student_name = input ("Enter Student Name : ")
student_id = input ("Enter Student ID : ")

high_school_student = hs_student.HighSchoolStudent(student_name)
print (high_school_student.get_name_capitalize())