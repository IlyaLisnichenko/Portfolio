import random
from string import ascii_lowercase, digits


def random_str(int_len: int = None) -> str:
    return _random_choices(population=ascii_lowercase, int_len=int_len).capitalize()


def random_int(int_len: int = 3) -> str:
    result = _random_choices(population=digits.replace("0", ""), int_len=1)
    result += _random_choices(population=digits, int_len=int_len - 1)
    return result


def _random_choices(population: str, int_len: int = None) -> str:
    str_len = int_len or random.randrange(7, 13)
    return "".join(random.choices(population, k=str_len))
