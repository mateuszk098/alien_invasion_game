"""
This module provides a Spaceship object, which the player controls.
"""

import pygame as pg
from pygame.sprite import Sprite
from pygame.surface import Surface
from pygame.rect import Rect


class Spaceship(Sprite):
    """Spaceship object controlled by the player."""

    _RESIZED_SHIP: str = "../assets/player_ships/SF02_resized.png"  # Used as remaining lives indicator.
    _NORMAL_SHIP: str = "../assets/player_ships/SF02.png"

    def __init__(self, ai_game, resized: bool = False) -> None:
        """Initialise Spaceship object."""
        super().__init__()
        self.screen: Surface = ai_game.screen
        self.screen_rect: Rect = ai_game.screen_rect
        self.settings = ai_game.settings

        self.moving_right: bool = False
        self.moving_left: bool = False

        ship_path: str = self._NORMAL_SHIP
        if resized:
            ship_path = self._RESIZED_SHIP

        self.image: Surface = pg.image.load(ship_path).convert_alpha()
        self.rect: Rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 20
        # Float type for the horizontal position due to more accurate tracking.
        self.x: float = float(self.rect.x)

    def update(self, *args, **kwargs) -> None:  # Override the Sprite.update()
        """Updates the spaceship x-position by its speed defined in settings."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_ship_speed
        if self.moving_left and self.rect.left > 0:  # Usage of elif means priority for moving right.
            self.x -= self.settings.player_ship_speed
        self.rect.x = int(self.x)

    def set_center(self) -> None:
        """Places the spaceship in the centre of the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 20
        self.x = float(self.rect.x)

    def draw(self) -> None:
        """Displays the spaceship in its current position on the screen."""
        self.screen.blit(self.image, self.rect)
