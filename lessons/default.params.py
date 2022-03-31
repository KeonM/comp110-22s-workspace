"""Examples of default paramteres"""


def add(x: int, y: int = 0, z: int = 0) -> int:
    """Defalt parameters give more flexibility S"""
    return x + y


print(add(1))
print(add(1, 2))
print(add(1, 2 , 3))