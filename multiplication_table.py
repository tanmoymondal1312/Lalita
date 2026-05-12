num = int(input("Enter a Number to print Multiplication Table: "))

print(f"\nMultiplication Table of {num}:\n")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
