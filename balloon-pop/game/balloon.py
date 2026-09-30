"""
Balloon: falls from the top of the screen. The player must pop it
before it reaches the bottom. Balloons vary in size - this matters for
how click detection should work.
"""

import pygame


class Balloon:
    def __init__(self, x, y, radius, speed, points=10, color=(255, 182, 193)):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.points = points
        self.color = color

    def update(self):
        self.y += self.speed

    def is_past_bottom(self, height):
        return self.y - self.radius > height

    def get_rect(self):
        return pygame.Rect(
            int(self.x - self.radius), int(self.y - self.radius),
            self.radius * 2, self.radius * 2,
        )