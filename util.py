x = 1.0
y = 3.0
while x < y:
    print(x)
    x = x + 0.5

exit = False

while not exit:
    print("calculating...")
    x = input("Stop calculating? (Y/N): ")
    if x == "Y":
        exit = True

        co