#!/usr/bin/env python
# coding: utf-8

# In[2]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[3]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)
display_board(test_board)


# In[4]:


def player_input():
    
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = ''
    while marker !='X' and marker != 'O':
        marker = input('Player1 choose X or O: ').upper()
        
    if marker == 'X':
        return('X','O')
    else:
        return('O', 'X')        


# In[7]:


player1_marker,player2_marker = player_input()


# In[8]:


player2_marker


# In[9]:


def place_marker(board, marker, position):
    board[position] = marker


# In[10]:


test_board


# In[11]:


def win_check(board, mark):
    return((board[1]==mark and board[2]==mark and board[3]==mark) or
          (board[4]==mark and board[5]==mark and board[6]==mark) or
          (board[7]==mark and board[8]==mark and board[9]==mark) or
          (board[7]==mark and board[4]==mark and board[1]==mark) or
          (board[8]==mark and board[5]==mark and board[2]==mark) or
          (board[9]==mark and board[6]==mark and board[3]==mark) or
          (board[1]==mark and board[5]==mark and board[9]==mark) or
          (board[3]==mark and board[5]==mark and board[7]==mark))


# In[12]:


win_check(test_board, 'X')


# In[13]:


import random
def choose_first():
    
    flip = random.randint(0,1)
    if flip==0:
        return 'Player1'
    else:
        return 'Player2'


# In[14]:


def space_check(board, position):
    return board[position] == ' '


# In[15]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[16]:


def player_choice(board):
    position=0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose position: (1-9)'))
    
    return position


# In[17]:


def replay():
    
    choice = input("Play again? Enter yes or no: ")
    return choice == 'yes'


# In[18]:


# While to keep the game running
print('Welcome to tic tac toe')

while True:
    
    # Play the game
    ## Set everything up (BOARD, WHOS FIRST, CHOOSE MARKERS X,O )
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn+' will go first')
    
    play_game = input('Ready to play? y or n?')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    ## Game Play
    
    while game_on:
        if turn == 'Player 1':
            
            # Show the board
            display_board(the_board)
            
            # Choose the position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player1_marker, position)
            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print(' Player 1 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE Game")
                    game_on = False
                else:
                    turn = 'Player 2'
        
        else:
             # Show the board
            display_board(the_board)
            
            # Choose the position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player2_marker, position)
            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print(' Player 2 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE Game")
                    game_on = False
                else:
                    turn = 'Player 1'    
    
    if not replay():
        break
    # Break out of the while loop on replay()


# In[ ]:




