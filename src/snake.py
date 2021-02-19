import arcade

from settings import SNAKE_LENGTH, UNIT


class Part:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def generate_parts(cls, x=0, y=0, length=SNAKE_LENGTH):
        return [cls(x, y) for _ in range(length)]


class Snake:
    def __init__(self, width, height, color, length):
        self.width = width
        self.height = height
        self.color = color
        self.length = length

        self.change_x = 0
        self.change_y = 0

        self.parts = Part.generate_parts()

    def teleport(self, x, y):
        self.parts = Part.generate_parts(x, y, self.length)

    def draw(self):
        for part in self.parts:
            arcade.draw_rectangle_filled(
                part.x,
                part.y,
                self.width,
                self.height,
                self.color,
            )

    def update(self):
        # TODO: adjust update to move parts
        for part in self.parts:
            part.x += self.change_x
            part.y += self.change_y

    def go_up(self):
        self.change_y = 1 * UNIT
        self.change_x = 0

    def go_down(self):
        self.change_y = -1 * UNIT
        self.change_x = 0

    def go_left(self):
        self.change_y = 0
        self.change_x = -1 * UNIT

    def go_right(self):
        self.change_y = 0
        self.change_x = 1 * UNIT
