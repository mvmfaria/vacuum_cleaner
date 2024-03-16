import pygame
import numpy as np

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("vaccum cleaner simulator")

dark_purple = (34, 9, 44)
dark_red = (135, 35, 65)
red = (190, 49, 68)
orange = (240, 89, 65)

font_path = "./v2/joystix monospace.ttf"
big_font = pygame.font.Font(font_path, 15)
medium_font = pygame.font.Font(font_path, 10)

fps = 10
clock = pygame.time.Clock()

#enviroment that eventually will come from another file. set an maximum size, like 6 x 6 maybe?
enviroment_state = np.random.randint(2, size=(3, 3))

def writing_basic_information():
    title_text = f"automatic vaccum cleaner"
    text_surface = big_font.render(title_text, True, 'white')
    text_x, text_y = 230, 27
    screen.blit(text_surface, (text_x, text_y))

    pygame.draw.rect(screen, orange, (230, 60, 21, 21))
    agent_text = "simple agent (reflexive)"
    text_surface = medium_font.render(agent_text, True, orange)
    text_x, text_y = 260, 64
    screen.blit(text_surface, (text_x, text_y))

    pygame.draw.rect(screen, dark_red, (230, 90, 21, 21))
    dirty_square_text = "dirty square"
    text_surface = medium_font.render(dirty_square_text, True, dark_red)
    text_x, text_y = 260, 94
    screen.blit(text_surface, (text_x, text_y))

    pygame.draw.rect(screen, red, (230, 120, 21, 21))
    clean_square_text = "clean square"
    text_surface = medium_font.render(clean_square_text, True, red)
    text_x, text_y = 260, 124
    screen.blit(text_surface, (text_x, text_y))

def writing_simulation_information():
    title_text = f"simulation information"
    text_surface = big_font.render(title_text, True, 'white')
    text_x, text_y = 230, 220
    screen.blit(text_surface, (text_x, text_y))

    spent_enrgy_text = f"spent energy: "
    text_surface = medium_font.render(spent_enrgy_text, True, 'yellow')
    text_x, text_y = 230, 250
    screen.blit(text_surface, (text_x, text_y))

def drawning_environment(enviroment_state, vaccum_cleaner_position):
    pygame.draw.rect(screen, 'white', (28, 28, 183, 183), 1)
    for i in range(enviroment_state.shape[0]):
        for j in range(enviroment_state.shape[1]):
            element = enviroment_state[i, j]
            if element:
                pygame.draw.rect(screen, dark_red, ((i+1)*30, (j+1)*30, 29, 29))
            else:
                pygame.draw.rect(screen, red, ((i+1)*30, (j+1)*30, 29, 29))
    pygame.draw.rect(screen, orange, ((vaccum_cleaner_position[0]+1)*34, (vaccum_cleaner_position[1]+1)*34, 21, 21))

running = True
while running:

    enviroment_state = np.random.randint(2, size=(6, 6))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(dark_purple)

    drawning_environment(enviroment_state, (0, 0))

    writing_basic_information()

    writing_simulation_information()

    pygame.display.update()

    clock.tick(fps)