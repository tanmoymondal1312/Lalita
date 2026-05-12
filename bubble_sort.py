numbers = [64, 34, 25, 12, 22, 11, 90]

print("=" * 40)
print("        BUBBLE SORT ALGORITHM")
print("=" * 40)
print(f"Input List    : {numbers}")
print(f"Total Elements: {len(numbers)}")
print("-" * 40)

n = len(numbers)
swaps = 0
passes = 0

for i in range(n):
    passes += 1
    swapped_in_pass = False
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swaps += 1
            swapped_in_pass = True
    if not swapped_in_pass:
        break

print(f"Sorted List   : {numbers}")
print("-" * 40)
print(f"Total Swaps   : {swaps}")
print(f"Total Passes  : {passes}")
print(f"Minimum Value : {numbers[0]}")
print(f"Maximum Value : {numbers[-1]}")
print(f"Average Value : {sum(numbers) / len(numbers):.2f}")
print("=" * 40)
