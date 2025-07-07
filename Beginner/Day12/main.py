from random import randint
from art import  logo

from oauthlib.common import to_unicode

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0
def Game():
	print(logo)
	def check_answer(user_guess , actual_answer ,turns):
		if user_guess > actual_answer:
			print("Too high. ")
			return  turns -1
		elif user_guess < actual_answer:
			print("Too low. ")
			return turns -1
		else:
			print(F"You got it! the answer was {actual_answer }")


	def set_difficulty():
		level = input("Choose Difficulty. type 'easy' or 'hard' :")
		if level == "easy":
			return EASY_LEVEL_TURNS
		else:
			return  HARD_LEVEL_TURNS


	print("Number Geussing Game!")
	print("I'm thinking of a number between 1 and 100")
	answer = randint(1,100)
	turns = set_difficulty()
	guess = 0
	while guess != answer:
		print(f" You have {turns} attempts remaining to guess the number")
		guess = int(input("Make a Guess: "))
		turns = check_answer(guess , answer , turns)
		if turns == 0:
			print("You've run out of guessing numbers . you loae")
			return
		elif guess != answer:
			print("Guess Again")
Game()