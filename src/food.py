import random

import arcade

from settings import FOOD_HEIGHT, FOOD_WIDTH


class Food(arcade.SpriteSolidColor):
    def random_teleport(self, map_width, map_height):
        x = random.randrange(0, map_width - FOOD_WIDTH)
        y = random.randrange(0, map_height - FOOD_HEIGHT)

        self.center_x = x
        self.center_y = y

        return self
