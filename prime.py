num = int(input("Enter a number to check Prime: "))

print("\n" + "=" * 35)
print("        PRIME NUMBER CHECK")
print("=" * 35)
print(f"Number: {num}")
print("-" * 35)

if num <= 1:
    print(f"Result : Not a Prime Number")
    print(f"Reason : Prime numbers must be greater than 1")
elif num == 2:
    print(f"Result : Prime Number ✓")
    print(f"Note   : {num} is the smallest and only even prime")
else:
    is_prime = True
    factors = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            factors.append(i)
            factors.append(num // i)

    if is_prime:
        print(f"Result : Prime Number ✓")
        print(f"Divisors: 1 and {num} only")
    else:
        factors = sorted(set(factors))
        print(f"Result : Not a Prime Number ✗")
        print(f"Factors: 1, {', '.join(map(str, factors))}, {num}")

print("=" * 35)
