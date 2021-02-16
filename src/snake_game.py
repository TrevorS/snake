import arcade

from settings import (
    BACKGROUND_COLOR,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    SCREEN_WIDTH,
    SNAKE_COLOR,
    SNAKE_HEIGHT,
    SNAKE_WIDTH,
)
from snake import Snake


class SnakeGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.snake = None
        self.snakes = None
        self.walls = None
        self.physics_engine = None

        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self):
        self.snakes = arcade.SpriteList()
        self.walls = arcade.SpriteList()

        self.snake = Snake(
            SNAKE_WIDTH,
            SNAKE_HEIGHT,
            SNAKE_COLOR,
        )

        width, height = self.get_size()

        self.snake.center_x = width / 2
        self.snake.center_y = height / 2

        self.snakes.append(self.snake)

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.snake,
            self.walls,
        )

    def on_draw(self):
        arcade.start_render()
        self.snakes.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.snake.go_up()
        elif key == arcade.key.A:
            self.snake.go_left()
        elif key == arcade.key.S:
            self.snake.go_down()
        elif key == arcade.key.D:
            self.snake.go_right()

    def on_update(self, delta_time):
        self.physics_engine.update()
