from fantastic_calculator.operators.operators_lists import operators_list, operators_regex_list
import re


def calculate(first_number_as_digit, operator_symbol, second_number_as_digit):
    result = None
    error = None
    regexes = list(map(lambda operator: operator.regex, operators_list.values()))
    operator_checked = None
    for regex_as_string in regexes:
        regex = re.compile(regex_as_string)
        search_result = regex.fullmatch(operator_symbol)
        if bool(search_result):
            operator_checked = operators_regex_list[regex_as_string]
            break

    try:
        if operator_checked.needs_index:
            second_number_checked = float(re.sub("[^0-9.-]", "", operator_symbol))
        else:
            second_number_checked = second_number_as_digit
        result = operator_checked.calculation(first_number_as_digit, second_number_checked)
    except Exception as ex:
        error = str(ex)

    if error is not None:
        return error
    else:
        return result
