word = input("Enter a word or sentence to check Palindrome: ")

print("\n" + "=" * 38)
print("        PALINDROME CHECKER")
print("=" * 38)

if not word.strip():
    print("Please enter a valid word!")
else:
    clean = word.lower().replace(" ", "")
    reversed_clean = clean[::-1]

    print(f"Original   : {word}")
    print(f"Reversed   : {word[::-1]}")
    print(f"Length     : {len(word)} characters")
    print(f"Letters    : {len(clean)} (excluding spaces)")
    print("-" * 38)

    if clean == reversed_clean:
        print(f"RESULT     : Palindrome ✓")
        print(f"'{word}' reads the same forwards and backwards!")
    else:
        print(f"RESULT     : Not a Palindrome ✗")

print("=" * 38)
