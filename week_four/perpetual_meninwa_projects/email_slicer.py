# Email Slicer

def main():
  try:
    # Get input from user
    email_add = input("What is your email address? ")
    if email_add == "":
      raise ValueError("Email address cannot be empty")
    elif "@" not in email_add:
      raise ValueError("Email address is not valid. Try again")
    else:
      email_split = email_add.split("@")
      username = email_split[0]
      domain = email_split[1]
      print(f"Email Address\t\tDomain\n====================================\n{username}\t{domain}")
  except ValueError as e:
    print("Error: ", e)

main()
