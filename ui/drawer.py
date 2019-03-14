class Drawer:
    def __init__(self, display):
        self.display = display

    def _get_xy(self, colrow: tuple):
        col, row = colrow
        return (col * self.display.font_width, row * self.display.font_height)

    def draw(self, xy: tuple, text: str, color: tuple = (255, 255, 255)):
        label = self.display.font.render(text, 1, color)
        self.display.screen.blit(label, self._get_xy(xy))

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
