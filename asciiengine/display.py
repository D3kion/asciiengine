import pygame

from . import Config, Scene


class Display():
    def __init__(self, window, config: Config):
        self._config = config
        self._window = window

        self._font = pygame.font.SysFont(*self._config.FONT_DEFAULT)

        self._font_width, self._font_height = self._font.size('a')
        size = (self._config.DISPLAY_COLS * self._font_width,
                self._config.DISPLAY_ROWS * self._font_height)
        self._display = pygame.Surface(size)

    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, scene: Scene, **kwargs):
        self._scene = scene(self, **kwargs)

    def _draw_display(self):
        window_width, window_height = pygame.display.get_surface().get_size()
        display_position = (
            (window_width - self._display.get_width()) // 2,
            (window_height - self._display.get_height()) // 2
        )

        self._window.blit(self._display, display_position)
        pygame.draw.rect(self._display, (15, 15, 15),
                         (0, 0, window_width, window_height))

    def render(self):
        self._draw_display()
        self._scene.draw()

        label = self._font.render('AAAAAAA', 1, (255, 0, 0))
        self._display.blit(label, (0, 0))
        pygame.display.flip()

    def _get_xy(self, colrow: tuple):
        col, row = colrow
        return (col * self._font_width, row * self._font_height)

    def draw(self, xy: tuple, text: str, color: tuple = (255, 255, 255)):
        label = self._font.render(text, 1, color)
        self._display.blit(label, self._get_xy(xy))

    def box(self, xy: tuple, wh: tuple,
            extra: tuple = ('-', '|', '+', '+', '+', '+')):
        x, y = xy
        w, h = wh
        if w < 3 | h < 3:
            raise ValueError
        # Draw ┌───┐
        self.draw((x, y), extra[2] + extra[0]*(w-2) + extra[3])
        # Draw │   │
        for i in range(y+1, y+h-1):
            self.draw((x, i), extra[1] + ' '*(w-2) + extra[1])
        # Draw └───┘
        self.draw((x, y+h-1), extra[4] + extra[0]*(w-2) + extra[5])
