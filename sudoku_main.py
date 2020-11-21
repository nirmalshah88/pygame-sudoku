# -*- coding: utf-8 -*-

import pygame
import sys

from pygame.sprite import Sprite

from sudoku_settings import Settings
from sudoku_block import Block

class Sudoku:
    """Sudoku puzzle game"""
    
    def __init__(self):
        """Initialize game"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen.fill(self.settings.screen_bg_color)
        
        self.blocks = pygame.sprite.Group()
        
        for num in range(1,10):
            block = Block(num, self)
            self.blocks.add(block)
        
        # self.blocks.draw(self.screen)
    
    
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
            ## Key down
            elif event.type == pygame.KEYDOWN:
                # self._check_keydown_events(event)
                pass
            ## Key up
            elif event.type == pygame.KEYUP:
                # self._check_keyup_events(event)
                pass
            ## Mouse clicks
            elif event.type == pygame.mouse.get_pressed():  
                pos = pygame.mouse.get_pos()
                print(pos)
                # for block in self.blocks.sprites():
                    ## if click on block
                    # block.collidepoint(pos):
                        # pass 
    
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        ## Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.screen_bg_color)
        
        for block in self.blocks.sprites():
            block.draw_block()
        
        ## Make the most recently drawn screen visible.
        pygame.display.flip()
    
    
if __name__ == '__main__':
    sudoku = Sudoku()
    sudoku.run_game()