"""Union typoe fives flexibity to single vars."""

from typing import Union

def log(info: Union[str, int]) -> None:
    if isinstance(info, str):
        print(f"str: {info}")
    else:
        print(f"int: {info}")
        
log("help")
log(110)