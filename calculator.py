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


def operations():
    return {**binary_operators, **unary_operators}


def second_number_required(operator):
    return operator in list(binary_operators.keys())
