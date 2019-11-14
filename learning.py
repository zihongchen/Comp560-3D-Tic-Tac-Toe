import numpy as np
import random
from time import sleep
import math
from Game import *

#utilityArray is a 4by4by4 numpy array with utility value
#this function updates the utility at the end of each single game
def utilityUpdate(board,winner,utilityArray):
    N=len(board)
    if winner!=-1:# when the game is not draw
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if board[i,j,k]==winner:
                        utilityArray[i,j,k]+=1# increase the utility value of the winner
                    elif board[i,j,k]!=0:
                         utilityArray[i,j,k]-=1# decrease the utility value of the loser  
        return utilityArray                    
#a list with the squares which have higher utility values at the beginning
def Rankedpossibilities(utilityArray):
    rankedPossible=utilityArray.flatten()
    rankedPossible=np.sort(rankedPossible)
    rankedPossible=rankedPossible[::-1]              
    return(rankedPossible) 


#Iterating the game for learning

def learning_randomly_4x4x4(iterations1,iterations2,iterations3): 
    utilityArray=create_board()
    Utility1=create_board()
    Utility2=create_board()
    Utility3=create_board()
    for i in range(iterations3):
        winner,board=play_game_randomly()[0:2]      
        utilityArray=utilityUpdate(board,winner,utilityArray)
        if i==iterations1:
            Utility1=utilityArray
            print("Utility function learning randomly with",iterations1,"iterations:")
            print(Utility1)
        elif    i==iterations2:
            Utility2=utilityArray
            print("Utility function learning randomly with",iterations2,"iterations:")
            print(Utility2)
    Utility3=utilityArray        
    print("Utility fuction learning randomly with",iterations3,"iterations:")
    print(Utility3)

