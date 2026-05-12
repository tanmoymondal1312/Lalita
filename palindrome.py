word = input("Enter a word to check Palindrome: ")

reversed_word = word[::-1]

if word == reversed_word:
    print(f"{word} Is a Palindrome")
else:
    print(f"{word} Is Not a Palindrome")
