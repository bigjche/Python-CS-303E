# File: Hailstone.py
# Description: returns the number with the longest hailstone sequence and the number of digits in that sequence
# Student Name: Jerry Che
# Student UT EID: jc78222
# Course Name: CS 303E
# Unique Number: 53450
# Date Created: 7/28/17
# Date Last Modified: 7/29/17


def main():
	a=eval(input("Enter starting number of the range: "))               #Asks the user for a starting range number
	while(a < 0):
		a = eval(input("Enter starting number of the range: "))			# Checks to see if the starting number is positive
	b=eval(input("Enter ending number of the range: "))					# Asks the user for an ending number
	while(b < 0 or b<a):
		b = eval(input("Enter ending number of the range: "))			# Prompts the user to enter another number if it is not positive or it is smaller than the starting numbert
	biggest = 0															# sets a variable that will hold the number length of the number with the longest sequence
	result = 0  														# set a variable that will hold the number with the longest length
	
	for n in range (a, b +  1):
		i = n
		length = 0														# resets the variable length so that it won't count the previous #'s length
		while(i > 1):
			if(i % 2 == 0):												# Checks to see if a number is positive then divides it by 2
				i = i // 2
				length +=1
			elif(i % 2 == 1):											# Checks to see if a number is odd and then multiplies it by 3 and adds one
				i = (3*i) + 1
				length += 1

		if (length >= biggest):											# Checks to see if the current length is bigger than the previous #'s length
			result = n 													# Sets the variable result to the number with the longest length
			biggest = length											# Sets the variable biggest to the length of the number with the longest sequence
	print("The number",result, "has the longest cycle length of", biggest) #Prints the results
main()




