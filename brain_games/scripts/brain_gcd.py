#!/usr/bin/env python
from brain_games.cli import play_game
from random import randint


def gen_question_brain_gcd():
    a = randint(1, 100)
    b = randint(1, 100)
    question = f"{a} {b}"
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    correct_answer = str(a + b)
    return question, correct_answer


def main():
    play_game('Find the greatest common divisor of given numbers.',
              gen_question_brain_gcd)


if __name__ == '__main__':
    main()
