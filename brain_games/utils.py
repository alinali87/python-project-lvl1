from typing import Callable
import operator


def congrat_user(name: str):
    """ Congrats if the user wins the game

    Args:
        name: name of the user
    """
    print(f"Congratulations, {name}!")


def op_to_string(op: Callable) -> str:
    """ Produce the string representing an arithmetic operation
        add: "+"
        sub: "-"
        mul: "*"
        truediv: "/"
    """
    mapping = {
        operator.add: "+",
        operator.sub: "-",
        operator.mul: "*",
        operator.truediv: "/",
    }
    return mapping[op]


def is_prime(n):
    """ Return true if the given number is prime, false otherwise """
    if n == 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True
