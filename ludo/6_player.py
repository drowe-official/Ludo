import arcade
import pymunk
import os
import random

players = [1, 2, 3, 4, 5, 6]
player_count = len(players)
sprite_count = player_count * 4

screen_width = 700
screen_height = 700
screen_title = "Ludo"

sprite_list = [["blue_sprite1.png", "blue_sprite2.png", "blue_sprite3.png", "blue_sprite4.png"],
               ["orange_sprite1.png", "orange_sprite2.png", "orange_sprite3.png", "orange_sprite4.png"],
               ["green_sprite1.png", "green_sprite2.png", "green_sprite3.png", "green_sprite4.png"],
               ["red_sprite1.png", "red_sprite2.png", "red_sprite3.png", "red_sprite4.png"],
               ["purple_sprite1.png", "purple_sprite2.png", "purple_sprite3.png", "purple_sprite4.png"],
               ["yellow_sprite1.png", "yellow_sprite2.png", "yellow_sprite3.png", "yellow_sprite4.png"]]


class PhysicsSprite(arcade.Sprite):

    def __init__(self, pymunk_shape, filename):
        super().__init__(filename, center_x=pymunk_shape.body.position.x, center_y=pymunk_shape.body.position.y)
        self.pymunk_shape = pymunk_shape


class BoxSprite(PhysicsSprite):

    def __init__(self, pymunk_shape, filename, width, height):
        super().__init__(pymunk_shape, filename)
        self.width = width
        self.height = height


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Setting up the physics of the pieces
        self.space = pymunk.Space()
        self.space.gravity = (0.0, 0.0)

        # Setting up the ability to drag pieces
        self.piece_being_dragged = None
        self.last_mouse_position = 0, 0

        self.background = None

        self.player_list: arcade.SpriteList[PhysicsSprite] = arcade.SpriteList()

        self.roll = None

        self.static_lines = []

        pos_x = 350
        pos_y = 110
        count = 0

        # Setting the start positions for the pieces
        for k in range(player_count):

            if count == 0:

                self.place_pieces(count, pos_x, pos_y)

                count += 1

            elif count == 1:

                pos_x = 570
                pos_y = 230

                self.place_pieces(count, pos_x, pos_y)

                count += 1

            elif count == 2:

                pos_x = 570
                pos_y = 485

                self.place_pieces(count, pos_x, pos_y)

                count += 1

            elif count == 3:

                pos_x = 350
                pos_y = 600

                self.place_pieces(count, pos_x, pos_y)

                count += 1

            elif count == 4:

                pos_x = 130
                pos_y = 485

                self.place_pieces(count, pos_x, pos_y)

                count += 1

            elif count == 5:

                pos_x = 130
                pos_y = 230

                self.place_pieces(count, pos_x, pos_y)

        arcade.set_background_color(arcade.color.AMAZON)

    def place_pieces(self, count, pos_x, pos_y):

        for i in range(4):

            size = 32
            mass = 1
            moment = pymunk.moment_for_box(mass, (size, size))
            body = pymunk.Body(mass, moment)
            body.position = pymunk.Vec2d(pos_x, pos_y)
            shape = pymunk.Poly.create_box(body, (size, size))
            self.space.add(body, shape)

            sprite = BoxSprite(shape, (".\\sprites\\" + sprite_list[count][i]),
                               width=size, height=size)
            self.player_list.append(sprite)

            if i == 0:
                pos_y += 40
            elif i == 1:
                pos_y -= 75
                pos_x -= 30
            elif i == 2:
                pos_x += 60

    def setup(self):

        self.background = arcade.load_texture(".\\boards\\ludo6.png")

        # Setting a default value to display on the middle roll
        self.roll = "6"

    def on_draw(self):

        arcade.start_render()

        arcade.draw_texture_rectangle(screen_width // 2, screen_height // 2,
                                      screen_width, screen_height, self.background)

        for line in self.static_lines:
            body = line.body

            pv1 = body.position + line.a.rotated(body.angle)
            pv2 = body.position + line.b.rotated(body.angle)
            arcade.draw_line(pv1.x, pv1.y, pv2.x, pv2.y, arcade.color.WHITE, 2)

        self.player_list.draw()

        arcade.draw_text(self.roll, 345, 340, arcade.color.BLACK, 20)

    def on_mouse_press(self, x, y, button, modifiers):

        if button == arcade.MOUSE_BUTTON_LEFT:
            self.last_mouse_position = x, y
            shape_list = self.space.point_query((x, y), 1, pymunk.ShapeFilter())

            if len(shape_list) > 0:
                self.piece_being_dragged = shape_list[0]

    def on_mouse_release(self, x, y, button, modifiers):

        if button == arcade.MOUSE_BUTTON_LEFT:
            self.piece_being_dragged = None

    def on_mouse_motion(self, x, y, dx, dy):

        if self.piece_being_dragged is not None:
            self.last_mouse_position = x, y
            self.piece_being_dragged.shape.body.position = self.last_mouse_position
            self.piece_being_dragged.shape.body.velocity = 0, 0

    def on_update(self, delta_time):

        self.space.step(1 / 60.0)

        if self.piece_being_dragged is not None:
            self.piece_being_dragged.shape.body.position = self.last_mouse_position
            self.piece_being_dragged.shape.body.velocity = 0, 0

        for sprite in self.player_list:
            sprite.center_x = sprite.pymunk_shape.body.position.x
            sprite.center_y = sprite.pymunk_shape.body.position.y

    def on_key_press(self, key, modifiers):

        if key == arcade.key.ENTER:
            roll = random.randint(1, 6)
            self.roll = str(roll)


def main():
    window = MyGame(screen_width, screen_height, screen_title)
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
