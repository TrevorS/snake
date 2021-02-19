import arcade

from settings import (
    BACKGROUND_COLOR,
    FOOD_COLOR,
    FOOD_HEIGHT,
    FOOD_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    SCREEN_WIDTH,
    SNAKE_COLOR,
    SNAKE_HEIGHT,
    SNAKE_LENGTH,
    SNAKE_WIDTH,
)
from snake import Food, Snake


class SnakeGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.snake = None
        self.food = None

        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self):
        width, height = self.get_size()

        self.food = Food(
            FOOD_HEIGHT,
            FOOD_WIDTH,
            FOOD_COLOR,
        )
        self.food.random_teleport(width, height)

        self.snake = Snake(
            SNAKE_WIDTH,
            SNAKE_HEIGHT,
            SNAKE_COLOR,
            SNAKE_LENGTH,
        )
        self.snake.teleport(width / 2, height / 2)

    def on_draw(self):
        arcade.start_render()

        self.snake.draw()
        self.food.draw()

    def on_update(self, delta):
        self.snake.update()
        self.food.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.snake.go_up()
        elif key == arcade.key.A:
            self.snake.go_left()
        elif key == arcade.key.S:
            self.snake.go_down()
        elif key == arcade.key.D:
            self.snake.go_right()
        elif key == arcade.key.Q:
            self.close()
