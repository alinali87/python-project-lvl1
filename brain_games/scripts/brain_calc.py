import prompt
import random
from operator import add, sub, mul
from brain_games.cli import welcome_user
from brain_games.utils import (make_congratulation_message,
                               op_to_string, make_game_over_message)


ROUNDS_TO_WIN = 3


def make_question() -> (str, str):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice([add, sub, mul])
    correct_answer = op(num1, num2)
    question = f"Question: {num1} {op_to_string(op)} {num2}"
    return question, str(correct_answer)


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    correct = 0
    while correct < ROUNDS_TO_WIN:
        question, correct_answer = make_question()
        print(question)
        answer = prompt.string("Your answer: ")
        if answer == correct_answer:
            correct += 1
            print("Correct!")
        else:
            game_over = make_game_over_message(name=name, answer=answer,
                                               correct_answer=correct_answer)
            print(game_over)
            return
    congratulation = make_congratulation_message(name)
    print(congratulation)


if __name__ == '__main__':
    main()
