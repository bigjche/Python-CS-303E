# File: CalculatePI.py
# Description: calculates PI given a random throw on the dartboard
# Student Name: Jerry Che
# Student UT EID: jc78222
# Course Name: CS 303E
# Unique Number: 51340
# Date Created: 10/15/17
# Date Last Modified: 10/16/17

import math											#imports the libraries the program will be using
import random

def computePI (numThrows):
	xPos = random.uniform(-1.0,1.0)					#Sets the x and Y coordinates to a random number in the range (-1.0,1.0)
	yPos = random.uniform(-1.0,1.0)
	dis = math.hypot(xPos,yPos)
	counter = 0
	newPi = 0

	for n in range (0,numThrows):
		xPos = random.uniform(-1.0,1.0)
		yPos = random.uniform(-1.0,1.0)
		dis = math.hypot(xPos,yPos)
		if (dis < 1):
			counter +=1

	newPi = (4.0 * counter) / numThrows
	return newPi


def main():
	for numThrows in (100, 1000, 10000, 100000, 1000000, 10000000):
		compPI = computePI(numThrows)
		diff = compPI - math.pi
		print ("num = %-8d   Calculated PI = %8.6f   Difference = %+9.6f" % \
          (numThrows, compPI, diff))

main()