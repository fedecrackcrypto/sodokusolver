import pygame
import sys
import time
from sodoku import *
from main import *

pygame.init()

#Set variables
size = width, height = 1000, 666.66
screen = pygame.display.set_mode(size)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
WHITE = (255, 255, 255)
grid_size = None

OPEN_SANS = "OpenSans-Regular.ttf"
smallFont = pygame.font.Font(OPEN_SANS, 20)
mediumFont = pygame.font.Font(OPEN_SANS, 28)
largeFont = pygame.font.Font(OPEN_SANS, 40)




while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BLACK)
   
    if grid_size is None:

        # Draw title
        title = largeFont.render("Choose the size of the grid", True, WHITE)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Draw buttons
        play9Button = pygame.Rect((width / 8), (height / 2), width / 4, 50)
        play9 = mediumFont.render("9x9", True, BLACK)
        play9Rect = play9.get_rect()
        play9Rect.center = play9Button.center
        pygame.draw.rect(screen, WHITE, play9Button)
        screen.blit(play9, play9Rect)

        play16Button = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
        play9 = mediumFont.render("16x16", True, BLACK)
        play16Rect = play9.get_rect()
        play16Rect.center = play16Button.center
        pygame.draw.rect(screen, WHITE, play16Button)
        screen.blit(play9, play16Rect)

        

        #Check for button click
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if play9Button.collidepoint(mouse):
                time.sleep(0.2)
                grid_size = 9
                sodoku = Sodoku(grid_size)
                sodoku.change_value(0,1,6)
                sodoku.change_value(0,4,7)
                sodoku.change_value(0,7,2)
                sodoku.change_value(1,4,8)
                sodoku.change_value(1,5,3)
                sodoku.change_value(1,7,1)
                sodoku.change_value(1,8,6)
                sodoku.change_value(2,0,9)
                sodoku.change_value(2,3,4)
                sodoku.change_value(2,7,7)
                sodoku.change_value(3,2,5)
                sodoku.change_value(3,3,6)
                sodoku.change_value(3,4,4)
                sodoku.change_value(4,0,8)
                sodoku.change_value(4,1,1)
                sodoku.change_value(4,6,5)
                sodoku.change_value(5,5,2)
                sodoku.change_value(5,6,3)
                sodoku.change_value(6,1,9)
                sodoku.change_value(6,2,3)
                sodoku.change_value(6,5,1)
                sodoku.change_value(6,7,8)
                sodoku.change_value(7,1,7)
                sodoku.change_value(7,6,2)
                sodoku.change_value(8,2,4)
                sodoku.change_value(8,3,5)
                sodoku.change_value(8,4,6)
                sodoku.change_value(8,5,9)
                sodoku.change_value(8,6,1)


                #Show 9x9 grid
            elif play16Button.collidepoint(mouse):
                time.sleep(0.2)
                grid_size = 16
                sodoku = Sodoku(grid_size)
                #Show 16x16 grid
        pygame.display.flip()
        
        

    else:    
  
    # Board parameters

        # AI Move button
        BOARD_PADDING = 20
        solve_button = pygame.Rect(
            (2 / 3) * width + BOARD_PADDING, (1 / 3) * height - 50,
            (width / 3) - BOARD_PADDING * 2, 50
        )
        buttonText = mediumFont.render("Solve Sodoku", True, BLACK)
        buttonRect = buttonText.get_rect()
        buttonRect.center = solve_button.center
        pygame.draw.rect(screen, WHITE, solve_button)
        screen.blit(buttonText, buttonRect)
    
        board_width = ((2 / 3) * width) - (BOARD_PADDING * 2)
        board_height = height - (BOARD_PADDING * 2)
        cell_size = int(min(board_width / grid_size, board_height / grid_size))
        board_origin = (BOARD_PADDING, BOARD_PADDING)
        grid = np.full((grid_size, grid_size), fill_value=None)
        #For alterning colors in pair subgrids
        alternate = False
        iteration = 1
        for i in range(grid_size):
            for j in range(grid_size):
                rect = pygame.Rect(
                    j * cell_size + board_origin[1],
                    i * cell_size + board_origin[0],                    
                    cell_size,
                    cell_size
                )
            
                grid[i][j] = rect
                #For alterning color in grids
                if not alternate:
                    if sodoku.board[i][j].grid%2 == 0:
                        pygame.draw.rect(screen, GRAY, rect)
                        if sodoku.subgrid_size%2 == 0 and (i+1)/iteration == sodoku.subgrid_size and (j+1) == grid_size:
                            alternate = not alternate
                            iteration += 1
                    else:
                        pygame.draw.rect(screen, (45,67,95), rect)
                else:
                    if sodoku.board[i][j].grid%2 == 0:
                        pygame.draw.rect(screen, (45,67,95), rect)
                        if sodoku.subgrid_size%2 == 0 and (i+1)/iteration == sodoku.subgrid_size and (j+1) == grid_size:
                            alternate = not alternate
                            iteration += 1
                    else:
                        pygame.draw.rect(screen, GRAY, rect)
                pygame.draw.rect(screen, WHITE, rect, 3)

                if sodoku.board[i,j].number is not None:
                    number = smallFont.render(
                        str(sodoku.board[i,j].number),
                        True, BLACK
                    )
                    numberTextRect = number.get_rect()
                    numberTextRect.center = rect.center
                    screen.blit(number, numberTextRect)
        pygame.display.flip()
        selected_cell = None
        first_key = True
        left, _, right = pygame.mouse.get_pressed()

        #check for user left click
        if left == 1:
            mouse = pygame.mouse.get_pos()
            #check for user selecting a cell
            if solve_button.collidepoint(mouse):
                solver = SodokuSolver(sodoku)
                solution = solver.solve()
                for variable in solution:
                    print(variable)
                    sodoku.change_value(variable.i,variable.j,solution[variable])


            elif True:
                for i in range(grid_size):
                    for j in range(grid_size):
                        if grid[i][j].collidepoint(mouse):
                            selected_cell = grid[i][j]
                            selected_i = i
                            selected_j = j                            
                            pygame.draw.rect(screen, (47,56,78), selected_cell, 3)
                            pygame.display.flip()
        
        #User has selected a cell to input a number
        number = None
        while selected_cell is not None:            
            for event in pygame.event.get():                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE: 
                        if sodoku.board[selected_i][selected_j] is not None:
                            sodoku.reset_value(selected_i,selected_j)                        
                        selected_cell = None
                        break
                    elif event.unicode.isdigit() and first_key:
                        if int(event.unicode) in range(1, grid_size+1):                            
                            number = event.unicode
                            first_key = False
                            numberRect = smallFont.render(
                                number,
                                True, BLACK
                            )
                            pygame.draw.rect(screen, GRAY, selected_cell)
                            pygame.draw.rect(screen, (47,56,78), selected_cell, 3)
                            numberTextRect = numberRect.get_rect()
                            numberTextRect.center = selected_cell.center
                            screen.blit(numberRect, numberTextRect)
                            pygame.display.flip()
                            continue
                    elif event.unicode.isdigit() and not first_key:
                        if int(number + event.unicode) in range(1, grid_size+1):
                            number = number + event.unicode
                            first_key = True
                        elif int(event.unicode) in range(1, grid_size+1):
                            number = event.unicode
                        numberRect = smallFont.render(
                            number,
                            True, BLACK
                        )
                        pygame.draw.rect(screen, GRAY, selected_cell)
                        pygame.draw.rect(screen, (47,56,78), selected_cell, 3)
                        numberTextRect = numberRect.get_rect()
                        numberTextRect.center = selected_cell.center
                        screen.blit(numberRect, numberTextRect)
                        pygame.display.flip()
                    elif event.key == pygame.K_RETURN:
                        if number is not None:
                            sodoku.change_value(selected_i, selected_j, int(number))
                        selected_cell = None
                        break