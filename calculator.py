num1 = float(input("Enter First Number: "))
operator = input("Enter Operator (+, -, *, /): ")
num2 = float(input("Enter Second Number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 == 0:
        print("Cannot Divide by Zero!")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid Operator!")
