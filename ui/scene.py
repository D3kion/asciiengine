import sys
from abc import ABC, abstractmethod

from . import Drawer


class Scene(ABC):
    def __init__(self, drawer: Drawer, **kwargs):
        self.drawer = drawer

    # def loop(self):
    #     self.running = True
    #     while self.running:
    #         self._handle_events()
    #         self._draw()
    #         self.display.render()
    #         self.clock.tick(10)

    @abstractmethod
    def handle_events(self):
        raise NotImplementedError

    @abstractmethod
    def draw(self):
        raise NotImplementedError
