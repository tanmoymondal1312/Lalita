num = int(input("Enter a number to check Prime: "))

print(f"\n--- Prime Check for {num} ---")

if num <= 1:
    print(f"{num} Is Not a Prime Number")
elif num == 2:
    print(f"{num} Is a Prime Number (smallest prime)")
else:
    is_prime = True
    factor = None
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            factor = i
            break
    if is_prime:
        print(f"{num} Is a Prime Number")
        print(f"Divisible only by 1 and {num}")
    else:
        print(f"{num} Is Not a Prime Number")
        print(f"Divisible by {factor} and {num // factor}")
