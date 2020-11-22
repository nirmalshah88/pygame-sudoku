# -*- coding: utf-8 -*-

import pygame
import sys

# from pygame.sprite import Sprite
from sudoku_settings import Settings

class SudokuScratch:
    """Sudoku puzzle game"""
    
    def __init__(self):
        """Initialize game"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen.fill((0,0,0))
    
    def run_game(self):
        """Start main game loop"""
        while True:
            # pygame.time.wait(1000)
            self._check_events()
            self._update_screen()
    
    
    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            ## Quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        ## Redraw the screen during each pass through the loop.
        # self.screen.fill(self.settings.screen_bg_color)
        
        for row in range(0, 450, 50):
            for column in range(0, 450, 50):
                square = pygame.draw.rect(self.screen, (0,255,255), (row,column,50,50),1)
                
        
        # for i in range(1, 10):
        #     for j in range(1, 10):
        #         self.left = (i-1) * self.settings.block_width
        #         self.rect = pygame.Rect(
        #             # ((i*j-(i-1))*self.settings.block_width, (i*j*-(i-1))*self.settings.block_height), 
        #             (self.settings.block_width, self.settings.block_height)
        #         )
        #         pygame.draw.rect(rect=self.rect, 
        #                  color=(0,255,255), 
        #                  surface=self.screen)
                
        
        ## Make the most recently drawn screen visible.
        pygame.display.flip()
    
    
if __name__ == '__main__':
    sudoku = SudokuScratch()
    sudoku.run_game()