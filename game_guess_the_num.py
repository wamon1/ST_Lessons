from random import randint

NumberToGuess = randint(1, 10)
userGuess = -1

while userGuess != NumberToGuess:

userGuess = int(input("Угадай число от 1 до 10: "))

if userGuess > NumberToGuess:
	print("Число должно быть меньше!")

elif userGuess < NumberToGuess:
	print("Число должно быть больше!")

print("Вы угадали, это число = " + str(NumberToGuess))


