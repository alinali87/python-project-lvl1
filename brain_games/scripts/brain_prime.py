#!/usr/bin/env python
from brain_games.cli import (
    play_game,
    is_prime
)
from random import randint


def gen_question_brain_prime():
    num = randint(1, 100)
    if is_prime(num):
        return str(num), 'yes'
    return str(num), 'no'


def main():
    play_game('Answer "yes" if given number is prime. Otherwise answer "no".',
              gen_question_brain_prime)


if __name__ == '__main__':
    main()
