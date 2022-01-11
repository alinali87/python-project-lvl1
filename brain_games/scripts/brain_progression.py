#!/usr/bin/env python
from brain_games.cli import (
    play_game
)
from random import (
    randint,
    choice
)


def gen_question_brain_progression():
    start = randint(1, 10)
    step = randint(1, 5)
    end = start + step * 8
    sequence = list(map(str, range(start, end, step)))
    missing = choice(sequence)
    question = ' '.join(sequence).replace(missing, '..')
    correct_answer = missing
    return question, correct_answer


def main():
    play_game('What number is missing in the progression?',
              gen_question_brain_progression)


if __name__ == '__main__':
    main()
