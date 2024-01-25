# Exercise 1

# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
## Extras:
#### 1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
#### 2. Print out that many copies of the previous message on separate lines.

####### SOLUTION ########

# Starting message for user
print("Hello! What is your name?")

# Name of user
user_name = input("Name: ")

# Response message with user's name
print("Nice to meet you " + user_name + "!")

# Ask user for age
print("How old are you?")

# Loop for user's age input to make sure a number is entered
check = True
while check:
    try:
        user_age_raw = input("Age: ")
        user_age_int = int(user_age_raw)
        check = False
    except ValueError:
        print("Oops! That's not a number silly. Try again.")

# Message to tell user intention of giving them the year they turn 100
print("Thank you for the information " + user_name + "!","I will now tell you the year in which you will turn 100.", "Calculating", sep = "\n")

# Loading string lines
counter = 0

while counter < 10:
    print(".....")
    counter += 1

# If statement to handle scenarios where age is >100, =100, <100
current_year = 2024

if user_age_int > 100:
    year_100_int = current_year - user_age_int + 100
    year_100_str = str(year_100_int)
    print("Oh wow you are already past 100!", "You turned 100 in " + year_100_str +".", sep="\n")
elif user_age_int == 100:
    current_year_str = str(current_year)
    print("Congratulations! You are 100 years old!", "You turned 100 in " + current_year_str +".", sep="\n")
else:
    year_100_int = current_year - user_age_int + 100
    year_100_str = str(year_100_int)
    print("You are under 100 years.", "You will turn 100 in " + year_100_str +".", sep="\n")

# Message to tell user to enter a number
print("Now pick a number please :)")

# Loop for user's number input to make sure a number is entered
check = True
while check:
    try:
        user_num_raw = input("Number: ")
        user_num_int = int(user_num_raw)
        check = False
    except ValueError:
        print("Oops! That's not a number silly. Try again.")

# Set previous message
previous_message = "Now pick a number please :)"

# Print previous message on one line
print(previous_message * user_num_int)

# Print previous message on seperate lines
for x in range(user_num_int):
    print(previous_message)