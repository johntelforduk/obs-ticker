# Scrolling ticker for OBS.

import pygame

ticker_colour = [255, 255, 255]         # White.
background_colour = [0, 255, 0]         # Green (chroma key colour).
screen_size = [1280, 720]               # Set the height and width of the window.
ticker_dist_from_bottom = 70            # Number of pixels that ticker is away from bottom of window.
target_fps = 100                        # Adjust this to speed up / slow down scrolling.


pygame.init()                           # Initialize the game engine.

# NOFRAME means it the green window won't have a title bar at the top.
screen = pygame.display.set_mode(screen_size, pygame.NOFRAME)

clock = pygame.time.Clock()

pygame.font.init()
ticker_font = pygame.font.SysFont('Courier New', 30)

text_offset = 0

done = False

while not done:
    clock.tick(target_fps)

    screen.fill(background_colour)

    for event in pygame.event.get():  # User did something.
        if event.type == pygame.QUIT:  # If user closed window.
            done = True  # Flag that we are done so we exit this loop, and quit the ticker.

    text_surface = ticker_font.render('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum', False, ticker_colour)
    screen.blit(text_surface, (text_offset, screen_size[1] - ticker_dist_from_bottom))

    text_offset -= 1                    # Scroll the text 1 pixel to the left.

    pygame.display.flip()

pygame.quit()
