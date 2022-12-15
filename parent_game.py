import random


class Game():

    def __init__(self):
        self.random_value = random.randint(1, 10)
        self.start_game()

    def __del__(self):
        print('Конец игры!')
