# Scrolling ticker for OBS.

import sys
import pygame

ticker_colour = [255, 255, 255]         # White.
background_colour = [0, 255, 0]         # Green (chroma key colour).
screen_size = [1280, 720]               # [width, height].
ticker_dist_from_bottom = 70            # Number of pixels that ticker is away from bottom of window.
font_size = 30                          # Size of the scrolling ticker.
target_fps = 100                        # Adjust this to speed up or slow down scrolling.
font_factor = 0.6                       # font_factor = width of character in pixels / font_size.

# Read contents of parm filename into text variable.
filename = sys.argv[1]
f = open(filename)
text = f.read()

# TODO Make the text loop once it has scrolled all the way to the left.
ticker_text = text

pygame.init()                           # Initialize the game engine.

# NOFRAME means it the green window won't have a title bar at the top.
screen = pygame.display.set_mode(screen_size, pygame.NOFRAME)

clock = pygame.time.Clock()

pygame.font.init()
ticker_font = pygame.font.SysFont('Courier New', font_size)

text_offset = 0

done = False

while not done:
    clock.tick(target_fps)

    screen.fill(background_colour)

    for event in pygame.event.get():        # User did something.
        if event.type == pygame.QUIT:       # If user closed window.
            done = True                     # Flag that we are done so we exit this loop, and quit the ticker.

    text_surface = ticker_font.render(ticker_text, False, ticker_colour)
    screen.blit(text_surface, (text_offset, screen_size[1] - ticker_dist_from_bottom))

    pygame.display.flip()

    text_offset -= 1                        # Scroll the text 1 pixel to the left.
    if text_offset < - len(ticker_text) * font_size * font_factor:
        text_offset = 0

pygame.quit()
