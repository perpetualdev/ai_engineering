# Ask user for 3 student names (separated by space)
# For each student, ask for their score
# Store the results in two lists
student_names = list()
student_scores = []

student_one = input("Student One Name: ")
student_names.append(student_one)
student_one_score = float(input("What is student one score: "))
student_scores.append(student_one_score)

student_two = input("Student two name: ")
student_names.append(student_two)
student_two_score = float(input("Student Two Score: "))
student_scores.append(student_two_score)

student_three = input("Student Three Name: ")
student_names.append(student_three)
student_three_score = float(input("Student Three Score: "))
student_scores.append(student_three_score)

print(student_names)
print(student_scores)

# Print formatted output of Name and Score neatly
print(f"Name\t\tScore\n========================\n{student_one}\t\t{student_one_score}\n{student_two}\t\t{student_two_score}\n{student_three}\t\t{student_three_score}")
