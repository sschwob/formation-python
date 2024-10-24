# This "import" line loads your own "age_in_days.py" file.
from age_in_days import age_in_days

### Talking with the user ###
birth_year = int(input("What's your year of birth? > "))

birth_month = int(input("What's your month of birth? > "))

birth_day = int(input("What's your day of birth? > "))
#############################

print("Computing your age (with the most complicated algorithms)........")

# TODO: This is probably where you'd like to use your brand new function!
calculated_age = 0

# Finally, print user's age in days:
print(f"You are {calculated_age} days old... phew!")
