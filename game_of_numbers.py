from parent_game import Game

class GuessNumber(Game):

    def start_game(self):
        self.guess_number = int(input("Введи число от 1 до 10\n"))
        while True:
            if int(self.guess_number) < self.random_value:
                print(f'{self.guess_number} число меньше загаданного')
                break
            if int(self.guess_number) > self.random_value:
                print(f'{self.guess_number} число больше загаданного')
                break
            if int(self.guess_number) == self.random_value:
                print(f'число {self.guess_number} угадано с 100% точностью')
            return
        self.start_game()

GuessNumber()