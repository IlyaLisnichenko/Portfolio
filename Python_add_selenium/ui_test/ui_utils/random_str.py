import random
from string import ascii_letters


def random_str(int_len: int = 10) -> str:
    return "".join(random.choices(ascii_letters, k=int_len))
