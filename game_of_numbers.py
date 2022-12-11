import random

number = random.randint(1, 10)
userGuess = 1

while userGuess != number:
    userGuess = int(input("Угадай число от 1 до 10: "))
    if userGuess > number:
        print("Число должно быть меньше!")
    elif userGuess < number:
        print("Число должно быть больше!")
    else:
        print("Молодец!")