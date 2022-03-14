"""Dictionary test!"""
__author__ = "730476939"


from dictionary import invert, favorite_color, count


def test_invert_one() -> None:
    """Invert test one."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}

    
def test_invert_two() -> None:
    """Invert test two."""
    xs: dict[str, str] = {'apple': 'cat'}
    assert invert(xs) == {'cat': 'apple'}


def test_invert_three() -> None:
    """Invert test three."""
    xs: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
    assert invert(xs) == {'jordan': 'michael'}
    
    
def test_favorite_color_one() -> None:
    """Favorite_color test one."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_two() -> None:
    """Favorite_color test two."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "red", "Kris": "blue"}
    assert favorite_color(xs) == "yellow"
    
    
def test_favorite_color_three() -> None:
    """Favorite_color test three."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "yellow", "Kris": "blue", "Bob": "Green"}
    assert favorite_color(xs) == "yellow"
    

def test_count_one() -> None:
    """Count test one."""
    xs: list[str] = ['hi', 'hi', 'hi', 'bye', 'bye', 'hola']
    assert count(xs) == {'hi': 3, 'bye': 2, 'hola': 1}
    

def test_count_two() -> None:
    """Count test two."""
    xs: list[str] = ['hi', 'hello', 'computer', 'phone', 'price']
    assert count(xs) == {'hi': 1, 'hello': 1, 'computer': 1, 'phone': 1, 'price': 1}
    

def test_count_three() -> None:
    """Count test three."""
    xs: list[str] = ['trail']
    assert count(xs) == {'trail': 1}