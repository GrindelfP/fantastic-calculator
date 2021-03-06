from datetime import datetime

from fantastic_calculator.operators.operators_lists import operators_list


def print_title(version: str) -> print():
    title_text = "\t\t\t\tFANTASTIC CALCULATOR\n" \
                 "\t\t\t\t\t(or just FanC)\n" \
                 "Welcome to the FANTASTIC CALCULATOR version " + str(version) + "!"
    return print(title_text)


def daytime() -> str:
    hour_now = datetime.now().hour

    if 0 <= hour_now < 6:
        daytime_text = 'night'
    elif 6 <= hour_now < 12:
        daytime_text = 'morning'
    elif 12 <= hour_now < 18:
        daytime_text = 'day'
    elif 18 <= hour_now <= 23:
        daytime_text = 'evening'
    else:
        daytime_text = ' - whatever there is at yours - '

    return daytime_text


def print_greetings() -> print():
    daytime_text = daytime()
    name = input("Please, stay calm and print your name: ")
    if not name.strip():
        name = "- whatever your name is"
    greetings_text = 'Good ' + daytime_text

    return print(greetings_text + ", " + name + "!")


def print_instructions() -> None:
    instructions_text_beginning = "Let's do some Math! This calculator can do " \
                                  "following operations:"
    instructions_text_ending = "Please, if your number is decimal, use '.'"

    print(instructions_text_beginning)
    for key, value in operators_list.items():
        print(key, " -> ", value.description)
    print(instructions_text_ending)


def print_intro() -> None:
    print_title("2.0.2")
    print_greetings()
    print_instructions()
