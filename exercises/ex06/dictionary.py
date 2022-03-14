"""Dictionaries!"""
__author__ = "730476939"


from calendar import c


def invert(a: dict[str, str]) -> dict[str, str]:
    """Reverses x and y."""
    b = {y: x for x, y in a.items()}
    return b


def favorite_color(a: dict[str, str]) -> str:
    """Turns dictionary values into a list and keeps count of how many times a value is called. Max is return."""
    value = list(a.values())
    maximum = max(value, key=value.count)
    return maximum


def count(a: list[str]) -> dict[str, int]:
    """Turns list of str into a dictionary of unique numbers."""
    res: dict[str, int] = dict()
    for key in a:
        if key in res:
            res[key] += 1
        else:
            res[key] = 1
    return res

