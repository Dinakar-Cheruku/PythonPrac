        # Challenge 1: Personal Info with Validation
        # Ask the user for their name, age, and favorite number.
        # Validate that age is positive and favorite number is between 1 and 100.
        # Print a sentence with all details.
        # Sample Input:
        # Name: Alex
        # Age: -5
        # Age: 25
        # Favorite Number: 150
        # Favorite Number: 42
        #
        # Expected Output:
        # Alex is 25 years old and loves the number 42.

# name = input("Enter the name: ")
# age = int(input("age?: "))
# fav = int(input("favorite number? (1-100): "))
# while age<=0 or fav not in range (1,101):
#     print("wrong info, enter again")
#     age = int(input("age?: "))
#     fav = int(input("favorite number? (1-100): "))
# print(f"{name} is {age} years old and loves the number {fav}.")

        # Smart Calculator
        # Ask the user for two numbers
        # Ask for an operation (+, -, *, /)
        # Perform the operation
        # If division, prevent division by zero
        # Keep asking until a valid operation is entered
        #
        # Sample Input:
        # Enter first number: 10
        # Enter second number: 0
        # Enter operation (+ - * /): /
        # Invalid operation or division by zero. Try again.
        # Enter operation (+ - * /): +
        #
        # Expected Output:
        # Result: 10

# a,b = map(int,input("Enter two numbers: ").split())
# op = input("select an operator (+,-,*,/): ")
# match op:
#     case "+":
#         print("result = ",a+b)
#     case "-":
#         print("result = ",a-b)
#     case "*":
#         print("result = ",a*b)
#     case "/":
#         print("result = ",a/b if b!=0 else "NOT DIVISIBLE BY 0")
#     case _:
#         print("Enter a valid operator")

#Learning Dictionaries
std = {}
std["name"] = 'Batthai'
std["age"] = 3
std["nature"] = "ferocious"
std["skills"] = ["sleeping","overacting","scrolling"]
std["hobbies"] = {"weekdays" : "Eating biryani","weekends" : "eating fried rice","holidays":"eating haleem"}

print(std["skills"][0])
print(std)

company = {
    "name": "TechCorp",
    "departments": {
        "data": {
            "head": "Alex",
            "employees": {
                "E1": {"name": "Sam", "role": "Data Engineer"},
                "E2": {"name": "Mia", "role": "Analytics Engineer"}
            }
        }
    }
}
print(company["departments"]["data"]["head"])
print(company["departments"]["data"]["employees"]["E1"]["role"])

company["departments"]["data"]["employees"]["E2"]["role"] = "Senior Analytics Engineer"
print(company)
