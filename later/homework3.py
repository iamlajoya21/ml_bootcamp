# Question 1: The Circle Calculator (Math & Floats)
# Write a program that asks the user for the radius of a circle (as a floating-point number).
# Calculate the area of the circle using the formula: $Area = \pi \times r^2$ (Use math.pi).
# Print the area rounded to 2 decimal places.
# Hint: Remember to import the math module.
# ==================================================
# PROBLEM 1: The Circle Calculator
# ==================================================

print("=" * 50)
print("PROBLEM 1: Circle Area Calculator")
print("=" * 50)

import math  # Import math module for pi

# Ask user for radius
radius = float(input("Enter the radius of the circle: "))

# Calculate area using formula: Area = π * r^2
area = math.pi * radius ** 2
area = round(area, 2)
# Print area rounded to 2 decimal places
print(f"Area of the circle: {area:.2f}")



# Question 2: The Savings Account (Augmented Assignments)
# You start with a bank balance of $1000. Write a program that simulates a deposit and a withdrawal using augmented assignments (+=, -=).
# Create a variable balance = 1000.
# Ask the user: "How much do you want to deposit?" Add this to the balance using +=.
# Ask the user: "How much do you want to withdraw?" Subtract this from the balance using -=.
# Print the final remaining balance.



# ==================================================
# PROBLEM 2: The Savings Account
# ==================================================

print("\n" + "=" * 50)
print("PROBLEM 2: Savings Account Simulator")
print("=" * 50)

# Start with initial balance
balance = 1000.0
print(f"Starting balance: ${balance:.2f}")

# Get deposit amount and add to balance using +=
deposit_amount = float(input("How much do you want to deposit? $"))
balance += deposit_amount  # Augmented assignment for deposit

# Get withdrawal amount and subtract from balance using -=
withdrawal_amount = float(input("How much do you want to withdraw? $"))
balance -= withdrawal_amount  # Augmented assignment for withdrawal

# Print final balance
print(f"Final balance: ${balance:.2f}")


# Question 3: String Slicer
# Write a program that asks the user to input a single word (e.g., "Python").
# Print the first 2 characters of the word.
# Print the last 2 characters of the word.
# Print the word in ALL UPPERCASE.
# Print the length of the word.


# ==================================================
# PROBLEM 3: String Slicer
# ==================================================

print("\n" + "=" * 50)
print("PROBLEM 3: String Slicer")
print("=" * 50)

# Ask user for a word
word = input("Enter a single word: ")

# Get first 2 characters using slicing
first_two = word[:2]

# Get last 2 characters using slicing
last_two = word[-2:]

# Convert to uppercase
uppercase_word = word.upper()

# Get length of word
word_length = len(word)

# Print all results
# print(f"First 2 characters: {first_two}")
# print(f"Last 2 characters: {last_two}")
# print(f"Uppercase: {uppercase_word}")
# print(f"Length: {word_length} characters")



# Print all results
print("First 2 characters: ", first_two)
# print(f"Last 2 characters: {last_two}")
# print(f"Uppercase: {uppercase_word}")
# print(f"Length: {word_length} characters")
