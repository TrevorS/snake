import random

import arcade

from direction import Direction
from settings import SNAKE_LENGTH, SNAKE_TRAVEL


class Snake(arcade.SpriteSolidColor):
    def __init__(self, width, height, color, length):
        super().__init__(width, height, color)

        self.change_x = 0
        self.change_y = 0
        self.direction = Direction.NONE

        self.parts = arcade.SpriteList()

        for _ in range(length):
            self.parts.append(arcade.SpriteSolidColor(width, height, color))

    def grow(self):
        self.parts.append(arcade.SpriteSolidColor(self.width, self.height, self.color))

    def score(self):
        return len(self.parts) - SNAKE_LENGTH

    def check_for_self_collision(self):
        head = self.parts[0]

        tail = arcade.SpriteList()
        tail.extend(self.parts[1:])

        return arcade.check_for_collision_with_list(
            head,
            tail,
        )

    def teleport(self, x, y):
        self.center_x = x
        self.center_y = y

        self.change_x = 0
        self.change_y = 0

        for i, part in enumerate(self.parts):
            part.center_x = x
            part.center_y = y - (i * SNAKE_TRAVEL)
            part.change_x = 0
            part.change_y = 0

        return self

    def draw(self):
        self.parts.draw()

    def update(self):
        if self.direction == Direction.NONE:
            return

        for i in range(len(self.parts) - 1, 0, -1):
            self.parts[i].center_x = self.parts[i - 1].center_x
            self.parts[i].center_y = self.parts[i - 1].center_y

        head = self.parts[0]

        head.center_x += self.change_x
        head.center_y += self.change_y

        self.center_x = head.center_x
        self.center_y = head.center_y

    def go_up(self):
        if Direction.up_down(self.direction):
            return

        self.direction = Direction.UP

        self.change_y = SNAKE_TRAVEL
        self.change_x = 0

    def go_down(self):
        if Direction.up_down(self.direction):
            return

        self.direction = Direction.DOWN

        self.change_y = -SNAKE_TRAVEL
        self.change_x = 0

    def go_left(self):
        if Direction.left_right(self.direction):
            return

        self.direction = Direction.LEFT

        self.change_y = 0
        self.change_x = -SNAKE_TRAVEL

    def go_right(self):
        if Direction.left_right(self.direction):
            return

        self.direction = Direction.RIGHT

        self.change_y = 0
        self.change_x = SNAKE_TRAVEL
