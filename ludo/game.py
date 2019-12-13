from arcade.gui import *
import player

class HostButton(TextButton):
    def __init__(self, ludo, x=0, y=0, width=100, height=40, text="Host",face_color=None, theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.ludo = ludo

    def on_press(self):
        self.pressed = True
        print("Host the Ludo")
        self.ludo.wipe()
        #player.main()

class JoinButton(TextButton):
    def __init__(self, ludo, x=0, y=0, width=100, height=40, text="Connect", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.ludo = ludo

    def on_press(self):
        self.pressed = True
        print("Joining Ludo..")
        #connect.main()

class QuitButton(TextButton):
    def __init__(self, ludo, x=0, y=0, width=100, height=40, text="Quit", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.ludo = ludo

    def on_press(self):
        self.pressed = True
        print("Quitting..")
        exit()

class Ludo(arcade.Window):
    def __init__(self):
        super().__init__(900, 900, "Ludo")
        arcade.set_background_color(arcade.color.BUBBLES)

    def bt(self):
        start = "start.png"
        self.theme.add_button_textures(start, start, start, start)

    def layout(self):
        self.theme =  ()
        self.theme.set_font(30, arcade.color.WHITE)
        self.bt()

    def buttons(self):
        self.button_list.append(HostButton(self, 450, 680, 310, 150, theme=self.theme))
        self.button_list.append(JoinButton(self, 450, 525, 310, 150, theme=self.theme))
        self.button_list.append(QuitButton(self, 450, 360, 310, 150, theme=self.theme))

    def start(self):
        self.layout()
        self.buttons()
    def wipe(self):
        self.button_list = []
        arcade.set_background_color(arcade.color.WHITE)
        
    def on_draw(self):
        arcade.start_render()
        super().on_draw()


def main():
    ludo = Ludo()
    ludo.start()
    arcade.run()

main()