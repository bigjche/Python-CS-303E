# File: DNA.py
# Description: takes a file named DNA.txt and finds the longest common substrand
# Student Name: Jerry Che
# Student UT EID: jc78222 
# Course Name: CS 303E
# Unique Number: 51340
# Date Created: 10/23/17
# Date Last Modified: 10/26/17




def main ():
  #opens the text file
  in_file = open ("./dna.txt", "r")

  #reads the number of strands to return
  num_pairs = in_file.readline ()
  num_pairs = num_pairs.strip()
  num_pairs = int (num_pairs)

  print("Longest Common Sequences")
  print()


  # sets DNA strands to strand1 and strand 2 and removes all spaces and captalizes it
  for i in range (num_pairs):
    st1 = in_file.readline()
    st2 = in_file.readline()

    st1 = st1.strip()
    st2 = st2.strip()

    st1 = st1.upper ()
    st2 = st2.upper ()

    


   # sets an empty list 
    longest_strand = [ ]
   #decides which strand is bigger and goes through a loop to find the longest common strand
    if(len(st2) > len(st1)):
      wnd = len(st1)
      
      while(wnd > 1):
        if(len(longest_strand) > 0):
          break
        st_index = 0   
   
        while(wnd + st_index <= len(st1)):
          if(st2.find(st1[st_index: st_index + wnd]) > -1):
            longest_strand.append(st1[st_index: st_index + wnd])
            if(longest_strand.count(st1[st_index: st_index + wnd]) > 1):
              longest_strand.remove(st1[st_index: st_index + wnd])
            
          st_index += 1
         
        wnd -= 1  
    # if strand 2 is shorter than it sets the window to the length of strand 2 and goes through a loop to find which is the longest substring
    else:
      wnd = len(st2)
      
      while(wnd > 1):
        if(len(longest_strand) > 0):
          break
          
        st_index = 0
        
        while(wnd + st_index <= len(st2)):
          if(st1.find(st2[st_index: st_index + wnd]) > -1):
            longest_strand.append(st2[st_index: st_index + wnd])
            if(longest_strand.count(st1[st_index: st_index + wnd]) > 1):
              longest_strand.remove(st1[st_index: st_index + wnd])
            
          st_index += 1
          
        wnd -= 1


    # prints out the result
    result = 'Pair ' + str(i+1) + ': '
    space  = len(result) * ' '
    
    print(result, end = '')
    
    if(len(longest_strand) == 0):
      print('No Common Sequence Found \n')
    
    else:
      for j in range(len(longest_strand)):
        if (j == 0):
          print(longest_strand[j])
        else:
          print(space + longest_strand[j])
      print('')
    
     
  #closes the file
  in_file.close()

main()