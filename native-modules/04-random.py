from random import random, randint, shuffle, choice, choices
from string import ascii_letters, digits

# Initialize lists
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
subset = [5, 8, 9, 4, 6]

# Shuffle the list
shuffle(numbers)

# Random operations
print(f"Random float between 0 and 1: {random()}")
print(f"Random integer between 1 and 10: {randint(1, 10)}")
print(f"Shuffled list: {numbers}")
print(f"Random single choice from subset: {choice(subset)}")
print(
    f"Random 3 choices (with replacement) from subset: {choices(subset, k=3)}")
print(f"Random 3 choices from a string: {choices('asdasdsad', k=3)}")

# Character sets for password generation
chars = ascii_letters
digits_set = digits
password_chars = choices(chars + digits_set, k=10)

# Output character sets and generated password
print(f"ASCII Letters: {chars}")
print(f"Digits: {digits_set}")
print(f"Selected characters for password: {password_chars}")

# Build and print password
password = "".join(password_chars)
print(f"Generated password: {password}")
