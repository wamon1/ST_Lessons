import random

def game(n, times):
    print("Угадай число от 1 до ",n," за ",times," попыток")
    user_guess = random.randint(1, n)
    b = -1
    popitka = 0
    while user_guess != b:
        b = int(input("Ваш вариант = "))
        popitka = popitka + 1
        if b < user_guess:
            print("Число должно быть больше!")
        elif b > user_guess:
            print("Число должно быть меньше!")
        else:
            print("Угадали с ",popitka, " попытки")
    if popitka <= times:
        print("Уровень пройден!")
        rez = 1
    else:
        print("Неудача.Пробуем еще раз")
        rez = 0
    return rez

print("Приветствую. Игра - 'Угадай число'")

print("Уровень 1")
win = 0
while win == 0:
    win = game(10, 4)

print("Уровень 2")
win = 0
while win == 0:
    win = game(30, 6)

print("Уровень 3")
win = 0
while win == 0:
    win = game(100, 8)
print("Молодец, Ты справился! Игра окончена.")