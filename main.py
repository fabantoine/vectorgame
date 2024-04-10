# !/usr/bin/env python
# import basic pygame modules
import pygame as pg
from settings import *
from landmark import Landmark
from inbox import Inbox

SCREENRECT = pg.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

def main():

    pg.init()
    clock = pg.time.Clock()
    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pg.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pg.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    landmark = Landmark()
    inbox = Inbox(screen, 50, 450, 100, 40, "Arial", 20)

    # create the background, tile the bgd image
    background = pg.Surface(SCREENRECT.size)
    pg.Surface.fill(background, (125, 50, 50), SCREENRECT)
    screen.blit(background, (0, 0))
    pg.display.flip()
    landmark.draw_landmark(screen)



    # Initialize Game Groups

    while True:
        inbox.draw()
        # get input
        if inbox.x_vector or inbox.y_vector != "":
            landmark.level.vector.coordinates = (inbox.x_vector, inbox.y_vector)
            landmark.level.vector.draw_vector(screen=screen, op=landmark.level.rect_cat.center)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            #if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            #    return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_i:
                    inbox.start_input()
                elif inbox.input_active:
                    inbox.handle_input(event)

        pg.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
    pg.quit()