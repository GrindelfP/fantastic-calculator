import math
from datetime import datetime


def print_title(version):
    title_text = "\t\t\t\tFANTASTIC CALCULATOR\n" \
                 "\t\t\t\t\t(or just FanC)\n" \
                 "Welcome to the FANTASTIC CALCULATOR version " + str(version) + "!"
    print(title_text)


def daytime():
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


def greetings():
    daytime_text = daytime()
    name = input("Please, stay calm and print your name: ")
    greetings_text = 'Good ' + daytime_text
    return greetings_text + ", " + name + "!"


def print_instructions():
    instructions_text = "Let's do some Math! This calculator can do " \
                        "following operations:\n" \
                        "+ -> addition\n" \
                        "- -> subtraction\n" \
                        "* -> multiplication\n" \
                        "/ -> division\n" \
                        "** -> exponentiation\n" \
                        "V -> square root\n" \
                        "% -> modulus\n" \
                        "! -> factorial\n" \
                        "log2x -> logarithm based on 2\n" \
                        "lg -> logarithm based on 10\n" \
                        "Please, if your number is decimal, use '.'"
    print(instructions_text)


def to_number(number_as_text):
    if "." in number_as_text:
        number_as_digit = float(number_as_text)
    else:
        number_as_digit = int(number_as_text)

    return number_as_digit


def get_number(place_of_number):
    number = input("Put here your " + place_of_number + " number -> |")
    while number.count("-") > 1 or number.count(".") > 1 or \
            not number.replace(".", "").replace("-", "").isdigit():
        number = input("Are you sure, that you printed a number? "
                       "Try again! Put here your first number -> |")

    return to_number(number)


# Here starts the program
print_title("0.1")

print(greetings())

print_instructions()

should_be_stopped = False

operators = "+ - * / ** V % ! log2x lg"

while not should_be_stopped:
    first_number_as_digit = get_number("first")

    operator = input("Choose one of this operators: " + operators + " -> |")

    # TODO check operator if f_n is negative

    while operator not in operators or operator == " ":
        operator = input("Sadly, this operator is unsupported by FanC! Did you choose one of given operators? "
                         "Try some of them again!"
                         "Choose one of this operators: " + operators + " -> |")

    while first_number_as_digit < 0 and operator == "!" or first_number_as_digit < 0 and operator == "V" or \
            first_number_as_digit < 0 and operator == "log2x" or first_number_as_digit < 0 and operator == "lg":
        first_number = input("It is impossible to do this operation with negative numbers. "
                             "Put here a positive one -> |")
        if "." in first_number:
            first_number_as_digit = float(first_number)
        else:
            first_number_as_digit = int(first_number)

    if operator != "!" and operator != "V" and operator != "log2x" and operator != "lg":
        second_number = get_number("second")
    # Here ends the input.

    # Next lines are of the MATH:
    if operator == "!":
        print("Your result is: " + str(math.factorial(first_number_as_digit)))
    elif operator == "V":
        print("Your result is: " + str(math.sqrt(first_number_as_digit)))
    elif operator == "log2x":
        print("Your result is: " + str(math.log2(first_number_as_digit)))
    elif operator == "lg":
        print("Your result is: " + str(math.log10(first_number_as_digit)))
    elif operator == "+":
        # noinspection PyUnboundLocalVariable
        print("Your result is: " + str(first_number_as_digit + second_number_as_digit))
    elif operator == "-":
        print("Your result is: " + str(first_number_as_digit - second_number_as_digit))
    elif operator == "*":
        print("Your result is: " + str(first_number_as_digit * second_number_as_digit))
    elif operator == "/":
        print("Your result is: " + str(first_number_as_digit / second_number_as_digit))
    elif operator == "**":
        print("Your result is: " + str(first_number_as_digit ** second_number_as_digit))
    elif operator == "%":
        print("Your result is: " + str(first_number_as_digit % second_number_as_digit))
    else:
        print("Something went wrong...\n"
              "Your operator wasn't recognized.\n"
              "If you want you can try to do this again.")
    # Here ends the MATH. Next lines are of exit opportunity:

    x = input("Do you want to continue calculating? (Y/N): ")
    if x == "N":
        should_be_stopped = True

# Here ends exit opportunity. It is the end of the code.
