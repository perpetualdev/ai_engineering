# Collect the names of people attending a seminar
seminar_attendance = set()
seminar_attendance.add(input("What is your name?: "))
seminar_attendance.add(input("What is your name?: "))
seminar_attendance.add(input("What is your name?: "))
seminar_attendance.add(input("What is your name?: "))
seminar_attendance.add(input("What is your name?: "))

# Display them in alphabetical order
attendance_list = list(seminar_attendance)
attendance_list.sort()
print("Seminar Attendance in Alphabetical Order: ", attendance_list)
