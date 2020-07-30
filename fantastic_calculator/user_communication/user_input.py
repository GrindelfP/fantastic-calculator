from fantastic_calculator.operators import operators_lists
from fantastic_calculator.checking import oerator_checking


def to_number(number_as_text: str) -> int or float:
    if "." in number_as_text:
        number_as_digit = float(number_as_text)
    else:
        number_as_digit = int(number_as_text)

    return number_as_digit


def get_number_input(original_prompt: str) -> int or float:
    number = input(original_prompt)
    while number.count("-") > 1 or number.count(".") > 1 or not number.replace(".", "").replace("-", "").isdigit():
        number = input("Are you sure, that you printed a number? Try again! Put here your first number -> |")

    return to_number(number)


def get_operator_input() -> str:
    operators = list(operators_lists.operators_list.keys())
    operators_as_string = " ".join(operators)
    operator_input = input("Choose one of this operators: " + operators_as_string + " -> |")
    while not oerator_checking.is_valid_operator(operator_input):
        operator_input = input("Sadly, this operator is unsupported by FanC! Did you choose one of given operators? "
                               "Try some of them again! "
                               "Choose one of this operators: " + operators_as_string + " -> |")

    return operator_input
