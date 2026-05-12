num = int(input("Enter a Number to check Armstrong: "))

total = 0
temp = num
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    total = total + (digit ** digits)
    temp = temp // 10

if total == num:
    print(f"{num} Is an Armstrong Number")
else:
    print(f"{num} Is Not an Armstrong Number")
