from game_logic import *
import pygame
import sys

# Lars Johnson
# The purpose of this code is to display the board state. 
# It will display the board, the stones, and the stones captured by each player

# screen size is 750(wide) x 850(tall)
window_size = 750
ui_size = 100

margin = 40

cell_size = (window_size - 2 * margin) / (board_size - 1)

stone_radius = cell_size * 0.45

player_turn = 1


def init_display():
    pygame.init()
    screen = pygame.display.set_mode((window_size, window_size + ui_size))
    font = pygame.font.SysFont("Arial", 15)
    return screen, font

def draw_board(screen):
    # draw_board needs to do the following,
    # 1. Fill the background with a board color.
    # 2. Draw the horizontal lines.
    # 3. Draw the vertical lines.

    global window_size, margin, cell_size, board_size

    # 1 - fill the background!!!
    screen.fill((191, 155, 0))

    for i in range(0, board_size):
        pygame.draw.line(screen, "black", (margin + i * cell_size, margin), (margin + i * cell_size, window_size - margin), 1)
        pygame.draw.line(screen, "black", (margin, margin + i * cell_size), (window_size - margin, margin + i * cell_size), 1)



def draw_stones(board, screen):
    # The purpose of this function is to draw the stones onto the board.
    # it will loop through each of the board positions, and depending on what is there, 
    # it will either draw nothing, a black stone, or a white stone.

    global board_size, margin, cell_size, window_size, stone_radius
    for i in range(0, board_size):
        for k in range(0, board_size):
            if board[i][k] == 1:
                pygame.draw.circle(screen, "black", (margin + k * cell_size, margin + i * cell_size), stone_radius)
            elif board[i][k] == 2:
                pygame.draw.circle(screen, "white", (margin + k * cell_size, margin + i * cell_size), stone_radius)


def draw_ui(screen, font):
    global window_size, ui_size, captured_black_stones, captured_white_stones, player_turn
    # The goal of this function is to draw who's turn it is, the number of stones captured of each color,
    # and a pass button for the end of the game. The button will not do anything yet.
    if player_turn == 1:
         player_turn_string = font.render("It is the turn of the black stones!", True, "black")

    elif player_turn == 2:
        player_turn_string = font.render("It is the turn of the white stones!", True, "black")

    screen.blit(player_turn_string, (50, 745))


    # Next: the number of stones captured for each person.
    # Captured Black Stones
    captured_black_stones_string = font.render(f"{captured_black_stones} Black Stones have been captured.", True, "black")
    screen.blit(captured_black_stones_string, (300, 745))

    # Captured White Stones
    captured_white_stones_string = font.render(f"{captured_white_stones} White Stones have been captured.", True, "black")
    screen.blit(captured_white_stones_string, (300, 800))

    # Next, the 'Pass' button will be rendered
    pygame.draw.rect(screen, "white", (535, 740, 180, 75))
    pass_string = font.render("Pass", True, "Black")
    screen.blit(pass_string, (535+77, 740+62/2))

def pixel_to_grid(x, y):
    # This function will be given the coordinates of the click, then convert that pixel to the grid.
    global margin, cell_size, board_size

    col = round((x - margin)/cell_size)
    row = round((y - margin)/cell_size)

    if 0 <= col <= (board_size - 1) and 0 <= row <= (board_size - 1):
        return row, col
    else:
        return None


#def draw_all(board, turn, captures):
def draw_all(board, screen, font):
    draw_board(screen)
    draw_stones(board, screen)
    draw_ui(screen, font)


place_stone(board, 1, 5, 1)

place_stone(board, 1, 4, 2)

place_stone(board, 2, 4, 1)

clock = pygame.time.Clock()
screen, font = init_display()
draw_stones(board, screen)
running = True

while running:
    draw_all(board, screen, font)

    pygame.display.flip()

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
            
