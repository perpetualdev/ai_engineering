# Collect the names of people attending a seminar
seminar_attendance = set()
for i in range(1, 6):
  seminar_attendance.add(input(f"Enter the name of attendee {i}: "))

# Display them in alphabetical order
attendance_list = list(seminar_attendance)
attendance_list.sort()
print("Seminar Attendance in Alphabetical Order: ", attendance_list)
