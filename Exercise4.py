# Exercise 4

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

####### SOLUTION ########

user_num = input("Number: ")
user_num_int = int(user_num)

range_check = range(1,user_num_int+1)
divisor_list = []

for i in range_check:
    if user_num_int % i == 0:
        divisor_list.append(i)

print(divisor_list)