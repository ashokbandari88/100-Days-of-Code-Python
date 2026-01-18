import random
print("Let's play Rock, Paper & Scissors Game!")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor:\n "))
computer_choice = random.randint(0, 2)
asci_ = ["Rock", "Paper", "Scissor"]

if user_choice < 0 or user_choice >= 3:
    print("You typed an invalid number. You've lost")
    exit()
else:
    print(f"User Choice: {asci_[user_choice]} and Computer choice: {asci_[computer_choice]}")
    if user_choice == computer_choice:
        print("It's a draw. Play again!")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win😍")
    elif computer_choice == 0 and user_choice == 2:
        print("You've Lost")
    elif user_choice > computer_choice:
        print("You win😍")
    elif computer_choice > user_choice:
        print("You've Lost")
