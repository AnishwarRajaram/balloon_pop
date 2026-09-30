"""
click_detection: figures out whether a click landed on a balloon.
"""


def check_pop(balloons, click_pos):
    """
    Returns the balloon that was clicked, or None if the click missed
    every balloon.
    """
    for balloon in balloons:
        dx = click_pos[0] - balloon.x
        dy = click_pos[1] - balloon.y
        distance_squared = dx * dx + dy * dy
        if distance_squared <= balloon.radius ** 2:
            return balloon
    return None
