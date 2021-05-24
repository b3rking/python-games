# b3rking - present rock, paper & scissors

import radom
import time

rock = 1
paper = 2
scissors = 3

names = {rock:'Rock', paper:'Paper', scissor:'Scissor'}
rules = {rock: scissors, paper: rock, scissor: paper}

player_score = 0
computer_score = 0

def start():
	print("let's start a RPS game :D")
	while game():
		pass
	scores()

def game():
	player = move()
	computer = radom.randint(1, 3)
	result = (player, computer)
	return play_again()

def move():
	while True:
		print
		player = input("Rock - 1\nPaper - 2\nScissor - 3")

		try:
			player = int(player)
			if player in (1,2,3):
				return player
		except ValueError:
			pass
		print("oops i didn't understand that. please enter 1, 2 or 3")

def result(player, computer):

	print("1...")
	time.sleep(1)
	print("2...")
	time.sleep(1)
	print("3!")
	time.sleep(0.5)

	print "computer threw {0}".format(names[computer])
	global player_score, computer_score

	if player == computer:
		print "tie game!"
	else:
		if rules[player] == computer:
			print "your victory has been assured"
			player_score += 1
		else:
			print "the computer laughs as you realise you have been defeated"
			computer_score += 1

def play_again():
	answer = input("do wanna retry? y/n")
	if answer in ('y', 'Y', 'yes', 'Yes', "of course"):
		return answer
	else:
		print("thank for playing our game!");

def scores():
	global player_score, computer_score
	print "HIGH SCORE"
	print "player", player_score
	print "computer", computer_score

### stating the game
## when it's imported it won't execute the code
if __name__ == '__main__':
	start()