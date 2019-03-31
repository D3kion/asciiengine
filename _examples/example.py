from random import randrange

from asciiengine import Engine, Scene


class MenuScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.current_choice = 0

    def handle_events(self):
        pass
        # for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             sys.exit()
        #         elif event.type == pygame.KEYDOWN:
        #             self._handle_keys(event)

    # def _handle_keys(self, event):
    #     if event.key in (pygame.K_DOWN, pygame.K_s):
    #         if self.current_choice < 4:
    #             self.current_choice += 1
    #     elif event.key in (pygame.K_UP, pygame.K_w):
    #         if self.current_choice > 0:
    #             self.current_choice -= 1
    #     elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
    #         if self.current_choice == 4:
    #             sys.exit()

    def draw(self, display):
        display.ui.box((0, 0), (80, 35))
        display.ui.box((29, 12), (21, 3))
        display.ui.box((29, 14), (21, 8))

        display.draw((33, 13), 'ASCII-ENGINE')
        display.draw((34, 16), 'Item 1')
        display.draw((34, 17), 'Item 2')
        display.draw((34, 18), 'Item 3')
        display.draw((34, 19), 'Exit')

        self._draw_pointer(display)

    def _draw_pointer(self, display):
        pos = (
            (32, 16),
            (32, 17),
            (32, 18),
            (32, 19),
        )

        if not self.current_choice:
            color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
            display.draw((33, 13), 'ASCII-ENGINE', color)
        else:
            display.draw(pos[self.current_choice-1], '>', (0, 63, 0))


if __name__ == '__main__':
    eng = Engine()
    eng.scene = MenuScene

    while True:
        eng.render()
        eng._clock.tick(10)
