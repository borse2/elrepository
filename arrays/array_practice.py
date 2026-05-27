#Boris Adokou
#Arrays
#Create a list of students using arrays
import random
students=["Robert", "Khalil", "Omar", "Jayden", "Adrian", "Skyler", "Mia", "Alicia", "Isaac", "Joel"]
print(students[4:7])
students.append("Max")
print(students)
del students[4]
print(students)
students.sort()
print(students)
print(random.choice(students))
