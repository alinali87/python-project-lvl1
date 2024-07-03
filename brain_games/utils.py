from typing import Callable
import operator


def make_congratulation_message(name: str) -> str:
    """ Return congratulation message

    Args:
        name: name of the user
    """
    return f"Congratulations, {name}!"


def make_game_over_message(name: str, answer: str, correct_answer: str) -> str:
    """ Return game over message

    Args:
        name: name of the user
        answer: user's answer
        correct_answer: correct answer
    """
    message = f"'{answer}' is wrong answer ;(. " \
              f"Correct answer was '{correct_answer}'.\n"\
              f"Let's try again, {name}!"
    return message


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
