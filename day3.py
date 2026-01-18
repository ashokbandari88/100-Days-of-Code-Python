#Coded by Ashok Bandari
print("Welcome to the Treasure Island!\n Your mission is to find treasure.")



choice1 = input("You are at crossroads. Where do you want to go? \n Type 'left' or 'right': ").lower()
if choice1 == "right":
    print("You fell into a hole. Game Over.😢")
else:
    print("You have come to the lake. There is island in the middle of the lake")
    choice2 = input("Type 'wait to wait for boat. Type 'swim' to swim across: ").lower()

    if choice2 == 'swim':
        print("You got attached by angry trout. Game Over.😢")
    else:
        print("You arrive the Island unharmed. There is house with 3 doors.")
        choice3 = input("One red, one yellow and one blue. Which color do you choose?:").lower()

        if choice3 == 'red':
            print("Its room full of fire. Game Over.😢")
        elif choice3 == 'blue':
            print("You enter a game of beasts. Game Over.😢")
        else:
            print("You found the treasure! You Win😍😀")