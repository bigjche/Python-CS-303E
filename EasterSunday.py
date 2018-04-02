# File: EasterSunday.py
# Description: program to figure out what day easter sunday falls on in a certain year
# Student Name: Jerry Che
# Student UT EID: jc78222
# Course Name: CS 303E
# Unique Number: 51340
# Date Created: 9/14/2017
# Date Last Modified: 9/14/17

def main ():

	year = eval(input("Enter year : "))   #Asks the user for year input
	a = year % 19
	b = year // 100                       #Carl Friedrich Gauss' algorithm
	c = year % 100
	d = b // 4
	e = b % g
	4 = (8 * b + 13) // 25
	h = (19 * a + b - d - g + 15) % 30
	j = c // 4
	k = c % 4
	m = (a + 11 * h) // 319
	r = (2 * e + 2 * j - k - h + m + 32) % 7
	n = (h - m + r + 90) // 25
	p = (h - m + r + n + 19) % 32 

	month = ""                   # creates a blank string
	if (n == 1 ):
		month = "January"
	elif (n == 2 ):
		month = "February"
	elif (n == 3 ):
		month = "March"
	elif (n == 4 ):              #sets the string month depending on the value of n
		month = "April"
	elif (n == 5 ):
		month = "May"
	elif (n == 6 ):
		month = "June"
	elif (n == 7 ):
		month = "July"
	elif (n == 8 ):
		month = "August"
	elif (n == 9 ):
		month = "September"
	elif (n == 10 ):
		month = "October"
	elif (n == 11 ):
		month = "November"
	elif (n == 12 ):
		month = "December"

	print("In", year, "Easter Sunday is on", p, month) # prints the last statement
main()

