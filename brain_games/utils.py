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
