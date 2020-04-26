import math
from datetime import datetime

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
# Here ends the greetings. Next lines are of calculating:

print("Let's do some Math! This calculator can do following operations:\n"
      "+ -> addition\n"
      "- -> subtraction\n"
      "") # TODO: add all operators and instructions for user (ye can do op. by...)

should_be_stopped = False

operators = "+ - * / ** V % !"

while not should_be_stopped:
    first_number = input("Put here your first number -> |")
    # TODO Work on variant, when the f_n (also s_n) isn't integer (anything except float)
    # TODO Work on variant, when the f_n (also s_n) is't integer (float)
    # TODO Also for s_n
    operator = input("Choose one of this operators: " + operators + " -> |")
    while operator not in operators:
        operator = input("Sadly, this operator is unsupported by FanC! Did you choose one of given operators? "
                         "Try some of them again!"
                         "Choose one of this operators: + - * / ** V % ! -> |")

    second_number = "nothing special"

    if operator != "!" and operator != "V":
        second_number = input("Put here your second number -> |")
        print("calculating...")

    # Here starts the MATH with other operators:
    if operator == "!":
        print("Your result is: " + str(math.factorial(int(first_number))))
    elif operator == "V":
        print("Your result is: " + str(math.sqrt(int(first_number))))
    elif operator == "+":
        print(str(int(first_number) + int(second_number)))
    elif operator == "-":
        print(str(int(first_number) - int(second_number)))
    elif operator == "*":
        print(str(int(first_number) * int(second_number)))
    elif operator == "/":
        print(str(int(first_number) / int(second_number)))
    elif operator == "**":
        print(str(int(first_number) ** int(second_number)))
    else:
        print(str(int(first_number) % int(second_number)))

    x = input("Do you want to stop calculating? (Y/N): ")
    if x == "Y":
        should_be_stopped = True