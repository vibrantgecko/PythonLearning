# Exercise 2

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
## Extras:
#### 1. If the number is a multiple of 4, print out a different message.
#### 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

####### SOLUTION ########

check = True
while check:
    try:
        user_num_raw = input("Enter a number: ")
        user_num_int = int(user_num_raw)
        check = False
    except ValueError:
        print("Please enter a number")

if user_num_int % 2 > 0:
    print("This is an odd number you got here.")
else:
    print("You got an even number on your hands.")