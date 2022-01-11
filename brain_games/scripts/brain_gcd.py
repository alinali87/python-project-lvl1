#!/usr/bin/env python
from brain_games.cli import (
    play_game,
    find_gcd
)
from random import randint


def gen_question_brain_gcd():
    a = randint(1, 100)
    b = randint(1, 100)
    question = f"{a} {b}"
    correct_answer = str(find_gcd(a, b))
    return question, correct_answer


def main():
    play_game('Find the greatest common divisor of given numbers.',
              gen_question_brain_gcd)


if __name__ == '__main__':
    main()
