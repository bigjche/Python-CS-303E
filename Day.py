# File: Day.py
# Description: asks the user for input of year,month,and day then returns the day of the week it falls on
# Student Name: Jerry Che
# Student UT EID: jc78222
# Course Name: CS 303E
# Unique Number: 51340
# Date Created: 9/23/17
# Date Last Modified: 9/24/17

def main():
	year = int(input("Enter year: "))			#Prompts the user for a year
	while (year>2100 or year<1900):				#Checks to see if the year falls in between the range 1900-2100
		year = int(input("Enter year: "))
	
	month = int(input("Enter month: "))			#Prompts the user for a month
	while(month > 12 or month < 1):
		month = int(input("Enter month: "))		#Checks to see if the year falls in between the ranges 1-12
	
	day = int(input("Enter day: "))				#Prompts the user to enter a day
	while((month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) and (day<1 or day>31)):			# Checks to see if the days fall outside of 31 days
		day = int(input("Enter day: "))
	while((month==4 or month==6 or month==9 or month==11) and (day<1 or day>30)):			                                    # Checks to see if the days fall outside of 30 days		
		day = int(input("Enter day: "))
	while(month==2 and ((year%4!=0) or (year%100==0) or (year%400!=0)) and (day>28 or day<1)):                                  # Checks to see if the year IS NOT a leap year and does not have more than 28 days
		day = int(input("Enter day: ")) 
	while(month==2 and ((year%4==0 and year%100!=0 and year%400==0)) and (day>29 or day<1)):									# Checks to see if the year IS a leap year and does not have more than 29 days
		day = int(input("Enter day: ")) 

 
	a = 0
	if(month>=3 and month<=12):			#Sets the variable a based on the month given
		a= month-2
	elif(month==1):
		a=11
		year -= 1
	elif(month==2):
		a=12
		year-=1
	b = day                               
	c = year%100
	d = year//100

	w = ((13*a)- 1)//5					 #Rev. Zeller's algorithm
	x = c//4
	y = d//4
	z = w+x+y+b+c-(2*d)
	r = z% 7
	r = (r+7)%7

	result="" 							#sets an empty string variable 
	if(r==0):
		result = "Sunday"        		#sets the variable result based on the number given by r
	if(r==1):
		result = "Monday"
	if(r==2):
		result = "Tuesday"
	if(r==3):
		result = "Wednesday"
	if(r==4):
		result = "Thursday"
	if(r==5):
		result = "Friday"
	if(r==6):
		result = "Saturday"

	print("The day is",result)			#prints the output 



main()




