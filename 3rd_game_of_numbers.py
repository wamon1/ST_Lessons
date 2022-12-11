import random

class Game():
    print("Угадай число от 1 до ",n," за ",times," попыток")

    def __init__(self, n):
        self.userGuess = random.randint(1, n)
