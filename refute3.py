letter = input("Enter a letter: ").lower()
if letter.isalpha() and len(letter) == 1:
    if letter in 'aeiou':  # Check if it is a vowel
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet.")