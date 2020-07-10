from fantastic_calculator.calculation.calculation import calculate
from fantastic_calculator.checking import oerator_checking
from fantastic_calculator.user_communication import user_input


def exit_prompt():
    to_be_stopped = False
    exit_request = input("Do you want to continue calculating? (Y/N): ").upper()
    while exit_request != "N" and exit_request != "Y":
        exit_request = input("I didn't understand you. Please, type 'Y' or 'N' for 'Yes' and 'No' (Y/N): ").upper()

    if exit_request == "N":
        to_be_stopped = True
        print("Good bye!")

    return to_be_stopped


def perform_calculation():
    should_be_stopped = False
    while not should_be_stopped:
        first_number_as_digit = user_input.get_number_input("Put here your first number -> |")
        user_operator = user_input.get_operator_input()
        second_number_as_digit = None
        if oerator_checking.second_number_required(user_operator):
            second_number_as_digit = user_input.get_number_input("Put here your second number -> |")
        print("Your result is -> ", str(calculate(first_number_as_digit, user_operator,
                                                  second_number_as_digit)))
        should_be_stopped = exit_prompt()
