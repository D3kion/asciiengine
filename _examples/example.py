import sys
from random import randrange

import pygame
from ascii_engine import Display
from ascii_engine.ui import Scene, Drawer


if __name__ == '__main__':
    display = Display()
    display.scene = MenuScene

    while True:
        display.handle_events()
        display.render()

class MenuScene(Scene):
    def __init__(self, drawer: Drawer, **kwargs):
        super().__init__(drawer, **kwargs)

        self.current_choice = 1

    def handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._handle_keys(event)

    def _handle_keys(self, event):
        if event.key in (pygame.K_DOWN, pygame.K_s):
            if self.current_choice < 4:
                self.current_choice += 1
        elif event.key in (pygame.K_UP, pygame.K_w):
            if self.current_choice > 0:
                self.current_choice -= 1
        elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
            if self.current_choice == 4:
                sys.exit()

    def draw(self):
        self.drawer.box((0, 0), (80, 35))
        self.drawer.box((29, 12), (21, 3))
        self.drawer.box((29, 14), (21, 8))

        self.drawer.draw((35, 13), 'ASCII-ENGINE')
        self.drawer.draw((34, 16), 'Item 1')
        self.drawer.draw((34, 17), 'Item 2')
        self.drawer.draw((34, 18), 'Item 3')
        self.drawer.draw((34, 19), 'Exit')

        self._draw_pointer()

    def _draw_pointer(self):
        pos = (
            (32, 16),
            (32, 17),
            (32, 18),
            (32, 19),
        )

        if not self.current_choice:
            color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
            self.drawer.draw((35, 13), 'ASCII-ENGINE', color)
        else:
            self.drawer.draw(pos[self.current_choice-1], '>', (0, 63, 0))
