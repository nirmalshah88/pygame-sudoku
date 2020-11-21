# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite
from sudoku_settings import Settings

class Block(Sprite):
    
    def __init__(self, num, game):
        """Initialize Sudoku block"""
        super().__init__()
        
        self.screen = game.screen
        
        self.settings = Settings()
        self.width = self.settings.block_width
        self.height = self.settings.block_height
        
        self.block_color = self.settings.block_color
        
        self.num = num
        self.left = 0
        self.top = 0
        
        # set block position (left, top) based on num
        if self.num <= 3:
            self.left = float(self.width * self.num)
        elif self.num > 3 and self.num <= 6:
            self.left = float(self.width * (self.num % 3 + 1))
            self.top = float(self.height)            
        elif self.num > 6 and self.num <= 9:
            self.left = float(self.width * (self.num % 3 + 1))
            self.top = float(self.height * 2)
            
        self.rect = pygame.Rect((self.left, self.top),
                                (self.width, self.height))
        
        """
        1 -> 0,0
        2 -> 10,0
        3 -> 20,0
        4 -> 0,10
        5 -> 10,10
        6 -> 20,10
        
        """
        
    def draw_block(self):
        pygame.draw.rect(rect=self.rect, color=self.block_color, surface=self.screen, border_radius=1)
        