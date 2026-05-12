word = input("Enter a word or sentence to check Palindrome: ")

if not word.strip():
    print("Please enter a valid word!")
else:
    clean = word.lower().replace(" ", "")
    reversed_clean = clean[::-1]

    print(f"\nOriginal  : {word}")
    print(f"Reversed  : {word[::-1]}")
    print(f"Length    : {len(word)} characters")

    if clean == reversed_clean:
        print(f"Result    : '{word}' Is a Palindrome ✓")
    else:
        print(f"Result    : '{word}' Is Not a Palindrome ✗")
