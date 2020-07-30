from fantastic_calculator.operators import operators_lists
import re


def is_valid_operator(users_operator: str) -> bool:
    regexes = list(map(lambda operator: operator.regex, operators_lists.operators_list.values()))
    is_valid = False
    for regex_as_string in regexes:
        regex = re.compile(regex_as_string)
        if regex.fullmatch(users_operator):
            is_valid = True
            break

    return is_valid


def second_number_required(operator_symbol: str) -> bool:
    is_binary = None
    for regex_as_string, operator in operators_lists.operators_regex_list.items():
        regex = re.compile(regex_as_string)
        if regex.fullmatch(operator_symbol):
            is_binary = operator.is_binary

    return is_binary
