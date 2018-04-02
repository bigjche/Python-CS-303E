# File: Goldbach.py
# Description: this program takes a user input that is greater than five and returns all even numbers and a sum of two numbers
# Student Name: Jerry Che
# Student UT EID: jc78222
# Course Name: CS 303E
# Unique Number: 51340
# Date Created: 10/10/17
# Date Last Modified: 

def is_prime(n):						#Function that determines if an argument is prime
	for i in range (2, int(n**0.5)+1):
		if(n%i==0):
			return False
	return True






def main():
	min = eval(input("Enter the lower limit: "))  # Prompts the user for a starting and end value
	max = eval(input("Enter the upper limit: "))

	if ((min % 2 ==0) and (max %2 ==0) and (max>min)):		#checks to make sure the user input works for the theorem

		for m in range (min, max + 1):			#Loop to search for prime numbers that add up to an even digit
			result = ""
			if (m %2 == 0):
				result += str(m)
				for a in range (2, m + 1):
					if (is_prime(a)):
						for b in range (2,m + 1):
							if (is_prime(b)):
								if(a+b==m):
									if (a<=b):
										result = result +" = " + str(a) +" " + "+" + " "+ str(b)
				print (result)					# Printst the result


main()





