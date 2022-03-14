__author__ = "730476939"

secret_word = "pythoan"
guess = input(f"What is your {len(secret_word)}-letter guess? ")

WHITE_BOX = "\U00002B1C"
GREEN_BOX = "\U0001F7E9"
YELLOW_BOX = "\U0001F7E8"
x = 0

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)}-letters! Try again: ")
while x < len(secret_word):
    x+=len(secret_word)
    if guess == secret_word:
        print(GREEN_BOX * 6)
        print("Woo! You got it!")
    else:
        count = 0
        space = ""
        for i in guess:
            if i == secret_word[count]:
                space += GREEN_BOX
            elif i in secret_word:
                space += YELLOW_BOX
            else:
                 space += WHITE_BOX
            count += 1
        print(space)
        print("Not quite. Play again soon!")