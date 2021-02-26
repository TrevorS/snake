import random

import arcade

from settings import FOOD_HEIGHT, FOOD_WIDTH


class Food(arcade.SpriteSolidColor):
    def random_teleport(self, map_width, map_height):
        # make sure we dont put food on walls
        x = random.randrange(1, map_width - FOOD_WIDTH - 1)
        y = random.randrange(1, map_height - FOOD_HEIGHT - 1)

        self.center_x = x
        self.center_y = y

        return self
