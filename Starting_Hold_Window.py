# Import pygame. 
import pygame
import sys

# Panel 1 (start holds)
PANEL_1_BOARD_WIDTH = 800
PANEL_2_BOARD_HEIGHT = 300

# Board color: light tan
TAN = (210, 180, 140)

# Initializing the game engine
pygame.init()


# Width and height of the screen
panel_1 = pygame.display.set_mode((PANEL_1_BOARD_WIDTH, PANEL_2_BOARD_HEIGHT))
pygame.display.set_caption("Panel 1; start holds")
panel_1.fill(TAN)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    pygame.display.update()

    
            
