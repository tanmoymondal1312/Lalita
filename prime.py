num = int(input("Enter a number to check Prime: "))

if num <= 1:
    print(f"{num} Is Not a Prime Number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} Is a Prime Number")
    else:
        print(f"{num} Is Not a Prime Number")
