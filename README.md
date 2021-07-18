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


