# Problem 1 - Tuple

marks = (80, 65, 90, 55, 75)

highest = max(marks)
lowest = min(marks)

print("Highest Mark:", highest)
print("Lowest Mark:", lowest)


# Problem 2 - Dictionary

student = {}

student["name"] = input("Enter name: ")
student["age"] = int(input("Enter age: "))
student["course"] = input("Enter course: ")

student["age"] = int(input("Enter updated age: "))
student["course"] = input("Enter updated course: ")

print("Updated Student Details:", student)
print("Student details updated successfully!")
