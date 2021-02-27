from enum import Enum


class Direction(Enum):
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    @classmethod
    def up_down(cls, direction):
        return direction == cls.UP or direction == cls.DOWN

    @classmethod
    def left_right(cls, direction):
        return direction == cls.LEFT or direction == cls.RIGHT
