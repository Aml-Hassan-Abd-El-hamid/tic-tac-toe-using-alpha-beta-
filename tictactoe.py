"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    for i in range(0,3):
        for j in range(0, 3):
            if board[i][j] == X:
                x += 1
            elif board[i][j] == O:
                o += 1
    if x > o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    Actions = set()

    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == EMPTY:
                Actions.add((i, j))

    return Actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Create new board, without modifying the original board received as input
    if  board[action[0]][action[1]] != EMPTY:
          raise Exception("Sorry, that cell isn't empyt")
    r= copy.deepcopy(board)
    r[action[0]][action[1]] = player(board)
    return r


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Rows:
    if board[0].count(X) == 3 or board[1].count(X) == 3 or board[2].count(X) == 3 :
        return X
    if board[0].count(O) == 3 or board[1].count(O) == 3 or board[2].count(O) == 3:
        return O
    #Columns:
    for j in range(3):
      column = ''
      for i in range(3):
        column += str(board[i][j])
      if column == 'XXX':
        return X
      if column == 'OOO':
        return O
    #Diagonals:
    diag1 = ''
    diag2 = ''
    j = 2
    for i in range(3):
      diag1 += str(board[i][i])
      diag2 += str(board[i][j])
      j -= 1
    if diag1 == 'XXX' or diag2 == 'XXX':
      return X
    elif diag1 == 'OOO' or diag2 == 'OOO':
      return O
    #nobody won
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) == "X" or winner(board)=="O":
        return True
    elif board[0].count(EMPTY)+board[1].count(EMPTY)+board[2].count(EMPTY)==0:
        return True
    else:
        return False
    #return True if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None) else False # noqa E501


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    # Check how to handle exception when a non terminal board is received.


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board)==X:
        v,move=maxi(board,-math.inf,math.inf)    
    else:
        v,move=mini(board,-math.inf,math.inf)
    return move

def maxi(board,alpha,beta):
    if terminal(board):
        return utility(board),None
    
    maxval=-math.inf
    actionss=actions(board)
    move=None
    for act in actionss:
        val,a=mini(result(board,act),alpha,beta)
        if maxval<val:
            maxval=val
            move=act
        if val==1:
            return val,act
        alpha=max(alpha,val) 
        if beta<=alpha:
            break  
    return maxval,move
    
def mini(board,alpha,beta):
    if terminal(board):
        return utility(board),None
    minval=math.inf
    actionss=actions(board)
    move=None
    for act in actionss:
        val,a=maxi(result(board,act),alpha,beta)
        if minval>val:
            minval=val
            move=act  
        if val==-1:
            return val,act
        beta=min(beta,val)
        if beta<=alpha:
            break   
    return minval,move