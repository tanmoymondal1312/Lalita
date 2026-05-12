n = int(input("How many Fibonacci numbers do you want? "))

if n <= 0:
    print("Please enter a positive number!")
else:
    a, b = 0, 1
    total = 0
    series = []
    even_count = 0
    odd_count = 0

    print("\n" + "=" * 35)
    print("       FIBONACCI SERIES")
    print("=" * 35)

    for i in range(n):
        label = "Even" if a % 2 == 0 else "Odd"
        print(f"  Term {i+1:>2}: {a}  ({label})")
        total += a
        series.append(a)
        if a % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        a, b = b, a + b

    print("=" * 35)
    print(f"Series     : {series}")
    print(f"Sum        : {total}")
    print(f"Largest    : {max(series)}")
    print(f"Even terms : {even_count}  |  Odd terms : {odd_count}")
    print("=" * 35)
