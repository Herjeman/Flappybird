import random

import gate
import player


class GateManager:
    """Spawns and manages gates"""

    timer: float
    spawn_cooldown: int
    screen_width: int
    screen_height: int

    active_gates = []

    def __init__(self, width, height,spawn_cooldown):

        self.screen_width = width
        self.screen_height = height
        self.spawn_cooldown = spawn_cooldown
        self.timer = spawn_cooldown

    def spawnGate(self):

        yspawn = self.screen_height * 0.5 + random.randint(-100, 100)
        self.active_gates.append(gate.Gate(self.screen_width, yspawn, self.screen_height, 250))

    def update(self, delta_time: float, player: player.Player):

        self.timer -= delta_time
        if self.timer < 0:
            self.spawnGate()
            self.timer = self.spawn_cooldown

        for instance in self.active_gates:
            instance.update(delta_time, player)

    def draw_gates(self):

        for instance in self.active_gates:
            instance.draw_self()