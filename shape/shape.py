
from abc import *
class Shape:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y        
        
    def move(self, offset_x, offset_y):
        self.__y += offset_x
        self.__y += offset_y
        
    @abstractmethod
    def area(self):
        pass

