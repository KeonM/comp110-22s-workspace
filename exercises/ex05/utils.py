"""Utils of ex05."""
__author__ = "730476939"


def only_evens(numbers: list[int]) -> list[int]:
    """Finds all even numbers in given list."""
    count = 0
    even_numbers: list[int] = []
    while count < len(numbers):
        if numbers[count] % 2 == 0:
            even_numbers.append(numbers[count])
        count += 1
    return even_numbers


def sub(the_list: list[int], begin: int, end: int) -> list[int]:
    """Finds all numbers in list based on range given."""
    empt: list[int] = list()
    for x in the_list[begin:end]:
        empt.append(x)
    return empt


def concat(first: list[int], second: list[int]) -> list[int]:
    """Combines the lists."""
    res: list[int] = []
    for x in first:
        res.append(x)
    for x in second:
        res.append(x)
    return res


print(only_evens([1, 2, 3, 4, 5, 6]))