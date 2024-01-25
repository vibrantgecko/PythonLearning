# Assignment 2

# Write a python program that asks the user to input the type of vegetable she wants from the following: 'Spinach', 'Carrot', 'Broccoli', 'Kale'.
# To finish entering the user should input 'Exit'. The program output should display the count of each type of vegetable entered.


########### SOLUTION ###########

current_stock = ["spinach", "carrot", "broccoli", "kale"]

print("Welcome to Pie Thon Veggie Shop! \nYou will be choosing vegetables from our current stock. \nCurrently we have the following to choose from:")

print(" ")
print("###########")
print(" ")

for i in current_stock:
    print(i)

print(" ")
print("###########")

print("Please enter one vegetable at a time. \nOnce you're done, enter 'Exit'. \nYou will then get a count for each vegetable you entered.")

spinach_count = 0
carrot_count = 0
broccoli_count = 0
kale_count = 0

shopping = True

while shopping:

    check = True
    while check:
        user_choice = input("Enter vegetable: ")
        user_choice_lower = user_choice.lower()
        if user_choice_lower in current_stock:
            check = False
        elif user_choice_lower == "exit":
            shopping = False
            check = False
        else:
            print("Error please try again.")
    

    if user_choice_lower == "spinach":
        spinach_count += 1
        print("Spinach Added")
    elif user_choice_lower == "carrot":
        carrot_count += 1
        print("Carrot Added")
    elif user_choice_lower == "broccoli":
        broccoli_count += 1
        print("Broccoli Added")
    elif user_choice_lower == "kale":
        kale_count += 1
        print("Kale Added")

print(" ")
print("###########")
print("Spinach: ", spinach_count)
print("Carrot: ", carrot_count)
print("Broccoli: ", broccoli_count)
print("Kale: ", kale_count)
    