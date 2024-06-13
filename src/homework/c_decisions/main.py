import decisions

option = 0
total = 0

option = float(input("\nHow many options for teachers do you have?\n"))
total = float(input("\nHow many teachers are their total?\n"))

ratio = decisions.get_options_ratio(option,total) #get the ratio

result = decisions.get_faculty_rating(ratio) #uses the ratio to get a value of rating, then turns to text

print("\nYour rating is:", result, "\n")

