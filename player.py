import arcade

class Player():

    xPos: int
    yPos: int

    width= 100
    height = 50

    screen_width: int
    screen_height: int

    kill_offset = 50

    xSpeed = 0
    ySpeed = 0
    gravity = 10
    jump_height = 200

    color = arcade.color.RED
    hit_box_point_list = []



    def __init__(self, xPos, yPos, screen_width, screen_height):
        """Relevant docstring here"""

        self.xPos = xPos
        self.yPos = yPos

        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, delta_time: float):
        """Relevant docstring here"""

        #apply gravity
        self.ySpeed -= self.gravity

        self.xPos = self.xPos + self.xSpeed * delta_time
        self.yPos = self.yPos + self.ySpeed * delta_time

        if self.yPos < 0 - self.kill_offset or self.yPos > self.screen_height + self.kill_offset:
            arcade.exit()

    def recieve_jump_input(self):
        """Call to make jump"""

        self.ySpeed += self.jump_height

    def draw_self(self):
        """Draw a rect object with relevant xPos and yPos"""

        arcade.draw_rectangle_filled(self.xPos, self.yPos, self.width, self.height, self.color)

    def get_hitbox(self):
        """Returns a point list of the player hitbox"""

        return arcade.get_rectangle_points(self.xPos, self.yPos, self.width, self.height)