"""Utils test in ex05."""
__author__ = "730476939"


from utils import only_evens, sub, concat


def test_only_evens_one() -> None:
    """Only even test one."""
    xs: list[int] = []
    only_evens(xs) == [1, 2, 3, 4]

    
def test_only_evens_two() -> None:
    """Only even test two."""
    xs: list[int] = []
    only_evens(xs) == [12, 2345, 53, 345]
    
    
def test_only_evens_three() -> None:
    """Only even test three."""
    xs: list[int] = []
    only_evens(xs) == [0]
    

def test_sub_one() -> None:
    """Sub test one."""
    xs: list[int] = []
    sub(xs, 1, 3) == [1, 2, 3, 4, 5, 6]


def test_sub_two() -> None:
    """Sub test two."""
    xs: list[int] = []
    sub(xs, 1, 3215) == [1, 2, 3, 4, 5, 6]


def test_sub_three() -> None:
    """Sub test three."""
    xs: list[int] = []
    sub(xs, 1, 4) == []


def test_concat_one() -> None:
    """Concat test one."""
    xs: list[int] = [1, 2, 34, 5, 6]
    ys: list[int] = [3, 4, 5, 6]
    concat(xs, ys)
    
    
def test_concat_two() -> None:
    """Concat test two."""
    xs: list[int] = []
    ys: list[int] = [3, 4, 5, 6]
    concat(xs, ys)
    

def test_concat_three() -> None:
    """Concat test three."""
    xs: list[int] = [12, 124, 53]
    ys: list[int] = [3, 4, 5, 6, 5, 7, 7, 8]
    concat(xs, ys)