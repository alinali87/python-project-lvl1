import prompt


def welcome_user() -> str:
    """ Print welcome prompt and wait for user to enter their name.
        Greet the user.

     Returns:
        str: name of the user
     """
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    return name
