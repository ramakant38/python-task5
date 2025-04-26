student = {
    "Alice":85,
    "Robin":91
}

name = input("Enter the student\'s name: ")

if name in student:
    print(name,"\'s marks: ",student.get(name))
else:
    print("Student not found")