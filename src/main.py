import arcade

from snake import Snake
from snake_game import SnakeGame


def main():
    window = SnakeGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
