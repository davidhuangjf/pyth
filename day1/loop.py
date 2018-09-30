running = True
number = 55

while running:
    guess = int(input("Enter an integer: "))

    if guess == number:
        print("OK")
        running=False