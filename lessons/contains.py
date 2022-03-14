"""Example of writing a function to search a list"""

def main() -> None:
    guess = input("What is the code word: ")
    answers = ["word", "music", "return"]
    if contains(guess, answers):
        print("you're in")
    else:
        print("Wrong")
    

def contains(needle: str, haystack: list[str]) -> bool:
    """Test of needle is found in haystack"""
    for item in haystack:
        if item == needle:
            return True
    return False


print(__name__)
if __name__ == "__main__":
    main()