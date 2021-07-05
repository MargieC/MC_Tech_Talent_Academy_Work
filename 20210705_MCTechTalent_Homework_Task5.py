#Task 5
number_1 =int(input("Please enter the first number: "))
number_2 =int(input("Please enter the second number: "))
operator = input("Enter an operation (/ + - * ^2): ")

if operator == "/":
    print("Result: " + str(number_1/number_2))
elif operator == "*":
    print("Result: " + str(number_1*number_2))
else:
    print("Unknown operator " + operator)