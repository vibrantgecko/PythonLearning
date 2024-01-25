# Exercise 2

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
## Extras:
#### 1. If the number is a multiple of 4, print out a different message.
#### 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

####### SOLUTION ########

# A while loop to ensure a number is entered using try/except until one is entered
check = True
while check:
    try:
        user_num_raw = input("Enter a number: ")
        user_num_int = int(user_num_raw)
        check = False
    except ValueError:
        print("Please enter a number")

# Checks to see if user number is even
if user_num_int % 2 > 0:
    print("This is an odd number you got here.")
else:
    print("You got an even number on your hands.")

# Checks to see if user number is evenly divisible by 4
if user_num_int % 4 == 0:
    print("This number is also divisible by 4!")

# Ask user for two numbers and makes sure numbers are entered
print("Now I need two numbers from you.")

check = True
while check:
    try:
        user_num1_raw = input("Number 1: ")
        user_num1_int = int(user_num1_raw)
        check = False
    except ValueError:
        print("Please enter a number")

check = True
while check:
    try:
        user_num2_raw = input("Number 2: ")
        user_num2_int = int(user_num2_raw)
        check = False
    except ValueError:
        print("Please enter a number")

# Set num and check values
num = user_num1_int
check = user_num2_int

# Check if num is evenly divisble by check
if num % check == 0:
    print("Number 1 is evenly divisible by Number 2.")
else:
    print("Number 1 is not evenly divisible by Number 2.")