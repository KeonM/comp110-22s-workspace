"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730476939"

ind = 0
five_letter: str = input("Enter a 5-character word: ")
if len(five_letter) == 5:
    single_letter: str = input("Enter a single character: ")
    if len(single_letter) == 1:
        print("Searching for", single_letter, "in", five_letter)
        x = 0
        for i in five_letter:
            if i == single_letter:
                print(single_letter, "found at index", ind)
                x += 1
            ind += 1
        if x == 0:
            print("No instances of", single_letter, "found in", five_letter)
        elif x > 1:
            print(x, "instances of", single_letter, "found in", five_letter)
        else:
            print(x, "instance of", single_letter, "found in", five_letter)
    else:
        print("Error: Character must be a single character.")
        exit()
else:
    print("Error: word must contain 5 characters")
    exit()