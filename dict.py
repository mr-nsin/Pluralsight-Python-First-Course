#Dictionaries are used when values to be stored are present in key and value pairs, used to store structured data.
#In Dictionary value can be of any type, can be a complete dictionary.
student = {
	"name" : "Nitin Singhal",
	"student_id" : 123,
	"blood_group" : 'O+'
}

#List of Dictionaries
all_students = [
	{"name" : "Nitin", "student_id" : 123},
	{"name" : "ABC", "student_id" : 1234}
]
print (student)
print (all_students)
print (all_students[0]["name"]) #To get value of particular key in Dict.
print (all_students[0].get("last_name", "UNKNOWN"))
print (all_students[0].keys())
print (all_students[0].values())
del student["name"]
print (student)