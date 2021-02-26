import arcade


class Wall(arcade.SpriteSolidColor):
    @classmethod
    def generate_walls(cls, map_width, map_height, width, height, color):
        walls = arcade.SpriteList(is_static=True, use_spatial_hash=True)

        # left and right
        for y in range(map_height):
            left = cls(width, height, color)

            left.center_x = 0
            left.center_y = y

            right = cls(width, height, color)

            right.center_x = map_width - 1
            right.center_y = y

            walls.append(left)
            walls.append(right)

        # top and bottom
        for x in range(map_width):
            top = cls(width, height, color)

            top.center_x = x
            top.center_y = map_height - 1

            bottom = cls(width, height, color)

            bottom.center_x = x
            bottom.center_y = 0

            walls.append(top)
            walls.append(bottom)

        return walls
