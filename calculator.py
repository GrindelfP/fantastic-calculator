import math

# Next two variables are the lists of operators:
binary_operators = {
    "+": "addition",
    "-": "subtraction",
    "*": "multiplication",
    "/": "division",
    "**": "exponentiation",
    "%": "modulus"
}

unary_operators = {
    "V": "square root",
    "!": "factorial",
    "log2x": "logarithm based on 2",
    "lg": "logarithm based on 10"
}


# Here ends two variables are the lists of operators.
# Next are of the functions, used for operators list and calculating:


operations = {**binary_operators, **unary_operators}


def second_number_required(operator):
    return operator in list(binary_operators.keys())


def division(numerator, divisor):
    try:
        return numerator / divisor
    except Exception:
        raise Exception("You cannot use ", divisor, "as a divisor!")


def factorial(number):
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


def modulus(numerator, divisor):
    try:
        return numerator % divisor
    except Exception:
        raise Exception("You tried to find modulo of division by 0!")


def calculate(first_number_as_digit, operator, second_number_as_digit):
    result = None
    error = None
    try:
        if operator == "!":
            result = factorial(first_number_as_digit)
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
            result = division(first_number_as_digit, second_number_as_digit)
        elif operator == "**":
            result = first_number_as_digit ** second_number_as_digit
        elif operator == "%":
            result = modulus(first_number_as_digit, second_number_as_digit)
        else:
            error = "Your operator wasn't recognized."
    except Exception as ex:
        error = str(ex)

    if error is not None:
        return error
    else:
        return result

# Here ends the functions.
