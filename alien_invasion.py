'''
General file with class used to game management.
'''

import sys

import pygame

from settings import Settings
from spaceship import Spaceship
from bullet import Bullet


class AlienInvasion():
    ''' General class to game management. '''

    def __init__(self) -> None:
        ''' Game initialization. '''
        pygame.init()  # Initialization of screen.
        pygame.display.set_caption('Alien Invasion')
        self.settings: Settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # Full screen.
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.ship: Spaceship = Spaceship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self) -> None:
        ''' Main loop of the game. '''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self) -> None:
        ''' Check reaction to button press and mouse interaction. '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event) -> None:
        ''' Reaction on key press. '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event) -> None:
        ''' Reaction on key release. '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self) -> None:
        ''' Create new bullet and add it to group. '''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet: Bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self) -> None:
        ''' Update of bullets positions and remove bullets from out of screen. '''
        self.bullets.update()
        # Remove bullets out of the screen.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:  # type: ignore
                self.bullets.remove(bullet)

    def _update_screen(self) -> None:
        ''' Updates the screen. '''
        self.screen.fill(self.settings.background_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()  # type: ignore
        pygame.display.flip()  # Update of the screen.


if __name__ == '__main__':
    # Instance of game
    ai: AlienInvasion = AlienInvasion()
    ai.run_game()
