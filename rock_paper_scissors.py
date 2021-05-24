# b3rking - present rock, paper & scissors

import random
import time

rock = 1
paper = 2
scissor = 3

names = {rock:'Rock', paper:'Paper', scissor:'Scissor'}
rules = {rock: scissor, paper: rock, scissor: paper}

player_score = 0
computer_score = 0

## call all functions

def start():
	print("let's start a RPS game :D")
	game()
	while play_again():
		game()
	scores()
	play_again()

## the actual game

def game():
	player = move()
	computer = random.randint(1, 3)
	result = (player, computer)
	return result

## time for the player to play

def move():

		print("Rock - 1\nPaper - 2\nScissor - 3")
		player = input("your choice >>> ")
		 
		try:
			player = int(player)
			if player in (1,2,3):
				return player
		except ValueError:
			pass
		print("oops i didn't understand that. please enter 1, 2 or 3")

## showing the result

def result(player, computer):

	print("1...")
	time.sleep(1)
	print("2...")
	time.sleep(1)
	print("3!")
	time.sleep(0.5)

	print ("computer threw {0}".format(names[computer]))
	global player_score, computer_score

	if player == computer:
		print ("tie game!")
	else:
		if rules[player] == computer:
			print ("your victory has been assured")
			player_score += 1
		else:
			print ("the computer laughs as you realise you have been defeated")
			computer_score += 1

## to manage action

def play_again():
	answer = input("do wanna retry? y/n >>> ")
	if answer in ('y', 'Y', 'yes', 'Yes', "of course"):
		return True
	else:
		print("thank for playing our game!");

## manage scores

def scores():
	global player_score, computer_score
	print ("HIGH SCORE")
	print ("player", player_score)
	print ("computer", computer_score)

### stating the game
## when it's imported it won't execute the code

if __name__ == '__main__':
	start()


# testing all functions

# game()
# play_again()
# result(2,3)
# move()
# scores()