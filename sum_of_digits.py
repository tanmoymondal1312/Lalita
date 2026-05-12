num = int(input("Enter a Number to find Sum of Digits: "))

total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total = total + digit
    temp = temp // 10

print(f"Sum of Digits of {num} is {total}")
