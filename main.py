import random

while True:
    random_number = random.randint(1, 10)
    Guess = int(input("Guess a Number 1-10: "))
    if Guess > random_number:
        print("TO HIGH! TO HIGH!")
    elif Guess < random_number:
        print("Low Ground")
    else:
        break
print("CONGRATS")