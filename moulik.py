n = int(input("Enter number: "))

if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("মৌলিক না")
            break
    else:
        print("মৌলিক সংখ্যা")
else:
    print("মৌলিক না")

