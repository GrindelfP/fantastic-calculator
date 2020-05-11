from datetime import datetime
import calculator

# Next lines are of functions, used in user-input-1:


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
    if not name.strip():
        name = "- whatever your name is"
    greetings_text = 'Good ' + daytime_text
    return greetings_text + ", " + name + "!"


def print_instructions():
    instructions_text_beginning = "Let's do some Math! This calculator can do " \
                                  "following operations:"
    instructions_text_ending = "Please, if your number is decimal, use '.'"

    print(instructions_text_beginning)
    operations_map = calculator.operations()
    for key, value in operations_map.items():
        print(key, " -> ", value)
    print(instructions_text_ending)


def to_number(number_as_text):
    if "." in number_as_text:
        number_as_digit = float(number_as_text)
    else:
        number_as_digit = int(number_as_text)

    return number_as_digit


def get_number_input(original_prompt):
    number = input(original_prompt)
    while number.count("-") > 1 or number.count(".") > 1 or \
            not number.replace(".", "").replace("-", "").isdigit():
        number = input("Are you sure, that you printed a number? "
                       "Try again! Put here your first number -> |")

    return to_number(number)


def get_operator_input():
    operators = list(calculator.operations().keys())
    operators_as_string = " "
    operators_as_string = operators_as_string.join(operators)
    operator_input = input("Choose one of this operators: " + operators_as_string + " -> |")

    while operator_input not in operators:
        operator_input = input("Sadly, this operator is unsupported by FanC! Did you choose one of given operators? "
                               "Try some of them again!"
                               "Choose one of this operators: " + operators_as_string + " -> |")
    return operator_input


def exit_prompt():
    to_be_stopped = False
    exit_request = input("Do you want to continue calculating? (Y/N): ").upper()
    while exit_request != "N" and exit_request != "Y":
        exit_request = input("I didn't understand you. Please, type 'Y' or 'N' for 'Yes' and 'No' (Y/N): ").upper()

    if exit_request == "N":
        to_be_stopped = True
        print("Good bye!")

    return to_be_stopped


# Here ends lines of functions, used in user-input-1. In next lines starts the program:
# Here begins the greetings:
print_title("0.2.0")

print(greetings())

print_instructions()
# Here ends the greetings. Next lines are of the input:

should_be_stopped = False

while not should_be_stopped:
    first_number_as_digit = get_number_input("Put here your first number -> |")

    operator = get_operator_input()
    # Here ends the input. Next lines are of the calculating:

    if calculator.second_number_required(operator):
        second_number_as_digit = get_number_input("Put here your second number -> |")

        print(calculator.binary_calculate(first_number_as_digit, operator, second_number_as_digit))

    else:
        while first_number_as_digit < 0 and operator == "!" or first_number_as_digit < 0 and operator == "V":
            first_number_as_digit = get_number_input("It is impossible to do this operation with negative numbers. "
                                                     "Put here a positive one -> |")
        while first_number_as_digit <= 0 and operator == "log2x" or first_number_as_digit <= 0 and operator == "lg":
            first_number_as_digit = get_number_input("It is impossible to do this operation with numbers "
                                                     "less or equal to 0. "
                                                     "Put here a positive one -> |")
        print(calculator.unary_calculate(first_number_as_digit, operator))
    # Here ends the calculating. Next lines are of the exit opportunity:

    should_be_stopped = exit_prompt()
# Here ends the exit opportunity. Here ends the program.
