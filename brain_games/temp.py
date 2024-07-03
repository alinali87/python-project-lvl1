def welcome_user():
    import prompt
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def start_game(text):
    print(text)


def congratulate(name):
    print(f'Congratulations, {name}!')


def game_over(name, answer, correct_answer):
    if answer != correct_answer:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")


def play_game(start_text, gen_question):
    name = welcome_user()
    start_game(start_text)
    counter = 0
    while counter < 3:
        question, correct_answer = gen_question()
        print(f"Question: {question}")
        answer = input('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            game_over(name, answer, correct_answer)
            return
    congratulate(name)


def find_gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True
