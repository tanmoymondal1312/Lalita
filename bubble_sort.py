numbers = [64, 34, 25, 12, 22, 11, 90]

print("Before Sorting:", numbers)
print(f"Total Elements: {len(numbers)}")

n = len(numbers)
swaps = 0

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swaps += 1

print("After Bubble Sort:", numbers)
print(f"Total Swaps: {swaps}")
print(f"Smallest: {numbers[0]}  |  Largest: {numbers[-1]}")
