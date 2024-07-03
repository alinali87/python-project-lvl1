import prompt
import random
from brain_games.cli import welcome_user
from brain_games.utils import (make_congratulation_message,
                               make_game_over_message)


ROUNDS_TO_WIN = 3


def make_question() -> (str, str):
    n = random.randint(6, 12)
    start = random.randint(1, 10)
    step = random.randint(1, 7)
    nums = list(range(start, start + n * step + 1, step))
    skip = random.choice(range(n))
    correct_answer = nums[skip]
    nums[skip] = ".."
    question = f"Question: {' '.join(map(str, nums))}"
    return question, str(correct_answer)


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
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
