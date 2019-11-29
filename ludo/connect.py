import arcade

class Window(arcade.Window):
    def __init__(self):
        super().__init__(900, 900)
        self.ip = ""

    def start(self):
        arcade.set_background_color(arcade.color.BUBBLES)
        self.text_list.append(arcade.gui.Text("    Enter the IP you wish to connect ", self.width / 2 - 205, self.height / 2))
        self.textbox_list.append(arcade.gui.TextBox(self.width / 2 - 90, self.height / 2))
        self.button_list.append(arcade.gui.SubmitButton(self.textbox_list[0], self.on_submit, self.width / 2 + 40,self.height / 2 -130))

    def on_draw(self):
        arcade.start_render()
        super().on_draw()
        arcade.draw_text(f": {self.textbox_list[0].text_storage.text}", 465, 437, arcade.color.BLACK, 20)
    
    def on_submit(self):
        self.ip = self.textbox_list[0].text_storage.text
        print(self.ip)

def main():
    window = Window()
    window.start()
    arcade.run()
main()