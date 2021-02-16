import arcade

from settings import UNIT


class Snake(arcade.Sprite):
    def __init__(self, width, height, color):
        super().__init__()

        self.head = arcade.SpriteSolidColor(
            width,
            height,
            color,
        )

        self.body = arcade.SpriteList()
        self.body.append(self.head)

        # get errors if i don't set the texture here
        self.texture = self.head.texture

    def on_draw(self):
        self.body.draw()

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

    def grow(self):
        self.height += 1 * UNIT
