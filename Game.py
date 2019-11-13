# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:10:53 2019

@author: ignac
"""

#Dont touch this functions!!Copy here when it is checked and is ok
#Converting a number into some base N with vector length L
#Number that players have: player1=1 or player2=2
#We will consider during the whole exercise matrix as i, rows as j and columns as k
import numpy as np
import random
from time import sleep
player1=1
player2=2
#Create a new board
def create_board():
    mat=np.array([[[0 for i in range(4)] for j in range(4)] for k in range(4)])
    return mat
#Checking empty spaces
def possibilities(board):
    pos=[]
    N=len(board)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if board[i,j,k]==0:
                   pos.append((i,j,k))               
    return(pos)
#Assignating a random position to me or the adversary considering the possibilities
def random_place(board,player):
    possible=possibilities(board)
    selection=random.choice(possible)
    board[selection]=player
    return board
#Different manners of win in the game
#Row checker. For now only for each matrix separated
def row_win(board,player):
    N=len(board)
    for i in range(N):
        for j in range(N):
            win=True
            for k in range(N):
                if board[i,j,k]!=player:
                    win=False
                    break
            if win==True:
                return win
    return win  
def column_win(board,player):
    N=len(board)
    #Matrix i
    for i in range(N):
        #Column k
        for k in range(N):
            win=True
            #Row j
            for j in range(N):
                if board[i,j,k]!=player:
                    win=False
                    break
            if win==True:
                return win
    return win  
def column3D_win(board,player):
    N=len(board)
    #Row j
    for j in range(N):
        #Column k
        for k in range(N):
            win=True
            #matrix i
            for i in range(N):
                if board[i,j,k]!=player:
                    win=False
                    break
            if win==True:
                    return win            
    return win  
#Try of both diagonals (2D)
def diags_win(board,player):
    N=len(board)
    #Matrix i
    for i in range(N):
        win=True
        #Diags
        for j in range(N):
            if board[i,j,j]!=player:
                win=False
                break
        if win==True:
            return win 
     #Matrix i   
    for i in range(N):
        win=True
        #Rows and columns
        for j in range(N):
            if board[i,j,(N-1)-j]!=player:
                win=False
                break
        if win==True:
            return win
    return win 
#See if there is a winner in 3D direction x
def win3Dx(board,player):
    #Rows j
    N=len(board)
    for j in range(N):
        #Level j
        win=True
        #Level i
        for i in range(N):
            if board[i,j,i]!=player:
                win=False
                break
        if win==True:
            return win
    #Rows j for the other diagonal
    for j in range(N): 
        win=True
        #Level i
        for i in range(N):
            if board[i,j,N-1-i]!=player:
                win=False
                break
        if win==True:
            return win
    return win    
def win3Dy(board,player):
    #Columns k
    N=len(board)
    for k in range(N):
        win=True
        #Level i
        for i in range(N):
            if board[i,i,k]!=player:
                win=False
                break
        if win==True:
            return win
    #Now to the other diagonal
    #Row k
    for k in range(N):
        win=True
        #Level i
        for i in range(N):
            if board[i,N-1-i,k]!=player:
                win=False
                break
        if win==True:
            return win
    return win    
def win3Ddiag(board,player):
    #Level i
    N=len(board)
    win=True
    for i in range(N):
        if board[i,i,i]!=player:
            win=False
            break
    if win==True:
        return win
    #Now to other diagonal
    win=True
    for i in range(N):
        if board[i,N-1-i,N-1-i]!=player:
            win=False
            break
    if win==True:
        return win
    #Third 3D diagonal
    win=True
    for i in range(N):
        if board[i,i,N-1-i]!=player:
            win=False
            break
    if win==True:
        return win
    #Last diagonal
    win=True
    for i in range(N):
        if board[i,N-1-i,i]!=player:
            win=False
            break
    if win==True:
        return win
    return win
#See if there is a winner
def win(board,player):
    win=row_win(board,player) or column_win(board,player)\
    or diags_win(board,player) or column3D_win(board,player)\
    or win3Dx(board,player) or win3Dy(board,player)\
    or win3Ddiag(board,player)
    return win
#Return the position that makes the player win
def positionwinner(board,player):
    N=len(board)
    if row_win(board,player):
        print("Win by 2D row")
        for i in range(N):
            for j in range(N):
                win=True
                positions=[]
                for k in range(N):
                    positions.append([i,j,k])
                    if board[i,j,k]!=player:
                        win=False
                        positions=[]
                        break
                if win==True:
                    print("winning positions are",positions)
                    return positions
        
    elif column_win(board,player):
        print("Win by 2D column")
        for i in range(N):
        #Column k
            for k in range(N):
                win=True
                positions=[]
            #Row j 
                for j in range(N):
                    positions.append([i,j,k])
                    if board[i,j,k]!=player:
                        win=False
                        positions=[]
                        break
                if win==True:
                    print("winning positions are",positions)
                    return positions
    elif diags_win(board,player):
        print("Win by win in diagonals 2D")
        for i in range(N):
            win=True
            positions=[]
            for j in range(N):
                positions.append([i,j,j])
                if board[i,j,j]!=player:
                        win=False
                        positions=[]
                        break
            if win==True:
                print("winning positions are",positions)
                return positions 
     #Matrix i   
        for i in range(N):
            win=True
            positions=[]
        #Rows and columns
            for j in range(N):
                positions.append([i,j,(N-1)-j])
                if board[i,j,(N-1)-j]!=player:
                        positions=[]
                        win=False
                        break
            if win==True:
                print("winning positions are",positions)
                return positions
            
    elif column3D_win(board,player):
        print("Win by 3D column")
        for j in range(N):
            for k in range(N):
                    win=True
                    positions=[]
                    for i in range(N):
                        positions.append([i,j,k])
                        if board[i,j,k]!=player:
                            positions=[]
                            win=False
                            break
                    if win==True:
                        print("winning positions are",positions)
                        return positions             
    elif win3Dx(board,player):
        print("Win by 3D in direction x rows")
        for j in range(N):
            win=True
            positions=[]
            for i in range(N):
                positions.append([i,j,i])
                if board[i,j,i]!=player:
                    positions=[]
                    win=False
                    break
            if win==True:
                print("Winning positions are",positions)
                return positions
    #Rows j for the other diagonal
        for j in range(N): 
            win=True
            positions=[]
            for i in range(N):
                positions.append([i,j,N-1-i])
                if board[i,j,N-1-i]!=player:
                    positions=[]
                    win=False
                    break
            if win==True:
                print("Winning positions are",positions)
                return positions   
    elif win3Dy(board,player) :
        print("Win by 3D in direction y rows")
        for k in range(N):
            win=True
            positions=[]
            for i in range(N):
                    positions.append([i,i,k])
                    if board[i,i,k]!=player:
                        positions=[]
                        win=False
                        break
            if win==True:
                print("Winning positions are",positions)
                return positions
    #Now to the other diagonal
    #Row k
        for k in range(N):
            win=True
            positions=[]
            for i in range(N):
                positions.append([i,N-1-i,k])
                if board[i,N-1-i,k]!=player:
                    positions=[]
                    win=False
                    break
            if win==True:
                print("Winning positions are",positions)
                return positions
    elif win3Ddiag(board,player):
        print("Win by 3D diagonals")
        win=True
        positions=[]
        for i in range(N):
            positions.append([i,i,i])
            if board[i,i,i]!=player:
                    win=False
                    positions=[]
                    break
        if win==True:
            print("Winning positions are",positions)
            return positions
        win=True
        positions=[]
        for i in range(N):
            positions.append([i,N-1-i,N-1-i])
            if board[i,N-1-i,N-1-i]!=player:
                win=False
                positions=[]
                break
        if win==True:
            print("Winning positions are",positions)
            return positions
    #Third 3D diagonal
        win=True
        positions=[]
        for i in range(N):
            positions.append([i,i,N-1-i])
            if board[i,i,N-1-i]!=player:
                win=False
                positions=[]
                break
        if win==True:
            print("Winning positions are",positions)
            return positions
    #Last diagonal
        win=True
        positions=[]
        for i in range(N):
            positions.append([i,N-1-i,i])
            if board[i,N-1-i,i]!=player:
                win=False
                positions=[]
                break
        if win==True:
            print("Winning positions are",positions)
            return positions
#Function to evaluate if there is a winner, or if there is not a winner but there is a draw
#Or if there is not winner or draw. Return 1 if the winner is player 1, return 2 if the winner is player
#2, return 0 if there is no winner yet and we can keep playing, and return -1 if there is a draw
def evaluate(board):
    winner=0
    for player in [1,2]:
        if win(board,player):
            winner=player
    if np.all(board!=0) and winner==0:
        winner=-1
    return winner
def play_game():
    board,winner,counter=create_board(),0,1
    while winner==0:
        for player in [1,2]:
            board=random_place(board,player)
            counter=counter+1
            winner=evaluate(board)
            if winner!=0:
                if winner==1 or winner==2:
                    print("the winner is player ",winner,"after",counter,"tries")
                    print("Te final board is")
                    print(board)
                    positionwinner(board,winner)
                else:
                    print("there is a draw")
                break
    return winner        

