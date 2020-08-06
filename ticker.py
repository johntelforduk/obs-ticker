# Scrolling ticker for OBS.

import sys
import pygame


ticker_colour = [255, 255, 255]         # White.
background_colour = [0, 255, 0]         # Green (chroma key colour).
screen_size = [1280, 720]               # [width, height].
ticker_dist_from_bottom = 70            # Number of pixels that ticker is away from bottom of window.
font_size = 30                          # Size of the scrolling ticker.
font_factor = 0.6  # font_factor = width of character in pixels / font_size.
target_fps = 100                        # Adjust this to speed up or slow down scrolling.


def text_length_in_pixels(this_text: str, font_point_size: int) -> int:
    """For parm text string, return its width in number of pixels if it is rendered in parm font size."""
    return round(len(this_text) * font_point_size * font_factor)


# Read contents of parm filename into text variable.
filename = sys.argv[1]
f = open(filename)
text = f.read()

# TODO Make short text repeat so it fills screen.

# TODO Add spaces to start of text, so it starts scrolling from right hand side of screen.
leading_spaces_needed = int(1 + screen_size[0] / (font_size * font_factor))
print(leading_spaces_needed)



ticker_text = ' ' * leading_spaces_needed + text

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

    # If all of the text has scrolled off left of screen, then reset the ticker.
    if text_offset < - text_length_in_pixels(ticker_text, font_size):
        text_offset = 0

pygame.quit()
