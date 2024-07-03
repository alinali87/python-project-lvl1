import prompt
import random
from brain_games.cli import welcome_user
from brain_games.utils import congrat_user, game_over


ROUNDS_TO_WIN = 3


def generate_question():
    num = random.randint(1, 100)
    correct_answer = "yes" if num % 2 == 0 else "no"
    return num, correct_answer


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct = 0
    while correct < ROUNDS_TO_WIN:
        num, correct_answer = generate_question()
        print(f"Question: {num}")
        answer = prompt.string("Your answer: ")
        if answer == correct_answer:
            print("Correct!")
            correct += 1
        else:
            game_over(name, answer, correct_answer)
            return
    congrat_user(name)


if __name__ == '__main__':
    main()
