#!/usr/bin/env python3
import numpy as np


#WE FIRST CONSTRUCT THE UNITARY THAT LET ME IDENTIFY THE 7 CLASSES

def BellAnalizer():
    phase= [[1,0,0,0,0,0,0,0],
       [0,-1,0,0,0,0,0,0],
       [0,0,1,0,0,0,0,0],
       [0,0,0,1,0,0,0,0],
       [0,0,0,0,1,0,0,0],
       [0,0,0,0,0,-1,0,0],
       [0,0,0,0,0,0,1,0],
       [0,0,0,0,0,0,0,1]]
    UMCF= [[1,1,0,0,1,1,0,0],
           [1,1,0,0,-1,-1,0,0],
           [0,0,1,1,0,0,1,1],
           [0,0,1,1,0,0,-1,-1],
           [1,-1,0,0,1,-1,0,0],
           [1,-1,0,0,-1,1,0,0],
           [0,0,1,-1,0,0,1,-1],
           [0,0,1,-1,0,0,-1,1]]
    Re1=[[0,0,0,0,0,0,0,1],
       [0,0,0,0,0,1,0,0],
       [0,0,0,1,0,0,0,0],
       [0,1,0,0,0,0,0,0],
       [0,0,1,0,0,0,0,0],
       [1,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,1,0],
       [0,0,0,0,1,0,0,0]]
    Re2=[[1,0,0,0,0,0,0,0],
       [0,1,0,0,0,0,0,0],
       [0,0,0,0,1,0,0,0],
       [0,0,0,0,0,1,0,0],
       [0,0,1,0,0,0,0,0],
       [0,0,0,1,0,0,0,0],
       [0,0,0,0,0,0,1,0],
       [0,0,0,0,0,0,0,1]]
    return np.matmul(np.matmul(Re2,UMCF), np.matmul(Re1,phase))
