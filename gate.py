import arcade
import random

import player


class Gate:

    xPos: int
    yPos: int

    moveSpeed: float

    gap_size: int
    top_offset: int
    bottom_offset: int
    wall_height: int
    wall_width = 50

    color = arcade.color.BLACK


    minimum_xPosition: int


    def __init__(self, xPos: int, yPos: int, screen_height: int, moveSpeed: float):

        self.xPos = xPos
        self.yPos = yPos

        self.wall_height = screen_height
        self.gap_size = random.randint(120, 350)

        self.moveSpeed = moveSpeed

    def update(self, delta_time: float, player: player.Player):

        self.xPos -= self.moveSpeed * delta_time

        top_point_list = arcade.get_rectangle_points(self.xPos, self.get_top_wall_position(), self.wall_width, self.wall_height)
        bottom_point_list = arcade.get_rectangle_points(self.xPos, self.get_bottom_wall_position(), self.wall_width, self.wall_height)

        if arcade.are_polygons_intersecting(player.get_hitbox(), top_point_list) or arcade.are_polygons_intersecting(player.get_hitbox(), bottom_point_list) :
            arcade.exit()

    def draw_self(self):

        #draw top part
        arcade.draw_rectangle_filled(self.xPos, self.get_top_wall_position(), self.wall_width, self.wall_height, self.color)

        #draw bottom part
        arcade.draw_rectangle_filled(self.xPos, self.get_bottom_wall_position(), self.wall_width, self.wall_height, self.color)

    def get_top_wall_position(self):

        return (self.yPos + self.gap_size * 0.5) + self.wall_height * 0.5


    def get_bottom_wall_position(self):

        return (self.yPos - self.gap_size * 0.5) - self.wall_height * 0.5