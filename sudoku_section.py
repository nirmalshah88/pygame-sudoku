# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite
from sudoku_settings import Settings
from sudoku_block import Block

class Section(Sprite):
    
    def __init__(self, game):
        """Initialize Sudoku section (9 x 9 blocks)"""
        super().__init__()
        
        self.settings = Settings()
        self.blocks = pygame.sprite.Group()
        
        for num in range(9):
            block = Block(num)
            self.blocks.add(block)