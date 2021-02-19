import random

import arcade

from settings import FOOD_HEIGHT, FOOD_WIDTH, SNAKE_LENGTH, UNIT


class Food(arcade.SpriteSolidColor):
    def teleport(self, x, y):
        self.center_x = x
        self.center_y = y

    def random_teleport(self, map_width, map_height):
        x = random.randrange(0, map_width - FOOD_WIDTH)
        y = random.randrange(0, map_height - FOOD_HEIGHT)

        self.center_x = x
        self.center_y = y


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
        for i in range(self.length - 1, 0, -1):
            self.parts[i].x = self.parts[i - 1].x
            self.parts[i].y = self.parts[i - 1].y

        head = self.parts[0]

        head.x += self.change_x
        head.y += self.change_y

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
