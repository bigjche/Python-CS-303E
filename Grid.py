#  File: Grid.py

#  Description: finds the greatest product in blocks of 4

#  Student Name: Jerry Che

#  Student UT EID: jc78222

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created: 11/2/17

#  Date Last Modified: 11/2/17


def main():
  # open file for reading
  in_file = open ("./grid.txt", "r")

  # read the dimension of the grid
  dim = in_file.readline()
  dim = dim.strip()
  dim = int (dim)

  # create an empty grid
  grid = []

  # populate the grid
  for i in range (dim):
    line = in_file.readline()
    line = line.strip()
    row = line.split()
    for j in range (dim):
      row[j] = int (row[j])
    grid.append (row)

  # print the grid
  # print (grid)

  # close the file
  in_file.close()

  # creates an empty grid
  results = []

  # read and multiply in blocks of four along rows
  for row in grid:
    for i in range (dim - 3):
      prod = 1
      for j in range (i, i + 4):
        prod = prod * row[j]
      results.append(prod)
   

  # read each column in blocks of four
  for j in range (dim):
    for i in range (dim - 3):
      prod = 1
      for k in range (i, i + 4):
        prod = prod * grid[k][j]
      results.append(prod)

  # go along all diagonals L to R in blocks of 4
  for i in range (dim - 3):
    for j in range (dim - 3):
      prod = 1
      for k in range (4):
        prod = prod * grid[i + k][j + k]
      results.append(prod)
  
 
  # go along all diagonals R to L in blocks of 4
  for i in range (dim - 3):
    for j in range (3, dim):
      prod = 1
      for k in range (4):
        prod = prod * grid[i + k][j - k]
      results.append(prod)

  # Finds the greates product by using the built-in function max and prints it out
  max_product = max(results)
  print("The greatest product is",max_product)

main()