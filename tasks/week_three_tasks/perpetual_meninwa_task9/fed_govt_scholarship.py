# Federal Government Scholarship Key Eligibility Requirements:
#   - Citizenship:
#     - Applicant must be a citizen of Nigeria. 
#   - Enrollment:
#     - Must be a registered, full-time undergraduate student in  a recognized Nigerian university. 
#   - Other Scholarships:
#     - Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international. 
#   - Academic Qualification:
#     - For undergraduate courses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.

"""
  Get input from the user 
"""
name = input("Enter your name: ")
nationality = input("Enter your nationality: ")
is_undergraduate = input("Are you a registered, full-time undergraduate student in a recognised Nigerian university? y/n")
other_scholarship = input("Are you currently receiving any other scholarship from an entity in the Oil and Gas industry? y/n: ")
academic_qualification = input("Do you have five distinctions in relevant subjects including English and Mathematics? y/n: ")

try:
  if nationality.title() == 'Nigerian':
    if is_undergraduate == 'y':
      if other_scholarship == 'n':
        if academic_qualification == 'y':
          print('Congratulations! You are eligible for the scholarship.')
        # Throw an error if the candidate does not have five distinctions inclusive of English and Mathematics
        else:
          raise ValueError("You need at least five distinctions in relevant subjects including English and Mathematics to qualify")
      # Throw an error if candidate is a beneficiary of any other scholarship
      else:
        raise ValueError("You cannot be a beneficiary of any other scholarship to apply for this one")
    # Throw an error if the candidate is not a full-time undergraduate student in a Nigerian uni
    else:
      raise ValueError("You need to be a full-time undergraduate student in a Nigerian university to qualify")
  # Thorw an error if the candidate is not even a Nigerian
  else:
    raise ValueError("You have to be a Nigerian citizen to qualify")
# Catch any other error
except Exception as e:
  print("Unexpected error", e)
