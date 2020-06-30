import math
import re


class Operator:
    def __init__(self, symbol, regex, description, can_be_prefix, is_binary, needs_index, calculation):
        self.symbol = symbol
        self.regex = regex
        self.description = description
        self.can_be_prefix = can_be_prefix  # for negative numbers, logarithms and radical (last two
        # also must have needs_index = True)
        self.is_binary = is_binary  # for operators requiring second number (not an index)
        self.needs_index = needs_index  # For radicals, logarithms and powers
        self.calculation = calculation


addition = Operator(symbol="+",
                    regex="\\+",
                    description="addition",
                    can_be_prefix=False,
                    is_binary=True,
                    needs_index=False,
                    calculation=lambda x, y: x + y)
subtraction = Operator(symbol="-",
                       regex="-",
                       description="subtraction",
                       can_be_prefix=True,
                       is_binary=True,
                       needs_index=False,
                       calculation=lambda x, y: x - y)
multiplication = Operator(symbol="*",
                          regex="\\*",
                          description="multiplication",
                          can_be_prefix=False,
                          is_binary=True,
                          needs_index=False,
                          calculation=lambda x, y: x * y)
division = Operator(symbol="/",
                    regex="/",
                    description="division",
                    can_be_prefix=False,
                    is_binary=True,
                    needs_index=False,
                    calculation=lambda x, y: division_calculus(x, y))
exponentiation = Operator(symbol="^[i]",
                          regex="\\^\\[\\d+\\]",
                          description="exponentiation with index i",
                          can_be_prefix=False,
                          is_binary=False,
                          needs_index=True,
                          calculation=lambda x, y: x ** y)
modulus = Operator(symbol="%",
                   regex="%",
                   description="modulus",
                   can_be_prefix=False,
                   is_binary=True,
                   needs_index=False,
                   calculation=lambda x, y: modulus_calculus(x, y))
radical_of_n_index = Operator(symbol="V[n]",
                              regex="V\\[\\d+\\]",
                              description="radical of n-index",
                              can_be_prefix=True,
                              is_binary=False,
                              needs_index=True,
                              calculation=lambda x, y: even_radical(x))  # TODO: make function
factorial = Operator(symbol="!",
                     regex="!",
                     description="factorial",
                     can_be_prefix=False,
                     is_binary=False,
                     needs_index=False,
                     calculation=lambda x, y: factorial_calculus(x))
logarithm_based_on_b = Operator(symbol="log[b]",
                                regex="log\\[\\d+\\]",
                                description="logarithm based on b",
                                can_be_prefix=True,
                                is_binary=False,
                                needs_index=True,
                                calculation=lambda x, y: natural_logarithm(x))
ln = Operator(symbol="ln",
              regex="ln",
              description="natural logarithm",
              can_be_prefix=True,
              is_binary=False,
              needs_index=False,
              calculation=lambda x, y: natural_logarithm(x))
lg = Operator(symbol="lg",
              regex="lg",
              description="logarithm based on 10",
              can_be_prefix=True,
              is_binary=False,
              needs_index=False,
              calculation=lambda x, y: logarithm_based_on_ten(x))

operators_list = {
    addition.symbol: addition,
    subtraction.symbol: subtraction,
    multiplication.symbol: multiplication,
    division.symbol: division,
    exponentiation.symbol: exponentiation,
    modulus.symbol: modulus,
    radical_of_n_index.symbol: radical_of_n_index,
    factorial.symbol: factorial,
    logarithm_based_on_b.symbol: logarithm_based_on_b,
    ln.symbol: ln,
    lg.symbol: lg
}

operators_regex_list = {
    addition.regex: addition,
    subtraction.regex: subtraction,
    multiplication.regex: multiplication,
    division.regex: division,
    exponentiation.regex: exponentiation,
    modulus.regex: modulus,
    radical_of_n_index.regex: radical_of_n_index,
    factorial.regex: factorial,
    logarithm_based_on_b.regex: logarithm_based_on_b,
    ln.regex: ln,
    lg.regex: lg
}


def is_valid_operator(users_operator):
    regexes = list(map(lambda operator: operator.regex, operators_list.values()))
    is_valid = False
    for regex_as_string in regexes:
        regex = re.compile(regex_as_string)
        search_result = regex.search(users_operator)
        is_valid = bool(search_result)
        if is_valid:
            break

    return is_valid


# Next are of the functions, used for operators list and calculating:
def second_number_required(operator_symbol):
    is_binary = None
    for regex_as_string, operator in operators_regex_list.items():
        regex = re.compile(regex_as_string)
        search_result = regex.search(operator_symbol)
        is_valid = bool(search_result)
        if is_valid:
            is_binary = operator.is_binary
            break
    return is_binary


def division_calculus(numerator, divisor):
    try:
        return numerator / divisor
    except Exception:
        raise Exception("You cannot use ", divisor, "as a divisor!")


def factorial_calculus(number):
    try:
        return math.factorial(number)
    except Exception:
        raise Exception("It is possible to get factorial only of integer! "
                        "You must use integer.")


def even_radical(number):
    try:
        return math.sqrt(number)
    except Exception:
        raise Exception("It is impossible to get even radical of negative number!")


def natural_logarithm(number):
    try:
        return math.log(number)
    except Exception:
        raise Exception("You can get logarithm only from number greater than 0 or equal to it!")


def logarithm_based_on_ten(number):
    try:
        return math.log10(number)
    except Exception:
        raise Exception("You can get logarithm only from number greater than 0 or equal to it!")


def modulus_calculus(numerator, divisor):
    try:
        return numerator % divisor
    except Exception:
        raise Exception("You tried to find modulo of division by 0!")


def calculate(first_number_as_digit, operator_symbol, second_number_as_digit):
    operation = operators_list[operator_symbol]
    result = None
    error = None
    try:
        if operators_list[operator_symbol].needs_index:
            second_number_checked = re.sub("[^0-9]", "", operator_symbol)
        else:
            second_number_checked = second_number_as_digit
        result = operation.calculation(first_number_as_digit, second_number_checked)
    except Exception as ex:
        error = str(ex)

    if error is not None:
        return error
    else:
        return result
