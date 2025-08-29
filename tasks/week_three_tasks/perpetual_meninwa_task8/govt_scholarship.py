# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))

# eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

"""
  - Ask the candidate to input their name and age and store it in variables called name and age respectively

  - Ask the candidate to enter their test score and store in a variable called score

  - Check their eligibility using operators (which returns true or false)
  -> If the candidate is less than 18 years old and has a score that is greater than 70, then the candidate is eligible

  - Display the candidate's data using escape sequence as well as their Eligibility (True or False)
"""

# Federal Government Scholarship Key Eligibility Requirements:
#   - Citizenship:
#     - Applicant must be a citizen of Nigeria. 
#   - Enrollment:
#     - Must be a registered, full-time undergraduate student in  a recognized Nigerian university. 
#   - Other Scholarships:
#     - Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international. 
#   - Academic Qualification:
#     - For undergraduate courses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.

# Defining Variables
name = input("Enter your name: ")
nationality = input("Enter your nationality: ")
is_undergraduate = input("Are you a registered, full-time undergraduate student in a recognised Nigerian university? y/n")
other_scholarship = input("Are you currently receiving any other scholarship from an entity in the Oil and Gas industry? y/n: ")
academic_qualification = input("Do you have five distinctions in relevant subjects including English and Mathematics? y/n: ")

eligible = (nationality.lower() == 'nigerian') and (is_undergraduate.lower() == 'y') and (other_scholarship.lower() == 'n') and (academic_qualification.lower() == 'y')

print(f"Candidate: {name}\nNationality: {nationality}\nIs Undergraduate: {is_undergraduate}\nReceiving Other Scholarship: {other_scholarship}\nEligible: {eligible}")
