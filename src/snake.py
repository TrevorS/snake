import random

import arcade

from settings import SNAKE_LENGTH, UNIT


class Snake(arcade.SpriteSolidColor):
    def __init__(self, width, height, color, length):
        super().__init__(width, height, color)

        self.change_x = 0
        self.change_y = 0
        self.length = length

        self.parts = arcade.SpriteList()

        for _ in range(length):
            self.parts.append(arcade.SpriteSolidColor(width, height, color))

    def teleport(self, x, y):
        self.center_x = x
        self.center_y = y

        self.change_x = 0
        self.change_y = 0

        for part in self.parts:
            part.center_x = x
            part.center_y = y
            part.change_x = 0
            part.change_y = 0

    def draw(self):
        self.parts.draw()

    def update(self):
        for i in range(self.length - 1, 0, -1):
            self.parts[i].center_x = self.parts[i - 1].center_x
            self.parts[i].center_y = self.parts[i - 1].center_y

        head = self.parts[0]

        head.center_x += self.change_x
        head.center_y += self.change_y

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
