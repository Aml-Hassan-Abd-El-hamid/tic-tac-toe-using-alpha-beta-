# Tic Tac Toe using alpha beta

that is my solution for problem tic tac toe from project 0 from the ai50 cource<br>
that's a link to the problem : https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/ <br>
Note : you need to run the commond ( pip3 install -r requirements.txt ) to install the required Python package (pygame) for this code to run with no problems. <br>
I added 2 additional helper functions to tictactoe.py: maxi and mini, maxi for the X player and mini for the O player, and called them in the orginal function minimax. I used the alpha beta pruning to help the code run faster.<br>
I also added an extra condition to help making things even faster, the condition force the max player to stop once it found a one as it can't get a better result and force the min player to stop once it found minus one as it can't get a better result.
