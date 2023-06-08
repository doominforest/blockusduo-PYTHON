# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 20:59:02 2023

@author: erins
"""

# -*- coding: utf-8 -*-
import numpy as np

#for i in range(29):
   # print("--",end="")
#for i in range(14):
    #print()
    #for j in range(14):
     #   print("|   ", end="")
    #print("|", end="")
    #print()
    #for i in range(29):
      #  print("--", end="")


#random 14 by 14 array
One_Array = np.array([[0,1,2,0,1,2,0,1,2,0,1,2,0,1],
                      [0,1,2,0,1,0,0,1,2,0,1,2,0,1],
                      [0,1,2,0,1,2,0,1,2,0,1,2,0,1],
                      [0,1,2,0,1,2,0,1,2,0,1,2,0,1],
                      [0,1,2,0,2,2,0,1,2,0,1,2,0,1],
                      [0,1,2,0,1,2,0,1,1,0,1,2,0,1],
                      [0,1,2,0,1,2,0,1,2,0,1,2,1,1],
                      [0,1,2,0,1,2,0,1,2,0,1,2,1,1],
                      [0,1,2,0,1,2,0,1,2,0,1,2,1,1],
                      [0,1,2,0,1,2,0,1,2,0,1,2,0,1],
                      [0,1,1,0,1,2,0,1,2,0,1,2,0,1],
                      [0,1,1,0,1,1,0,1,1,0,1,2,0,1],
                      [0,1,2,0,1,2,0,1,2,0,1,2,0,1],
                      [0,1,2,0,1,2,0,1,2,0,1,2,0,1]])
print()
for i in range(29):
    print("--",end="")
for i in One_Array:
    print()
    for j in i:
        if j == 1:
            print("| B ", end="")
        if j == 2:
            print("| W ", end="")
        if j == 0: 
            print("|   ", end="")
    print("|", end="")
    print()
    for i in range(29):
        print("--", end="")
