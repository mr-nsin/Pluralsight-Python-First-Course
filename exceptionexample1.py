student = {
	"name" : "Mark",
	"student_id" : 123,
	"feedback" : "positive"
}

print (student)

try:
	lastName = student["last_name"]
except KeyError:
	print ("Error finding last name.")

print ("This code executes.")