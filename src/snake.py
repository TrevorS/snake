import arcade

from settings import UNIT


class Snake:
    def __init__(self, width, height, color, length):
        self.width = width
        self.height = height
        self.color = color
        self.length = length

        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0
        self.angle = 0

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x,
            self.center_y,
            self.width,
            self.height,
            self.color,
            self.angle,
        )

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

    def go_up(self):
        self.change_y = 1 * UNIT
        self.change_x = 0

        self.angle = 0

    def go_down(self):
        self.change_y = -1 * UNIT
        self.change_x = 0

        self.angle = 180

    def go_left(self):
        self.change_y = 0
        self.change_x = -1 * UNIT

        self.angle = -90

    def go_right(self):
        self.change_y = 0
        self.change_x = 1 * UNIT

        self.angle = 90
