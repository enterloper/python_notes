import random

def game():
	secret_num = random.randint(1, 10)
	guesses = []

	while len(guesses) < 5:
		try:
			# get a number guess from the player
			guess = int(input("Guess a number between 1 and 10: "))
		except ValueError:
			print("{} is not a number!".format(guess))
		else:
			# compare guess to secret number
			if guess == secret_num:
				print("You got it! The number was {}".format(secret_num))
				break
			elif guess > secret_num:
				print("Close but no cigar, the number is lower than {}".format(guess))
			else:
				print("Your guess was a little low! The number is higher than {}".format(guess))
			guesses.append(guess)
	else:
		print("You didn't get it, my number was {}".format(secret_num))
	play_again = input("Do you want to play again?")
	if play_again.lower() != 'n':
		game()
	else:
		print("Bye!")

game()