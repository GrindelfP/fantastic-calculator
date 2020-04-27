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
      "! -> factorial")
# Here ends description of calculating. Next lines are of input:

should_be_stopped = False

operators = "+ - * / ** V % !"

while not should_be_stopped:
    first_number = input("Put here your first number -> |")
    while not first_number.isdigit():
        first_number = input("Are you sure, that you printed a number? "
                             "Try again! Put here your first number -> |")

    operator = input("Choose one of this operators: " + operators + " -> |")

    while operator not in operators:
        operator = input("Sadly, this operator is unsupported by FanC! Did you choose one of given operators? "
                         "Try some of them again!"
                         "Choose one of this operators: " + operators + " -> |")

    second_number = "nothing special"

    if operator != "!" and operator != "V":
        second_number = input("Put here your second number -> |")
        while not second_number.isdigit():
            second_number = input("Are you sure, that you printed a number? "
                                  "Try again! Put here your second number -> |")

    print("calculating...")
    # Here ends the input. Next lines are of the MATH:

    if operator == "!":
        print("Your result is: " + str(math.factorial(int(first_number))))
    elif operator == "V":
        print("Your result is: " + str(math.sqrt(int(first_number))))
    elif operator == "+":
        print("Your result is: " + str(int(first_number) + int(second_number)))
    elif operator == "-":
        print("Your result is: " + str(int(first_number) - int(second_number)))
    elif operator == "*":
        print("Your result is: " + str(int(first_number) * int(second_number)))
    elif operator == "/":
        print("Your result is: " + str(int(first_number) / int(second_number)))
    elif operator == "**":
        print("Your result is: " + str(int(first_number) ** int(second_number)))
    else:
        print("Your result is: " + str(int(first_number) % int(second_number)))
    # Here ends the MATH. Next lines are of exit opportunity:

    x = input("Do you want to continue calculating? (Y/N): ")
    if x == "N":
        should_be_stopped = True
# Here ends exit opportunity. It is the end of the code.
