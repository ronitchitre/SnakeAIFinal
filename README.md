# SnakeAIFinal
Name of mentee: Ronit Chitre\
Roll no.: 200110090\
Name of mentor: Shubham Lohiya
## About Project
In this project we automated the snake game using Reinforcement Learning.\
This is a type of machine learning in which the agent is trained by giving it a positive reward for desired behaviour and negative reward for undesired behaviour\
I have used three algorithms -: qlearning, sarsa, and expected sarsa.
## How To Play
First the agent needs to be trained for some episodes using some algorithm\
This is done by running *python backend.py -m {number of episodes} -a {algorithm}*\
{algorithm} can be 'qlearing', 'sarsa', 'expecsarsa'\
This will output a .txt file which will tell the snake the optimal action for each state\
Then run *python main.py -m {number of episodes} -a {algorithm}* to see the snake in action\
high_score.txt stores the overall highscore achieved\
In the solutions directory the average score and the state action matrix for different algorithms can be found
## Assignments
We had two assignments in this project
#### Assignment one 
This assignment was of two parts\
In the first part we had to solve a given mdp using value iterations the solution to the mdp was given for crosschecking\
In the next part we had to find the shortest path through a maze. In this part we had to encode the mdp ourselves and solve it using the algorihtm we made in the first part\
All information regarding maze and mdp can be found in the data directory\
Run *python planner.py --mdp {address of .txt file where mdp data is stored}* to solve the given mdp.\
Run *python encoder.py --grid {address of .txt file in which maze is encoded}* to find optimal solution to maze (which will be printed in stdout in the form of directions N for north, S for south, E for east, W for west)
#### Assignment two
In this assignment we had to train our agent using model free RL methods -: qlearning, sarsa, expected sarsa\
We plotted the episode number vs time step for the different algorithms\
The plots can be found in assigment 3 folder


