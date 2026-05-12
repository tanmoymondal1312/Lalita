n = int(input("How many Fibonacci numbers do you want? "))

a, b = 0, 1
total = 0

print("\nFibonacci Series:")

for i in range(n):
    print(f"  Term {i+1}: {a}")
    total += a
    a, b = b, a + b

print(f"\nSum of {n} Fibonacci numbers: {total}")
