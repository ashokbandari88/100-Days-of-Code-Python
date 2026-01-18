#Coded by Ashok Bandari

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("Welcome to caesar cipher!")

action = input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()
message = input("Type your message:\n").lower()
shift = int(input("Type the shift number: "))

text = ""
def caesar(message, shift, action):
    if action == "decode":
        shift *= -1
    for char in message:
        global text
        if char in alphabet:
            current_pos = alphabet.index(char)
            new_pos = (current_pos + shift) % 26
            text += alphabet[new_pos]
        else:
            text += char

caesar(message, shift, action)
print(text)