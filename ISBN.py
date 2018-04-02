#  File: ISBN.py

#  Description: takes an ISBN and returns if it is a true isbn or not

#  Student Name: Jerry Che

#  Student UT EID: jc78222

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created: 10/28/17

#  Date Last Modified: 10/30/17

# Function to determine wheter an ISBN is valid
def is_valid(s1):
  for i in range (len(s1)-1):
    if ((ord(s1[i])< 48) or (ord(s1[i]) > 57)):
      return False
    if (s1[i]=='X' or s1[i]=='x'):
      return False
  if (len(s1) != 10):
      return False
  return True

# Function to determine if the partial sums are divisble by 11
def sum_isbn(s2):
  isbn_checked = []
  sum1 = []
  sum2 = 0
  if (is_valid(s2)):
    for i in range (len(s2)):
      if (s2[i]=='X' or s2[i]=='x'):
        isbn_checked.append(10)
      else:
        isbn_checked.append(int(s2[i]))
    for j in range(len(isbn_checked)):
      if (j==0):
        sum1.append(isbn_checked[0])
      else:
        sum1.append(isbn_checked[j]+ sum1[j-1])
    for k in range(len(sum1)):
      sum2 += sum1[k]

    if (sum2 % 11 == 0):
      return True
  return False





def main ():
  # Opens files
  isbn = open("./isbn.txt", "r")
  isbnOut = open("./isbnOut.txt","w")

  #Goes through and runs the program into the two methods and checks to see if it is a valid ISBN
  for line in isbn:
    isbn_1 = line
    isbn_1 = isbn_1.strip()
    isbn_1 = isbn_1.replace('-',"")

    if (is_valid(isbn_1) and sum_isbn(isbn_1)):
      isbnOut.write(line.strip() + " valid\n")
    else:
      isbnOut.write(line.strip() + " invalid\n")
      

  #Closese the file
  isbn.close()
  isbnOut.close()


main()