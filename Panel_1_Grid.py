import pygame, sys
import Homewall_Constants


def get_hold_color(hold_type):
    hold_color = Homewall_Constants.TAN
    if hold_type == "h":
        hold_color = Homewall_Constants.PINK
    if hold_type == "o":
        hold_color = Homewall_Constants.GRAY
    if hold_type == "s":
        hold_color = Homewall_Constants.GREEN
    return hold_color

def draw_panel_1(panel_1, holds):
    for j, hold in enumerate(holds):
        for i, hold_type in enumerate(hold):
            rect_hold = pygame.Rect(i*Homewall_Constants.HOLD_WIDTH, j*Homewall_Constants.HOLD_HEIGHT, Homewall_Constants.HOLD_WIDTH, Homewall_Constants.HOLD_HEIGHT)
            pygame.draw.rect(panel_1, get_hold_color(hold_type), rect_hold)


def hold_loop(panel_1, hold_layout):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        draw_panel_1(panel_1, hold_layout)
        pygame.display.update()


def initialize_prob():
    pygame.init()
    panel_1 = pygame.display.set_mode((Homewall_Constants.PANEL_1_BOARD_WIDTH, Homewall_Constants.PANEL_2_BOARD_HEIGHT))
    pygame.display.set_caption(Homewall_Constants.TITLE)
    panel_1.fill(Homewall_Constants.TAN)
    return panel_1


def draw_hold_layout(LAYOUTFILE):
    with open(LAYOUTFILE, 'r') as f:
        hold_layout = f.readlines()
    hold_layout = [line.strip() for line in hold_layout]
    return(hold_layout)

def main():
    hold_layout = draw_hold_layout(Homewall_Constants.LAYOUTFILE)
    panel_1 = initialize_prob()
    hold_loop(panel_1, hold_layout)
    

if __name__=="__main__":
    main()