# Store days of the week in a tuple
days_of_the_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

# Ask user to input an activity for three specific days
first_three_days = days_of_the_week[:3]
activities = tuple(input("Enter an activity for Sunday, Monday, and Tuesday respectively, separated by commas: ").split(','))
print("You entered:", activities)
print(first_three_days)

# Create a dictionary mapping the first three days to the activities
days_and_activities = dict(zip(first_three_days, activities))

print("Activities for the first three days of the week:", days_and_activities)
