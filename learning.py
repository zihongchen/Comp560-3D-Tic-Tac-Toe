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
    
def availablePositions(board):
        positions = []
        N=len(board)
        for i in range(N):
            for j in range(N):
                for k in range (N):
                    if board[i, j,k] == 0:
                        positions.append((i, j, k))  # need to be tuple
        return positions

def utility_place(board,player,utilityArray,exp_rate): 
    positions=availablePositions(board)
    if np.random.uniform(0, 1) <= exp_rate:
        # take random action
        idx = np.random.choice(len(positions))
        action = positions[idx]
        #actionList.append(action)
        board[action]=player
        return board
    else:
        maxValue = -1000000000000000
        valueIndex = 0
        for i in positions:
            if utilityArray[i]>maxValue:
                maxValue=utilityArray[i]#find the current available position with the biggest utility value
                valueIndex=i
        board[i]=player
        #actionList.append(i)
        return board
        
def play_gameWithUtility(utilityArray):
    board,winner,counter=create_board(),0,1
    #player1Actionlist=[]
    #player2Actionlist=[]
    while winner==0:
        for player in [1,2]:
            if player ==1:
                board=utility_place(board,player,utilityArray,0.3)
            if player ==2:
                board=utility_place(board,player,utilityArray,0.3)
            winner=evaluate(board)        
            if winner!=0:
                #player1Actionlist=player1Actionlist[::-1]
                #player2Actionlist=player2Actionlist[::-1]
                if winner==1:  
                    utilityUpdate(board,winner,utilityArray)
                if winner==2: 
                    utilityUpdate(board,winner,utilityArray)
                          
                
    return winner 

def learning_with_exploration(iterations1,iterations2,iterations3): 
    utilityArray=create_board()
    Utility1=create_board()
    Utility2=create_board()
    Utility3=create_board()
    for i in range(iterations3):
        play_gameWithUtility(utilityArray)            
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
    