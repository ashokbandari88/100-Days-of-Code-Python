# Coded by Ashok Bandari
import os

def clear():
    os.system('cls')

print("Welcome to secret auction bidding system!")

def bidding():
    bids = {}
    should_continue = True
    while should_continue:
        bid_name = input("What is your name?: ")
        bid_amount = float(input("What is your bid amount?$ "))
        bids[bid_name] = bid_amount
        continue_bidding = input("Are there any other bidders? Type 'yes' or 'no': ")
        if continue_bidding == "no":
            should_continue = False
        elif continue_bidding == "yes":
            clear()
    return bids
bids = bidding()
print(bids)


def highest_bid():
    highest = 0
    winner_name = ""

    for name in bids:
        bid_amount = bids[name]
        if bid_amount > highest:
            highest = bid_amount
            winner_name = name

    print(f"The winner is {winner_name} with a bid of ${highest}")

highest_bid()