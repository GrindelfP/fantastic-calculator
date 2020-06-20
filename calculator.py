import math


class Operator:
    def __init__(self, symbol, description, can_be_prefix, is_binary, needs_index):
        self.symbol = symbol
        self.description = description
        self.can_be_prefix = can_be_prefix  # for negative numbers, logarithms and radical (last two
        # also must have needs_index = True)
        self.is_binary = is_binary  # for operators requiring second number (not an index)
        self.needs_index = needs_index  # For radicals, logarithms and powers


addition = Operator("+",
                    "addition",
                    False,
                    True,
                    False)
subtraction = Operator("-",
                       "subtraction",
                       True,
                       True,
                       False)
multiplication = Operator("*",
                          "multiplication",
                          False,
                          True,
                          False)
division = Operator("/",
                    "division",
                    False,
                    True,
                    False)
exponentiation = Operator("^",
                          "exponentiation",
                          False,
                          False,
                          True)
modulus = Operator("%",
                   "modulus",
                   False,
                   True,
                   False)
radical_of_n_index = Operator("V[n]",
                              "radical of n-index",
                              True,
                              False,
                              True)
factorial = Operator("!",
                     "factorial",
                     False,
                     False,
                     False)
logarithm_based_on_b = Operator("log[b]",
                                "logarithm based on b",
                                True,
                                False,
                                True)
ln = Operator("ln",
              "logarithm based on e",
              True,
              False,
              False)
lg = Operator("ln",
              "logarithm based on 10",
              True,
              False,
              False)


operators_list = {
    addition.symbol: addition.description,
    subtraction.symbol: subtraction.description,
    multiplication.symbol: multiplication.description,
    division.symbol: division.description,
    exponentiation.symbol: exponentiation.description,
    modulus.symbol: modulus.description,
    radical_of_n_index.symbol: radical_of_n_index.description,
    factorial.symbol: factorial.description,
    logarithm_based_on_b.symbol: logarithm_based_on_b.description,
    ln.symbol: ln.description,
    lg.symbol: lg.description
}


# Next are of the functions, used for operators list and calculating:
def second_number_required(operator):
    return operator.is_binary


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


def calculate(first_number_as_digit, operator, second_number_as_digit):
    result = None
    error = None
    try:
        if operator == "!":
            result = factorial_calculus(first_number_as_digit)
        elif operator == "V":
            result = even_radical(first_number_as_digit)
        elif operator == "log2x":
            result = logarithm_based_on_two(first_number_as_digit)
        elif operator == "lg":
            result = logarithm_based_on_ten(first_number_as_digit)
        elif operator == "+":
            result = first_number_as_digit + second_number_as_digit
        elif operator == "-":
            result = first_number_as_digit - second_number_as_digit
        elif operator == "*":
            result = first_number_as_digit * second_number_as_digit
        elif operator == "/":
            result = division_calculus(first_number_as_digit, second_number_as_digit)
        elif operator == "**":
            result = first_number_as_digit ** second_number_as_digit
        elif operator == "%":
            result = modulus_calculus(first_number_as_digit, second_number_as_digit)
        else:
            error = "Your operator wasn't recognized."
    except Exception as ex:
        error = str(ex)

    if error is not None:
        return error
    else:
        return result

# Here ends the functions.
