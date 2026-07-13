from typing import List, Tuple, Dict, Union

# List integer
number : list[int] = [1, 3, 5, 6]

# tuple of a string and an interger
person : tuple[str, int] = ("Alice", 34)

# Dictonary with string key and integer value
scores = dict[str, int] = {"Alice": 90, "bob": 20}

# Union type for variables that can hold multiple types
identifier: Union[str, int] = "ID986"
identifier = 1213 # Also valid


n : int = 5

name : str = "Ajay"


def sum(a: int, b : int) -> int:
    return (a+b)

a = sum(2, 4)
print(a)