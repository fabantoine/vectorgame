# !/usr/bin/env python
# import basic pygame modules
import pygame as pg
from settings import *
from landmark import Landmark

SCREENRECT = pg.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
landmark = Landmark()
def main():
    pg.init()
    clock = pg.time.Clock()
    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pg.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pg.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    # create the background, tile the bgd image
    background = pg.Surface(SCREENRECT.size)
    pg.Surface.fill(background, (125, 50, 50), SCREENRECT)
    screen.blit(background, (0, 0))
    pg.display.flip()
    landmark.draw_landmark(screen)


    # Initialize Game Groups

    while True:
        # get input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return

        pg.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
    pg.quit()