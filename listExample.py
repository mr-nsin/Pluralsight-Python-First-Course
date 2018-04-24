student_names = ["Mark", "Katarina", "Jessica"]
# student_names[3] = "Homer" #No can DO! We can not simply add into list 
student_names.append("Homer")

print(student_names)

print(str("Mark" in student_names) + " " + str("Nitin" in student_names))

print (len(student_names))

del student_names[2]  #will shift the elements to left in list.

print (student_names)

#List Slicing (Will not change list value)
#last value is not included
#list[initial_value:last_value:increment]
print (student_names[1:])
print(student_names[-1::-1])
print (student_names[1:-1])