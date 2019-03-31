class UI:
    def __init__(self, display):
        self._display = display

    def text(self, xy: tuple, color: tuple):
        pass

    def box(self, xy: tuple, wh: tuple,
            extra: tuple = ('-', '|', '+', '+', '+', '+')):
        x, y = xy
        w, h = wh
        if w < 3 | h < 3:
            raise ValueError

        # Draw ┌───┐
        self._display.draw((x, y), extra[2] + extra[0]*(w-2) + extra[3])
        # Draw │   │
        for i in range(y+1, y+h-1):
            self._display.draw((x, i), extra[1] + ' '*(w-2) + extra[1])
        # Draw └───┘
        self._display.draw((x, y+h-1), extra[4] + extra[0]*(w-2) + extra[5])
