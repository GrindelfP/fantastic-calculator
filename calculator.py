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


addition = Operator("+",
                    "\\+",
                    "addition",
                    False,
                    True,
                    False,
                    lambda x, y: x + y)
subtraction = Operator("-",
                       "-",
                       "subtraction",
                       True,
                       True,
                       False,
                       lambda x, y: x - y)
multiplication = Operator("*",
                          "\\*",
                          "multiplication",
                          False,
                          True,
                          False,
                          lambda x, y: x * y)
division = Operator("/",
                    "/",
                    "division",
                    False,
                    True,
                    False,
                    lambda x, y: division_calculus(x, y))
exponentiation = Operator("^[i]",
                          "\\^\\[\\d+\\]",
                          "exponentiation with index i",
                          False,
                          False,
                          True,
                          lambda x, y: x ** y)
modulus = Operator("%",
                   "%",
                   "modulus",
                   False,
                   True,
                   False,
                   lambda x, y: modulus_calculus(x, y))
radical_of_n_index = Operator("V[n]",
                              "V\\[\\d+\\]",
                              "radical of n-index",
                              True,
                              False,
                              True,
                              lambda x, y: even_radical(x))  # TODO: make function
factorial = Operator("!",
                     "!",
                     "factorial",
                     False,
                     False,
                     False,
                     lambda x, y: factorial_calculus(x))
logarithm_based_on_b = Operator("log[b]",
                                "log\\[\\d+\\]",
                                "logarithm based on b",
                                True,
                                False,
                                True,
                                lambda x, y: logarithm_based_on_two(x))
ln = Operator("ln",
              "ln",
              "logarithm based on e",
              True,
              False,
              False,
              lambda x, y: logarithm_based_on_two(x))  # TODO: make function ln
lg = Operator("lg",
              "lg",
              "logarithm based on 10",
              True,
              False,
              False,
              lambda x, y: logarithm_based_on_ten(x))

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


def is_valid_operator(users_operator):
    regexes = list(map(lambda operator: operator.regex, operators_list.values()))
    is_valid = False
    for regex in regexes:
        search = re.compile(regex).search(users_operator)
        is_valid = bool(search)

    return is_valid


# Next are of the functions, used for operators list and calculating:
def second_number_required(operator_symbol):
    operation = operators_list[operator_symbol]
    return operation.is_binary


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


def logarithm_based_on_two(number):
    try:
        return math.log2(number)
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
        result = operation.calculation(first_number_as_digit, second_number_as_digit)
    except Exception as ex:
        error = str(ex)

    if error is not None:
        return error
    else:
        return result

# Here ends the functions.
