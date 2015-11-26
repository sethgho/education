
import random

def getRandomNumber():
	return int(random.random() * 10);


def askQuestion(number1, number2):
	question = "What is " + str(number1) + " x " + str(number2) + "? "
	correct = False;
	while not correct:
		answer = raw_input(question)
		if answer.isdigit():
			correct = int(answer) == number1 * number2
			if correct:
				print "CORRECT!"
			else:
				print "Wrong. Try again!"
		else:
			print "That's not a number, silly!"
		
while True:
	firstNumber = getRandomNumber()
	secondNumber = getRandomNumber()
	askQuestion(firstNumber, secondNumber)
