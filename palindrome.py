# Palindrome

word = input("Type a word here: ").lower()

if (word == word[:: -1]):
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")