# Meow 3 times
#print("meow")
#print("meow")
#print("meow")


# make it in to a while loop (using minus)
#i = 3
#while i != 0:
#    print("meow")
#    i = i - 1

# make it into a while loop using plus

#i = 1
#while i <= 3:
#    print("meow")
#    i = i + 1

# for loop
#for i in [0, 1, 2]:
#    print("meow")

# improve for loop by using the range function

#for i in range(3):
#    print("meow")

#print("meow\n" * 3)


#students = ["shoaib", "akmal", "nabeela"]

# print students
#print(students[0])
#print(students[1])
#print(students[2])

# print students in a better way

#for student in students:
#    print(student)


# Dictionary (using multilines so it is clear, can put all in one line, student and house (dictionary is key and value ))

#students = {
#    "Shoaib": "81 Leigh road",
#    "Akmal": "81 Leigh road"
#}

#print(students["Shoaib"])

#for student in students:
#    print(student, students[student], sep=", ")


# LIST OF DICTIONARIES

students = [
    {"name": "Shoaib", "House": "81 Leigh Road", "DOB": "17/02/2001"},
    {"name": "Akmal", "House": "81 Leigh Road", "DOB": None}
]

for student in students:
    print(student["name"], student["House"], sep=",")