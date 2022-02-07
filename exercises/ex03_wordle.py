__author__ = "730476939"

W: str = "\U00002B1C"
G: str = "\U0001F7E9"
Y: str = "\U0001F7E8"


def contains_char(word: str, single_letter: str) -> bool:
    """Entering a single letter and checking if it is in the index of the word"""
    assert len(single_letter) == 1
    if single_letter in word:
        return True
    else:
        return False


def emojified(guess: str, secret_word: str) -> str:
    """Creating G, Y, OR W boxes based on if the character is in the secret word"""
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

print(emojified("guess", "gzzue"))
# print(contains_char("guess", "z"))