word = input("Enter a word to check Palindrome: ")

reversed_word = word[::-1]

print(f"\nOriginal  : {word}")
print(f"Reversed  : {reversed_word}")

if word.lower() == reversed_word.lower():
    print(f"Result    : {word} Is a Palindrome")
else:
    print(f"Result    : {word} Is Not a Palindrome")
