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


def operations():
    return {**binary_operators, **unary_operators}


def second_number_required(operator):
    return operator in list(binary_operators.keys())


def unary_calculate(first_number_as_digit, operator):
    if operator == "!":
        result = math.factorial(first_number_as_digit)
    elif operator == "V":
        result = math.sqrt(first_number_as_digit)
    elif operator == "log2x":
        result = math.log2(first_number_as_digit)
    elif operator == "lg":
        result = math.log10(first_number_as_digit)
    else:
        result = "unknown"

    if result == "unknown":
        return "Something went wrong...\n" \
               "Your operator wasn't recognized.\n" \
               "If you want you can try to do this again."
    else:
        return "Your result is: " + str(result)


def binary_calculate(first_number_as_digit, operator, second_number_as_digit):
    if operator == "+":
        result = first_number_as_digit + second_number_as_digit
    elif operator == "-":
        result = first_number_as_digit - second_number_as_digit
    elif operator == "*":
        result = first_number_as_digit * second_number_as_digit
    elif operator == "/":
        result = first_number_as_digit / second_number_as_digit
    elif operator == "**":
        result = first_number_as_digit ** second_number_as_digit
    elif operator == "%":
        result = first_number_as_digit % second_number_as_digit
    else:
        result = "unknown"

    if result == "unknown":
        return "Something went wrong...\n" \
               "Your operator wasn't recognized.\n" \
               "If you want you can try to do this again."
    else:
        return "Your result is: " + str(result)

# Here ends the functions.
