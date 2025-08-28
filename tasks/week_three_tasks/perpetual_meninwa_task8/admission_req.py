# Define variables
name = input("Enter your name: ")
departmental_cut_off = 280
post_utme = 75

# ==================== UTME ELIGIBILITY ======================
utme_score = int(input("Enter your UTME score: "))
is_unilag_first_choice = input("Is UNILAG your first choice? Yes/No: ")

utme = (utme_score >= 200) and is_unilag_first_choice.lower() == "yes"

# ========================== OTHERS ===========================
has_relevant_credit = input("Do you have five credit passes at one sitting in relevant subjects, including English and Mathematics? Yes/No: ")

post_utme_score = int(input("Enter your post utme score: "))

# Checking for eligibility
eligible = utme and (post_utme_score >= post_utme) and has_relevant_credit.lower() == "yes"

if eligible:
  print(f"Candidate \"{name}\" is eligible for admission.")
else:
  print("Not eligible")

