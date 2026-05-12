n = int(input("How many Fibonacci numbers do you want? "))

if n <= 0:
    print("Please enter a positive number!")
else:
    a, b = 0, 1
    total = 0
    series = []

    print("\nFibonacci Series:")

    for i in range(n):
        print(f"  Term {i+1}: {a}")
        total += a
        series.append(a)
        a, b = b, a + b

    print(f"\nSeries     : {series}")
    print(f"Sum        : {total}")
    print(f"Largest    : {max(series)}")
