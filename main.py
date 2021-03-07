import numpy as np
board = ["-","-","-",
          "-","-","-",
          "-","-","-"]


#default values
#if game is still going
game_still_going = True

#Who won? or Tie?
winner = None

#random start
start = np.random.rand()

#Whose turn is it?
if start > 0.5:
  current_player = "X"
else:
  current_player = "O"

#turn count
turn = 0


# ------------Functions ------------------#

def display_board(turn):
  start_list = [0,3,6]

  print("\n")
  print("Board at Turn #", turn)
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")

  print("\n")
  



def play_game():
  global turn
  global game_still_going
  #display initial board
  display_board(turn)

  while game_still_going:

    #handle a single turn or an arbitrary player
    handle_turn(current_player)

    #check if the game has ended
    check_if_game_over()

    #flip to the other player
    flip_player()
    turn += 1

  #The game has ended
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")

  



#Handle a single turn of an arbitrary player
def handle_turn(player):
  global turn
  #Get position from player
  print(player + "'s turn.'")

  position = input("Choose a position from 1-9: ")

  #Checking if the input is valid
  valid = False

  while not valid:
    #make sure the input is valid
    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("Choose a position from 1-9: ")

    #Get the correct index of board          
    position = int(position) - 1

    #Make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Choose another position")
  
  #Put the game piece on the board
  board[position] = player

  #show the game board
  display_board(turn)



def check_if_game_over():
  check_for_winner()
  check_if_tie()



def check_for_winner():
  global winner
  #check rows
  row_winner = check_rows()

  #check columns
  column_winner =  check_columns()
  #check diagonals
  diagonal_winner = check_diagonals()

  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None

  

def check_rows():
  #Set global variables
  global game_still_going
  #Check if any of the columns have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  #If any column does have a match, flag that there is a winner
  if row_1 or row_2 or row_3:
    game_still_going = False
    
    #Return the winner
    if row_1:
      return board[0]
    elif row_2:
      return board[3]
    elif row_3:
      return board[6]
  
  #Or return None if there is no winner
  else:
    return None



def check_columns():
  #Set global variables
  global game_still_going
  #Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  #If any column does have a match, flag that there is a winner
  if column_1 or column_2 or column_3:
    game_still_going = False
    
    #Return the winner
    if column_1:
      return board[0]
    elif column_2:
      return board[1]
    elif column_3:
      return board[2]
  
  #Or return None if there is no winner
  else:
    return None



#Check the diagonals for a win 
def check_diagonals():
  #Set global variables
  global game_still_going
  #Check if any of the diagonals have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  
  #If any row does have a match, flag that there is a winner
  if diagonal_1 or diagonal_2:
    game_still_going = False
    
    #Return the winner
    if diagonal_1:
      return board[0]
    elif diagonal_2:
      return board[2]
  
  #Or return None if there is no winner
  else:
    return None


#Check if there is a tie
def check_if_tie():
  #Set global variables
  global game_still_going
  #if board is full
  if "-" not in board:
    game_still_going = False
    return True
  #Else there is no tie
  else:
    return False



def flip_player():
  #global variables we next
  global current_player

  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  
#--------------Start Execution ------------------
#paly a game of tic tac toe
play_game()