#!/usr/bin/env python
from brain_games.temp import play_game
from random import randint


def gen_question_brain_even():
    num = randint(1, 100)
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return num, correct_answer


def main():
    play_game('Answer "yes" if the number is even, otherwise answer "no".',
              gen_question_brain_even)


if __name__ == '__main__':
    main()
