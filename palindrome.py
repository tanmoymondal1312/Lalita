word = input("Enter a word or sentence to check Palindrome: ")

if not word.strip():
    print("Please enter a valid word!")
else:
    clean = word.lower().replace(" ", "")
    reversed_clean = clean[::-1]

    print(f"\nOriginal  : {word}")
    print(f"Reversed  : {word[::-1]}")
    print(f"Length    : {len(word)} characters")
    print(f"Letters   : {len(clean)} (excluding spaces)")

    if clean == reversed_clean:
        print(f"\nResult    : '{word}' Is a Palindrome ✓")
        print("It reads the same forwards and backwards!")
    else:
        print(f"\nResult    : '{word}' Is Not a Palindrome ✗")
        print(f"Difference found at letter position(s).")
