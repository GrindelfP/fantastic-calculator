import math
from datetime import datetime

# Next lines are of the greetings:

print("               FANTASTIC CALCULATOR")
print("                 (or just FanC)")
print('Welcome to the FANTASTIC CALCULATOR!')
name = input("Please, stay calm and print your name: ")

daytime = 'unknown daytime'
hour_now = datetime.now().hour

if 0 <= hour_now < 6:
    daytime = 'night'
elif 6 <= hour_now < 12:
    daytime = 'morning'
elif 12 <= hour_now < 18:
    daytime = 'day'
elif 18 <= hour_now <= 23:
    daytime = 'evening'
else:
    daytime = ' - whatever there is at yours - '

hay = 'Good ' + daytime

print(hay + ', ' + name + '!')
# Here ends the greetings. Next lines are description of calculating:

print("Let's do some Math! This calculator can do following operations:\n"
      "+ -> addition\n"
      "- -> subtraction\n"
      "* -> multiplication\n"
      "/ -> division\n"
      "** -> exponentiation\n"
      "V -> square root\n"
      "% -> modulus\n"
      "! -> factorial"
      "Please, if your number is decimal, use '.'")
# Here ends description of calculating.

# Next lines are of input:
should_be_stopped = False

operators = "+ - * / ** V % !"

while not should_be_stopped:
    first_number = input("Put here your first number -> |")
    while first_number.count("-") > 1 or first_number.count(".") > 1 or \
            not first_number.replace(".", "").replace("-", "").isdigit():
        first_number = input("Are you sure, that you printed a number? "
                             "Try again! Put here your first number -> |")
    first_number_as_digit = 0
    if "." in first_number:
        first_number_as_digit = float(first_number)
    else:
        first_number_as_digit = int(first_number)

    operator = input("Choose one of this operators: " + operators + " -> |")

    # TODO check operator if f_n is negative

    while operator not in operators or operator == " ":
        operator = input("Sadly, this operator is unsupported by FanC! Did you choose one of given operators? "
                         "Try some of them again!"
                         "Choose one of this operators: " + operators + " -> |")

    while first_number.count("-") > 0 and operator == "!" or first_number.count("-") > 0 and operator == "V":
        first_number = input("It is impossible to do this operation with negative numbers. "
                             "Put here a positive one -> |")
        if "." in first_number:
            first_number_as_digit = float(first_number)
        else:
            first_number_as_digit = int(first_number)

    if not operator == "!" and not operator == "V":
        second_number = input("Put here your second number -> |")
        while second_number.count("-") > 1 or second_number.count(".") > 1 or \
                not second_number.replace(".", "").replace("-", "").isdigit():
            second_number = input("Are you sure, that you printed a number? "
                                  "Try again! Put here your first number -> |")

        second_number_as_digit = 0
        if "." in second_number:
            second_number_as_digit = float(second_number)
        else:
            second_number_as_digit = int(second_number)
    # Here ends the input.

    # Next lines are of the MATH:
    if operator == "!":
        print("Your result is: " + str(math.factorial(first_number_as_digit)))
    elif operator == "V":
        print("Your result is: " + str(math.sqrt(first_number_as_digit)))
    elif operator == "+":
        # noinspection PyUnboundLocalVariable
        print("Your result is: " + str(first_number_as_digit + second_number_as_digit))
    elif operator == "-":
        print("Your result is: " + str(first_number_as_digit - second_number_as_digit))
    elif operator == "*":
        print("Your result is: " + str(first_number_as_digit * second_number_as_digit))
    elif operator == "/":
        print("Your result is: " + str(first_number_as_digit / second_number_as_digit))
    elif operator == "**":
        print("Your result is: " + str(first_number_as_digit ** second_number_as_digit))
    elif operator == "%":
        print("Your result is: " + str(first_number_as_digit % second_number_as_digit))
    else:
        print("Something went wrong...\n"
              "Your operator wasn't recognized.\n"
              "If you want you can try to do this again.")
    # Here ends the MATH. Next lines are of exit opportunity:

    x = input("Do you want to continue calculating? (Y/N): ")
    if x == "N":
        should_be_stopped = True
# Here ends exit opportunity. It is the end of the code.
