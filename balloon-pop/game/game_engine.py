"""
GameEngine: owns all balloons, spawns new ones, and handles clicks.

version 3: Includes multi-type balloon spawning (Normal, Bonus, Penalty), click hit detection,
lives/miss system, countdown timer, and game reset handling.
"""

import random

from game.balloon import Balloon
from game.click_detection import check_pop
from game.renderer import WIDTH, HEIGHT

SPAWN_INTERVAL_FRAMES = 45
ROUND_DURATION_SECONDS = 30

BALLOON_TYPES = [
    {"color": (255, 182, 193), "points": 10,  "is_penalty": False},  # Pink (Normal)
    {"color": (255, 223, 0),   "points": 50,  "is_penalty": False},  # Yellow (Bonus)
    {"color": (220, 20, 60),   "points": -5,  "is_penalty": True},   # Red (Penalty)
]


class GameEngine:
    def __init__(self):
        self.reset()

    def reset(self):
        """Resets score, lives, timer, and balloons for a new round."""
        self.balloons = []
        self.frames_until_spawn = 0
        self.score = 0
        self.lives = 3
        self.time_remaining = ROUND_DURATION_SECONDS
        self.game_over = False

    def _spawn_balloon(self):
        radius = random.randint(16, 44)
        x = random.randint(radius + 10, WIDTH - radius - 10)
        speed = random.uniform(1.5, 3.0)
        
        type_choice = random.choices(
            BALLOON_TYPES, 
            weights=[0.70, 0.15, 0.15], 
            k=1
        )[0]

        balloon = Balloon(
            x=x,
            y=-radius,
            radius=radius,
            speed=speed,
            points=type_choice["points"],
            color=type_choice["color"],
        )
        balloon.is_penalty = type_choice["is_penalty"]
        self.balloons.append(balloon)

    def handle_click(self, pos):
        if self.game_over:
            return

        popped = check_pop(self.balloons, pos)
        if popped is not None:
            self.balloons.remove(popped)
            self.score += popped.points

    def handle_keydown(self, key):
        """Restarts the game if 'R' or 'SPACE' is pressed during Game Over."""
        import pygame
        if self.game_over and key in (pygame.K_r, pygame.K_SPACE):
            self.reset()

    def update(self, dt):
        """dt is the delta time in seconds passed since last frame."""
        if self.game_over:
            return

        # Countdown Timer
        self.time_remaining -= dt
        if self.time_remaining <= 0:
            self.time_remaining = 0
            self.game_over = True
            return

        # Spawning Logic
        self.frames_until_spawn -= 1
        if self.frames_until_spawn <= 0:
            self._spawn_balloon()
            self.frames_until_spawn = SPAWN_INTERVAL_FRAMES

        # Balloon Updates
        for b in self.balloons:
            b.update()

        # Miss / Life Deduction Logic
        remaining_balloons = []
        for b in self.balloons:
            if b.is_past_bottom(HEIGHT):
                if not getattr(b, "is_penalty", False):
                    self.lives -= 1
                    if self.lives <= 0:
                        self.lives = 0
                        self.game_over = True
            else:
                remaining_balloons.append(b)

        self.balloons = remaining_balloons

    def draw(self, surface, font):
        from game import renderer
        renderer.draw_scene(surface, self.balloons)
        
        # HUD Displays
        renderer.draw_text(surface, font, f"Score: {self.score}", (10, 10))
        renderer.draw_text(surface, font, f"Time: {int(self.time_remaining)}s", (WIDTH // 2 - 40, 10))
        renderer.draw_text(surface, font, f"Lives: {self.lives}", (WIDTH - 120, 10))

        # Game Over Banner displaying final score and restart prompt
        if self.game_over:
            banner_text = f"GAME OVER! Final Score: {self.score}"
            sub_text = "Press 'R' or 'SPACE' to Restart"
            renderer.draw_banner_with_subtitle(surface, font, banner_text, sub_text)