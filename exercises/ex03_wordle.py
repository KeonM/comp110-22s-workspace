"""EX03 - Structured Wordle!"""
__author__ = "730476939"

W: str = "\U00002B1C"
G: str = "\U0001F7E9"
Y: str = "\U0001F7E8"


def contains_char(word: str, single_letter: str) -> bool:
    """Entering a single letter and checking if it is in the index of the word!"""
    assert len(single_letter) == 1
    if single_letter in word:
        return True
    else:
        return False


def emojified(guess: str, secret_word: str) -> str:
    """Creating G, Y, OR W boxes based on if the character is in the secret word!"""
    count = 0
    space = ""
    while count < len(secret_word):
        if guess[count] == secret_word[count]:
            space += G
        elif contains_char(secret_word, guess[count]):
            space += Y
        else:
            space += W
        count += 1
    return space


def input_guess(number_word: int) -> str:
    """Determining if guess is the length of secret word!"""
    guess = input(f"Enter a {number_word} character word: ")
    while len(guess) != number_word:
        guess = input(f"That wasn't {number_word} chars! Try again: ")
        if len(guess) == number_word:
            return guess
    if len(guess) == number_word:
        return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word = "codes"
    x = 0
    y = 1
    while x < 6:
        print(f"=== Turn {y}/6 ===")
        guess = input_guess(5)
        if guess == secret_word:
            print(emojified(guess, secret_word))
            print(f"You won in {y}/6 turns!")
            x = 6
        elif guess != secret_word:
            print(emojified(guess, secret_word))
        x += 1
        y += 1
    if x == 6:
        print("X/6 - Sorry, try again tomorrow!")
   

if __name__ == "__main__":
    main()