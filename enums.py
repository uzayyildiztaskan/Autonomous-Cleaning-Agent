from enum import Enum

class Grid_State(Enum):
    FREE = 0
    OBSTACLE = 1    
    UNKOWN = 2
    CLEANED = 3

class Directions(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)