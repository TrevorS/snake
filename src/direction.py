from enum import Enum


class Direction(Enum):
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    @classmethod
    def unchanged(cls, current, new):
        ud, lr = (cls.UP, cls.DOWN), (cls.LEFT, cls.RIGHT)

        return current in ud and new in ud or current in lr and new in lr


DELTA = {
    Direction.NONE: (0, 0),
    Direction.UP: (0, 1),
    Direction.DOWN: (0, -1),
    Direction.LEFT: (-1, 0),
    Direction.RIGHT: (1, 0),
}


def get_delta(direction):
    return DELTA[direction]
