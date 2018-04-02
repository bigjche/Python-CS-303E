# File: Deal.py
# Description: simulates the Monty Hall "Lets Make a Deal" game show
# Student Name: Jerry Che
# Student UT EID: jc78222
# Course Name: CS 303E
# Unique Number: 51340
# Date Created: 10/17/17
# Date Last Modified: 10/20/17

import random
import math
def main():
	play = eval(input("Enter number of times you want to play: "))			#Prompts the user for the number of times they want to play
	switch = 0
	print (" ","Prize","      ","Guess","       ","View","    ","New Guess")
	for t in range (0,play + 1):
		prize = random.randint(1,3)											#Sets prize,guess,and view to random variables
		guess = random.randint(1,3)
		view = random.randint(1,3)
		while (view==prize or view==guess):									#makes sutr view doesn't equal guess or prize
			view=random.randint(1,3)
		newGuess = random.randint(1,3)
		while(newGuess==view or newGuess==guess):							#makes sure guess doesn't equal view or guess
			newGuess= random.randint(1,3)
		if (newGuess==prize):
			switch +=1														#increments switch if they get the right guess after they switch their guess

		print("   ",prize,"          ",guess,"          ",view,"          ",newGuess,end=" ")  #prints the results of each round
		print()


	


	switch_win= switch/play    												#calculates the percentage that the player wins by switching
	win = 1-switch_win

	
	print("Probability of winning if you switch = ","{:.2f}".format(switch_win))   #Prints the probabilities 
	print("Probability of winning if you do not switch = ","{:.2f}".format(win))

	

main()
  
