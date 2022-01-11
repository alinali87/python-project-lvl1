#!/usr/bin/env python
from brain_games.cli import (
    welcome_user,
    start_game,
    congratulate,
    game_over,
    play_game
)
from random import (
    randint,
    choice
)
import operator


def gen_question_brain_calc():
    ops = [(operator.add, '+'), (operator.sub, '-'), (operator.mul, '*')]
    op = choice(ops)
    a = randint(1, 100)
    b = randint(1, 100)
    question = f"{a} {op[1]} {b}"
    correct_answer = str(op[0](a, b))
    return question, correct_answer


def main():
    play_game('What is the result of the expression?', gen_question_brain_calc)


if __name__ == '__main__':
    main()
