student = {
	"name" : "Mark",
	"student_id" : 123,
	"feedback" : "positive"
}

print (student)
student["last_name"] = "Kowaski"
try:
	lastName = student["last_name"]
	numbered_lastName = 3 + lastName
except KeyError:
	print ("Error finding last name.")
except TypeError as error:
	print ("I can't add these two values.")
	print (error)

print ("This code executes.")