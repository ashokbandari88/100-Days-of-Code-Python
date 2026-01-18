# Coded by Ashok Bandari
import random
word_list = [
    'abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom',
    'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beepboop', 'blitz',
    'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo'
    ]

choice = random.choice(word_list)

display = []

for letter in choice:
    display += "_"
print(f"Word to guess: {display}")

lives = 6
is_game_on = True
while is_game_on:
    guess = input("Guess a letter: ")
    for position in range(len(choice)):
        letter = choice[position]
        if letter == guess:
            display[position] = letter
    result = ''.join(display)
    if guess not in choice:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(f"************ {lives}/6 LIVES LEFT ************")
        if lives == 0:
            is_game_on = False
            print("You lose. Game Over")
    elif result == choice:
        is_game_on = False
        print("You win. You saved a man")

    print(result)
print(f"Correct word is {choice}")