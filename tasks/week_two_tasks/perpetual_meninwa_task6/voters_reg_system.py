# Ask for voters names and store in a set
# if voter registers twice, display a warning
voters = set()
for i in range(1, 4):
  voter_name = input(f"Enter the name of voter {i}: ")
  if voter_name in voters:
    print("Vote already registered for this user!!!")
  else:
    voters.add(voter_name)
    print(voters)

print("Voters Registration: ", voters)

# Display the total number of unique votes
print("Total Number of Voters: ", len(voters))
