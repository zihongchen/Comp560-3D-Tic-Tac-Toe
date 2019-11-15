# Comp560-3D-Tic-Tac-Toe

**To run our program:** \

Our project is not on master branch!!
Our functions are on functions.py and learning.py and game.py
You could see our result in the jupiter file playground.
To run our program from shell, excute Playground.py in terminal




Zihong Chen

Ignacio Piera Fernández de Retana



Contributions:

Both students contributed to both parts, but Ignacio contributed the most to the creation of the game and the simplest learning and Zihong to the learning implementation with exploration and exploitation for improving the learning.

First part: Creating the game

First， we developed the game. It consisted in creating the board for each of the games, giving the rules about what does mean either winning or loose and the possibilities that each player has during each try of one game.

Finally, we did an evaluate function for knowing if there was a winner, a draw or the game had not finished yet and it returned the value of the winner (Player 1 or player 2) or -1 if there was a draw.

Finally， we start the learning implementation with a game where each of the adversaries choose positions randomly.

Second part: Learning implementation

Simple Learning- learning_randomly_4x4x4(iterations1,iterations2,iterations3)：

On the first hand we tried to do the simplest case: just learning the utility function by doing random moves and giving rewards of either +1 or -1. Each player places randomly until someone wins the game. After that, we update all winner’s squares by +1 and loser’s squares by -1. At the end we return a 4x4x4 array representing the utility of each square of the board.

For implementing the learning option we created a learning file with a function called learning_randomly_4x4x4(iterations1,iterations2,iterations3), which basically asks for 3 distinct number of iterations that have to be higher one after the other (Example: (100,1000,2000)) and outputs the Utility function value after each number of iterations.



learning_with_exploration_and_exploitation(iterations1,iterations2,iterations3):
In this function, agents no longer randomly choose the square. 30% of the time, the player would choose randomly. 70% percent of the time, the player would choose the square that has the highest utility value on the 4x4x4 utility array. At the first round, the 4x4x4 utility array is all zero, so the player would just randomly choose squares. After first round, the winner’s squares’ utility values get increased by one; the loser’s squares’ utility values get decreased by 1. 
This is the utility array two rounds later. 

[[[-3  0  0  0]
  [ 0  0  1  0]
  [ 0  0  0  0]
  [ 0  0 -2  0]]

 [[ 0  0 -2  2]
  [-2  2  2  2]
  [-2  3 -2  2]
  [ 2  2 -2 -2]]

 [[ 2  2 -2  2]
  [-2 -3  2 -3]
  [ 2  2 -2 -1]
  [-2 -3  2  2]]

 [[-1  3 -3  3]
  [-3  3 -3  1]
  [-1  3  3 -3]
  [ 3 -3  1 -1]]]

 
The player now would value squares with the utility value 3 more than the square value with -2 for 70% of the time. For the other 30% of the time, it would choose randomly.

However, this method doesn’t perform well without potential row or column checker. To get a truly intelligent agent, we have to use either Q-learning or temporal difference to do the utility update instead of just adding one. However, that means we have to keep track of the state space, in 4x4x4 tic tac toe. We plan to do it, but we are running out of the time. 

