# Ask for voters names and store in a set
# if voter registers twice, display a warning
voters = set()
voter_name = input("Enter your name: ")
if voter_name in voters:
  print("Vote already registered for this user!!!")
else:
  voters.add(voter_name)
  print(voters)
voter_name2 = input("Enter your name: ")
if voter_name2 in voters:
  print("Vote already registered for this user!!!")
else:
  voters.add(voter_name2)
  print(voters)
voter_name3 = input("Enter your name: ")
if voter_name3 in voters:
  print("Vote already registered for this user!!!")
else:
  voters.add(voter_name3)
  print(voters)
voter_name4 = input("Enter your name: ")
if voter_name4 in voters:
  print("Vote already registered for this user!!!")
else:
  voters.add(voter_name4)
  print(voters)
voter_name5 = input("Enter your name: ")
if voter_name5 in voters:
  print("Vote already registered for this user!!!")
else:
  voters.add(voter_name5)
  print(voters)

print("Voters Registration: ", voters)

# Display the total number of unique votes
print("Total Number of Voters: ", len(voters))
