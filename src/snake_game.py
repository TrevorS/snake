import arcade

from food import Food
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
    WALL_COLOR,
    WALL_HEIGHT,
    WALL_WIDTH,
)
from snake import Snake
from wall import Wall


class SnakeGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.snake = None
        self.foods = None
        self.snakes = None
        self.walls = None

        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self):
        width, height = self.get_size()

        self.foods = arcade.SpriteList()
        self.snakes = arcade.SpriteList()

        food = Food(
            FOOD_HEIGHT,
            FOOD_WIDTH,
            FOOD_COLOR,
        ).random_teleport(width, height)
        self.foods.append(food)

        self.snake = Snake(
            SNAKE_WIDTH,
            SNAKE_HEIGHT,
            SNAKE_COLOR,
            SNAKE_LENGTH,
        ).teleport(width / 2, height / 2)
        self.snakes.append(self.snake)

        self.walls = Wall.generate_walls(
            width,
            height,
            WALL_WIDTH,
            WALL_HEIGHT,
            WALL_COLOR,
        )

    def on_draw(self):
        arcade.start_render()

        self.foods.draw()
        self.snake.draw()
        self.walls.draw()

    def on_update(self, delta):
        self.foods.update()
        self.snakes.update()
        self.walls.update()

        wall_hit_list = arcade.check_for_collision_with_list(
            self.snake,
            self.walls,
        )

        if len(wall_hit_list) > 0:
            print("You hit a wall")
            self.close()

        food_hit_list = arcade.check_for_collision_with_list(
            self.snake,
            self.foods,
        )

        for food in food_hit_list:
            print(f"You ate a food, score: {self.snake.score()}")
            food.remove_from_sprite_lists()

            width, height = self.get_size()

            new_food = Food(
                FOOD_HEIGHT,
                FOOD_WIDTH,
                FOOD_COLOR,
            ).random_teleport(width, height)

            self.foods.append(new_food)

            self.snake.grow()

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
