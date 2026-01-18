# Coded by Ashok Bandari
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the pyPassword Generator!")


nr_letters = int(input("How many letters would you like your password?\n"))
nr_symbols = int(input("How many symbols would you like your password?\n"))
nr_numbers = int(input("How many numbers would you like your password?\n"))
choice = input("Type 'easy' or 'hard' to select password level: ").lower()

def easy():
    password = ""
    for letter in range(nr_letters):
        password += random.choice(letters)
    for symbol in range(nr_symbols):
        password += random.choice(symbols)
    for number in range(nr_numbers):
        password += random.choice(numbers)

    print(f"Your password is: {password}")

def hard():
    password = []
    for letter in range(nr_letters):
        password += random.choice(letters)
    for symbol in range(nr_symbols):
        password += random.choice(symbols)
    for number in range(nr_numbers):
        password += random.choice(numbers)

    random.shuffle(password)
    print(f"Your password is: {password}")

if choice == "easy":
    easy()
elif choice == "hard":
    hard()
else:
    print("Invalid input. Try again!")