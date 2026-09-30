"""
renderer: all pygame drawing lives here, kept separate from game logic.
"""

import pygame

WIDTH, HEIGHT = 700, 500
WINDOW_SIZE = (WIDTH, HEIGHT)

COLOR_BG = (200, 230, 245)
COLOR_TEXT = (30, 30, 30)


def draw_scene(surface, balloons):
    surface.fill(COLOR_BG)
    for b in balloons:
        pygame.draw.circle(surface, b.color, (int(b.x), int(b.y)), b.radius)
        pygame.draw.line(surface, (120, 120, 120), (b.x, b.y + b.radius), (b.x, b.y + b.radius + 12), 2)


def draw_text(surface, font, text, pos, color=COLOR_TEXT):
    surface.blit(font.render(text, True, color), pos)


def draw_banner(surface, font, text):
    surf = font.render(text, True, (180, 40, 40))
    rect = surf.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2))
    surface.blit(surf, rect)

def draw_banner_with_subtitle(surface, font, title_text, sub_text):
    center_x = surface.get_width() // 2
    center_y = surface.get_height() // 2

    # Draw semi-transparent overlay box
    overlay = pygame.Surface((480, 120))
    overlay.set_alpha(220)
    overlay.fill((255, 255, 255))
    overlay_rect = overlay.get_rect(center=(center_x, center_y))
    surface.blit(overlay, overlay_rect)

    # Main Title (Final Score)
    title_surf = font.render(title_text, True, (180, 40, 40))
    title_rect = title_surf.get_rect(center=(center_x, center_y - 20))
    surface.blit(title_surf, title_rect)

    # Subtitle (Restart Instruction)
    sub_surf = font.render(sub_text, True, (50, 50, 50))
    sub_rect = sub_surf.get_rect(center=(center_x, center_y + 20))
    surface.blit(sub_surf, sub_rect)