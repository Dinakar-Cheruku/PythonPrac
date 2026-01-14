#Day 1 and 2 assignment

#1

name = "Dinakar"
age = 24
favourite_number = 7

print(f"My name is {name}, I am {age} years old, and my favourite number is {favourite_number}.")



#2

num1 = 10
num2 = 5

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)




#student profile
student_name = "Aarav"
grade = "8th"
age = 13

print(f"The student's name is {student_name}, they are {age} years old, and they study in grade {grade}.")



#shopping bill calculator
item1_price = 50
item2_price = 120
item3_price = 30
total_bill = item1_price + item2_price + item3_price
print(f"The total bill amount is {total_bill}.")




#Counting numbers

for i in range(1, 11):
    print(i)



#Even Numbers
for i in range(1, 21):
    if i % 2 == 0:
        print(i)



#Multiplication table

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)



# Steps taken each day (can be customized)
steps = [5000, 7000, 8000, 6000, 7500, 9000, 6500]

for day in range(1, 8):
    print(f"Day {day}: {steps[day-1]} steps")


#attendance and students
for student in range(1, 11):
    print(f"Student {student}: Present")



#Multiplication table for Shop prices
# Ask the user for the price of one item
price = float(input("Enter the price of one item: "))
# Loop through quantities 1 to 10
for quantity in range(1, 11):
    total_cost = price * quantity
    print(f"Quantity {quantity}: Total cost = {total_cost}")


#while loop, Sum of numbers
# Initialize variables
num = 1
total_sum = 0
#Loop from 1 to 50
while num <= 50:
    total_sum += num  # Add current number to total_sum
    num += 1          # Move to next number

# Print the final sum
print(f"The sum of numbers from 1 to 50 is {total_sum}")

#while loop, password checker
# Set the correct password
correct_password = "python123"

# Ask the user for the password
entered_password = input("Enter the password: ")

# Keep asking until the correct password is entered
while entered_password != correct_password:
    print("Incorrect password. Try again.")
    entered_password = input("Enter the password: ")

# Success message
print("Password accepted! You are logged in.")


#Number guessing game
import random

sn = random.randint(1,10)
n = 0
i = 0
while n!=sn:
    i += 1
    n = int(input("Enter your guess btw 1 to 10: "))
    if n<sn:
        print("Too low")
    elif n>sn:
        print("Too high")
    else:
        print("-------------------------")
        print("you have done it, its ",sn," and you took ",i," guesses")


#saving money tracker
# Initialize variables
total_savings = 0
daily_saving = 50
days = 0

# Keep saving until total_savings reaches 1000
while total_savings < 1000:
    total_savings += daily_saving
    days += 1

# Print the total days required
print(f"It will take {days} days to save {total_savings} dollars.")


#Login systems
#Store correct credentials
correct_username = "admin"
correct_password = "pass123"

# Ask the user for username and password
username = input("Enter username: ")
password = input("Enter password: ")

# Keep asking until correct credentials are entered
while username != correct_username or password != correct_password:
    print("Incorrect username or password. Try again.")
    username = input("Enter username: ")
    password = input("Enter password: ")

# Welcome message
print(f"Welcome, {username}! You are logged in.")


#Mini project

# Ask the user for units consumed
units = float(input("Enter the number of electricity units consumed: "))

# Initialize total bill
total_bill = 0

# Calculate bill based on units consumed
if units <= 100:
    total_bill = units * 5
else:
    # First 100 units at 5/unit + remaining units at 7/unit
    total_bill = (100 * 5) + ((units - 100) * 7)

# Print the total bill
print(f"Total electricity bill for {units} units is: {total_bill} currency units")

