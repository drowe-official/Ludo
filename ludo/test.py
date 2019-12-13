"""This program shows how to:
  * Have one or more instruction screens
  * Show a 'Game over' text and halt the game
  * Allow the user to restart the game

Make a separate class for each view (screen) in your game.
The class will inherit from arcade.View. The structure will
look like an arcade.Window as each view will need to have its own draw,
update and window event methods. To switch a view, simply create a view
with `view = MyView()` and then use the view.show() method.

This example shows how you can set data from one View on another View to pass data
around (see: time_taken), or you can store data on the Window object to share data between
all Views (see: total_score).

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.view_instructions_and_game_over.py
"""

from arcade import *
import random
import os
PLAYER_TYPE = None
IP = None
WIDTH = 1000
HEIGHT = 1000

class HostButton(TextButton):
    def __init__(self, ludo, x=0, y=0, width=100, height=40, text="Host",face_color=None, theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.ludo = ludo

    def on_press(self):
        self.pressed = True
        print("Now Hosting Ludo....")
        #players = input("Enter the Number of Players ")
        self.ludo.window.players = players
        game_view = GameView()
        self.ludo.window.show_view(game_view)

class JoinButton(TextButton):
    def __init__(self, ludo, x=0, y=0, width=100, height=40, text="Connect", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.ludo = ludo

    def on_press(self):
        self.pressed = True
        ip = input("Please input the IP you wish to connect to ")
        print("Joining Ludo....")
        self.ludo.window.ip = ip
        self.ludo.window.ip = "player"
        game_view = GameView()
        self.ludo.window.show_view(game_view)

class QuitButton(TextButton):
    def __init__(self, ludo, x=0, y=0, width=100, height=40, text="Quit", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.ludo = ludo

    def on_press(self):
        self.pressed = True
        print("Quitting..")
        exit()

    def on_draw(self):
        arcade.start_render()
        super().on_draw()
      
class MenuView(View):
    def __init__(self):
        super().__init__()
        self.button_list = []
        
    def on_show(self):
        arcade.set_background_color(arcade.color.BUBBLES)
        
    def bt(self):
        start = "start.png"
        self.theme.add_button_textures(start, start, start, start)

    def layout(self):
        self.theme = gui.Theme()
        self.theme.set_font(30, arcade.color.WHITE)
        self.bt()
        
    def on_draw(self):
        arcade.start_render()
        for i in self.button_list:
            i.draw()
    
    def buttons(self):
        self.button_list.append(HostButton(self, 450, 680, 310, 150, theme=self.theme))
        self.button_list.append(JoinButton(self, 450, 525, 310, 150, theme=self.theme))
        self.button_list.append(QuitButton(self, 450, 360, 310, 150, theme=self.theme))

    def start(self):
        self.layout()
        self.buttons()
      
class GameView(View):
    def __init__(self):
        super().__init__()
        self.background = None
        
    def on_show(self):
        self.background = arcade.load_texture("board.png")
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(WIDTH // 2, HEIGHT // 2,
                                      WIDTH, HEIGHT, self.background)

def main():
    window = arcade.Window(WIDTH, HEIGHT, "test")
    window.total_score = 0
    menu_view = MenuView()
    menu_view.start()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()