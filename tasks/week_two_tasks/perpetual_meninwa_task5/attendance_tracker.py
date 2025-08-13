# Write a python program that stores the days of the week in a tuple
days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(days_of_the_week)

# And the months of the year in another tuple
months_of_the_year = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
print(months_of_the_year)

# Ask user to enter student's name, gender, course track, current month (1-12), current day (1-7)
student_name = input("Student Name: ")
gender = input("Gender: ")
course_track = input("Course Track: ")
month = int(input("Month(1-12): "))
day = int(input("Day(1-7): "))

print(f"{student_name}\t{gender}\t{course_track}\t{months_of_the_year[month - 1]}\t{days_of_the_week[day - 1]}")
print(f"{student_name} is a {gender} learning {course_track} on {days_of_the_week[day - 1]}, {months_of_the_year[month - 1]} 2025.")