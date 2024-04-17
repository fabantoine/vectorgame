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
    inbox = Inbox(screen, 250, 350, 100, 40, "Arial", 20)
    clikable_surface = pg.Rect(inbox.x, inbox.y, inbox.width, inbox.height)
    # create the background, tile the bgd image
    background = pg.Surface(SCREENRECT.size)
    pg.Surface.fill(background, (125, 50, 50), SCREENRECT)
    #screen.blit(background, (0, 0))
    #pg.display.flip()
    #landmark.draw_landmark(screen)



    # Initialize Game Groups

    while True:
        screen.blit(background, (0, 0))
        landmark.draw_landmark(screen)
        inbox.draw()
        # get input
        if inbox.x_vector or inbox.y_vector != "":
            landmark.level.vector.coordinates = (inbox.x_vector, inbox.y_vector)
            landmark.level.vector.draw_vector(screen=screen, op=landmark.level.init_pos_cat)
            if not landmark.level.animation.is_animated and landmark.level.vector.is_defined:
                landmark.level.animation.set_end((landmark.level.rect_cat.center[0]+inbox.x_vector*offset_grid,
                                                landmark.level.rect_cat.center[1]-inbox.y_vector*offset_grid))
                landmark.level.animation.is_animated = True
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if clikable_surface.collidepoint(event.pos):
                        inbox.start_input()
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