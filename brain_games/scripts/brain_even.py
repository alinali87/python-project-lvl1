import prompt
import random
from brain_games.cli import welcome_user
from brain_games.utils import (make_congratulation_message,
                               make_game_over_message)


ROUNDS_TO_WIN = 3


def make_question() -> (str, str):
    num = random.randint(1, 100)
    correct_answer = "yes" if num % 2 == 0 else "no"
    question = f"Question: {num}"
    return question, correct_answer


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct = 0
    while correct < ROUNDS_TO_WIN:
        question, correct_answer = make_question()
        print(question)
        answer = prompt.string("Your answer: ")
        if answer == correct_answer:
            print("Correct!")
            correct += 1
        else:
            game_over = make_game_over_message(name=name, answer=answer,
                                               correct_answer=correct_answer)
            print(game_over)
            return
    congratulation = make_congratulation_message(name)
    print(congratulation)


if __name__ == '__main__':
    main()
