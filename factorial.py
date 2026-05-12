num = int(input("Enter a number to find Factorial: "))

factorial = 1

print(f"\n--- Factorial of {num} ---")

if num < 0:
    print("Factorial is not defined for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    formula = " x ".join(str(i) for i in range(1, num + 1))
    print(f"Formula   : {formula}")
    print(f"Factorial of {num} = {factorial}")
