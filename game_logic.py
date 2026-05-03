


# Lars Johnson
# The goal of this program is to make the basic rules for the game of go.
# This will involve making a basic board state and the placements of pieces
# additionally, the basic board state should also be printed

board_size = 9

captured_black_stones = 0
captured_white_stones = 0


# This code will place a stone on the board, no rules applied at this moment...
def place_stone(game_board, row, column, player):
    game_board[row - 1][column - 1] = player
    handle_captures(game_board, (row-1), (column-1))


# The goal of this function is to print the board state with either a ., a B, or a W.
# Pretty cool stuff!!!
def print_board(game_board, board_size):
    for i in range(0,board_size):
        for j in range(0, board_size):
            if game_board[i][j] == 0:
                print(".", end=" ")
            elif game_board[i][j] == 1:
                print("B", end=" ")
            elif game_board[i][j] == 2:
                print("W", end=" ")
            else:
                print(" ", end=" ")

        print("")

# Next, we need to make an iterative function to find the liberties for a specific go pieces
def find_liberties(game_board, row, column):
    # need to first determine which piece the selected position holds
    color = game_board[row][column]
    
    group = [(row, column)]

    liberties = set()

    just_the_group = [(row, column)]

    visited = {(row, column)}

    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # now we need to do a loop for the beginning piece, if it is able to find more pieces throughout the process we need to somehow search those pieces as well
    while len(group) > 0:

        #print(f"{game_board[group[0][0]][group[0][1]]}")
        #print(f"{game_board[group[0][0]+1][group[0][1]]}")

        current = group.pop(0)

        r, c = current      # Gives the row of the stone
        # Gives the column of the stone 


        # next we need determine which spaces we need to search
        for i in range(0, len(offsets)):
            neighbor = ((offsets[i][0] + r), (offsets[i][1] + c))
            # Now we have a list of neighbors of the stone

            if (neighbor[0] >= 0) and (neighbor[0] < board_size) and (neighbor[1] < board_size) and (neighbor[1] >= 0): # neighbor is now in the range of the board!!!
                # Next we check if we have already visited the neighbor
                if ((neighbor[0], neighbor[1])) not in visited:
                    visited.add((neighbor[0], neighbor[1]))
                    if game_board[neighbor[0]][neighbor[1]] == color:
                        group.append((neighbor))
                        just_the_group.append((neighbor))
                    elif game_board[neighbor[0]][neighbor[1]] == 0:
                        liberties.add((neighbor))

    return liberties, just_the_group


# Now, we need a function to handle captures...
# If a stone has 0 liberties around it, it should then be taken off the board and the size of the group should be added to a counter...
def handle_captures(game_board, row, column):
    placed_stone_color = game_board[row][column]

    global captured_white_stones, captured_black_stones

    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    
    # Now 
    for i in range(0, len(offsets)):        # For each of the neighbors

        # Check to see if the neighbors are in valid positions...
        if offsets[i][0] + row >= 0 and offsets[i][0] + row < board_size and offsets[i][1] + column >= 0 and offsets[i][1] + column < board_size:
            neighbor = ((offsets[i][0] + row), (offsets[i][1] + column))
            # Now we need to see if the neighbors are of the opposite color
            if (game_board[neighbor[0]][neighbor[1]] != placed_stone_color) and (game_board[neighbor[0]][neighbor[1]] != 0):
                # Frpm this position, we now need to find out if this stone of the opposite color has zero liberties...

                liberties, group = find_liberties(game_board, neighbor[0], neighbor[1])
                # !!!!! Reminder that the liberties and group have starting index at 0, so this may be confusing...


                # now we need to handle if the number of liberties are 0...
                if len(liberties) == 0:

                    if placed_stone_color == 1:
                        captured_white_stones = captured_white_stones + len(group)
                    elif placed_stone_color == 2:
                        captured_black_stones = captured_black_stones + len(group)

                    for stones in group: # Capture the stones!!!
                        game_board[stones[0]][stones[1]] = 0

                    

                    print(f"This is how many black stones captured :{captured_black_stones}")
                    print(f"This is how many white stones captured :{captured_white_stones}")

                    # For this we need to get rid of the group with 0 liberties!!!
                    #... But how?

def legal_move(game_board, row, column):
    # there are two things we need to do in this function...
    # the first is to prevent the stone from being placed on an already placed stone
    # The second is to prevent the stone from being immediately killed...
    # The second one is the hard one...

    







# First: creating the basic board state.

board = [[0] * board_size for i in range(board_size)]

place_stone(board, 2, 7, 1)

place_stone(board, 3, 4, 2)
place_stone(board, 2, 5, 2)

place_stone(board, 3, 6, 2)
place_stone(board, 4, 5, 2)

place_stone(board, 4, 4, 1)
place_stone(board, 4, 6, 1)
place_stone(board, 5, 5, 1)

print_board(board, board_size)

place_stone(board, 3, 5, 1)

print_board(board, board_size)

