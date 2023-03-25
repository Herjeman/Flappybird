# This is a sample Python script.
import gate_manager
# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings

import player
import gate
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Flappy Bird"

PLAYER = player.Player(SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.5, SCREEN_WIDTH, SCREEN_HEIGHT)

class GameWindow(arcade.Window):
    """
    Main application class
    """

    gateManager: gate_manager.GateManager

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        #Sprite lists go here?

        self.gateManager = gate_manager.GateManager(SCREEN_WIDTH, SCREEN_HEIGHT, 1.7)

    def setup(self):
        """Sets up the game. Call to restart the game"""

    def on_draw(self):
        """Render the screen"""

        #clear screen
        self.clear()

        #Do rendering here
        PLAYER.draw_self()
        self.gateManager.draw_gates()


    def on_update(self, delta_time: float):
        """Update logic goes here"""
        PLAYER.update(delta_time)
        self.gateManager.update(delta_time, PLAYER)


    def on_key_press(self, key, key_modifiers):
        """Called when a key on the keyboard is pressed"""

        if key == arcade.key.SPACE:
            PLAYER.recieve_jump_input()


    def on_key_release(self, key, key_modifiers):
        """Called whenever a key on the keyboard is released"""

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """Called when the mouse is moved"""

        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """Main game function"""
    game = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
