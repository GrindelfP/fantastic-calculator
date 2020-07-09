import math


def addition_calculus(numerator, divisor):
    return numerator + divisor


def subtraction_calculus(numerator, divisor):
    return numerator - divisor


def multiplication_calculus(numerator, divisor):
    return numerator * divisor


def division_calculus(numerator, divisor):
    try:
        return numerator / divisor
    except Exception:
        raise Exception("You cannot use ", divisor, "as a divisor!")


def exponentiation_calculus(numerator, divisor):
    return numerator ** divisor


def factorial_calculus(number):
    try:
        return math.factorial(number)
    except Exception:
        raise Exception("It is possible to get factorial only of integer! "
                        "You must use integer.")


def radical(number, power):
    try:
        return number ** (1 / power)
    except Exception:
        raise Exception("It is impossible to get even radical of negative number!")


def logarithm_based_ob_b(number, base):
    try:
        return math.log(number, base)
    except Exception:
        raise Exception("You can get logarithm only from number greater than 0 or equal to it!")


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
