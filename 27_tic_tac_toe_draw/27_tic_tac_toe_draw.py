#!/usr/bin/python3

MAX_X = 3
MAX_Y = 3

ERROR_MSG_NO_COMMA = "ERROR: There is no , in the input!"
ERROR_MSG_ONLY_XY = "ERROR: Only X and Y coordinates are needed!"
ERROR_MSG_NUMERIC = "ERROR: Inputs should be numeric!"
ERROR_MSG_X_BETWEEN = "ERROR: X should be between 1 and "
ERROR_MSG_Y_BETWEEN = "ERROR: Y should be between 1 and "

INPUT_MSG = "Please enter X and Y coordinates - [x,y]: "

def input_checker(input_string, range_x, range_y):
  error_flag = True
  is_numeric_flag = True

  if "," not in input_string:
    print(ERROR_MSG_NO_COMMA)
    error_flag = False

  splitted_input = input_string.split(",")
  
  if len(splitted_input) > 2:
    print(ERROR_MSG_ONLY_XY)
    error_flag = False

  if (splitted_input[0].isnumeric() == False) or (splitted_input[1].isnumeric() == False):
    print(ERROR_MSG_NUMERIC)
    is_numeric_flag = False
    error_flag = False
	
  if is_numeric_flag == False or range_x < int(splitted_input[0]) or int(splitted_input[0]) < 1:
    print(ERROR_MSG_X_BETWEEN + str(range_x))
    error_flag = False

  if is_numeric_flag == False or range_y < int(splitted_input[1]) or int(splitted_input[1]) < 1:
    print(ERROR_MSG_Y_BETWEEN + str(range_y))
    error_flag = False

  if error_flag == False:
    return False
  else:
    return splitted_input

def input_handler():
  value = str(input(INPUT_MSG))
  
  result = input_checker(value, MAX_X, MAX_Y)
  
  if result != False:
    numeric_result = [int(result[0]), int(result[1])]
    return numeric_result

  return False

def update_game(game, player, x, y):
  new_game = game
  new_game[x-1][y-1] = player
  
  return new_game

game = [[0, 0, 0],
	    [0, 0, 0],
	    [0, 0, 0]]

print(game)

x_y_input = input_handler()
if x_y_input != False:
  game = update_game(game, 1, x_y_input[0], x_y_input[1])

print(game)