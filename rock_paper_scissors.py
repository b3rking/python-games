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