import math


def addition_calculus(augend: int or float, addend: int or float) -> int or float:
    return augend + addend


def subtraction_calculus(minuend: int or float, subtrahend: int or float) -> int or float:
    return minuend - subtrahend


def multiplication_calculus(multiplier: int or float, multiplicand: int or float) -> int or float:
    return multiplier * multiplicand


def division_calculus(numerator: int or float, divisor: int or float) -> int or float or str:
    try:
        return numerator / divisor
    except Exception:
        raise Exception("You cannot use ", divisor, "as a divisor!")


def exponentiation_calculus(base: int or float, exponent: int or float) -> int or float:
    return base ** exponent


def factorial_calculus(number: int) -> int or str:
    try:
        return math.factorial(number)
    except Exception:
        raise Exception("It is possible to get factorial only of integer! "
                        "You must use integer.")


def radical(radicand: int or float, degree: int or float) -> int or float or str:
    try:
        return radicand ** (1 / degree)
    except Exception:
        raise Exception("It is impossible to get even radical of negative number!")


def logarithm_based_ob_b(anti_logarithm: int or float, base: int or float) -> int or float or str:
    try:
        return math.log(anti_logarithm, base)
    except Exception:
        raise Exception("You can get logarithm only from number greater than 0 or equal to it!")


def natural_logarithm(anti_logarithm: int or float) -> int or float or str:
    try:
        return math.log(anti_logarithm)
    except Exception:
        raise Exception("You can get logarithm only from number greater than 0 or equal to it!")


def logarithm_based_on_ten(anti_logarithm: int or float) -> int or float or str:
    try:
        return math.log10(anti_logarithm)
    except Exception:
        raise Exception("You can get logarithm only from number greater than 0 or equal to it!")


def modulus_calculus(numerator: int or float, divisor: int or float) -> int or float or str:
    try:
        return numerator % divisor
    except Exception:
        raise Exception("You tried to find modulo of division by 0!")
