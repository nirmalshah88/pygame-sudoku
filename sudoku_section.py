# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite
from sudoku_settings import Settings
from sudoku_block import Block

class Section(Sprite):
    
    def __init__(self, num, game):
        """Initialize Sudoku section (9 x 9 blocks)"""
        super().__init__()
        
        ## Initialize vars
        self.screen = game.screen
        
        self.settings = Settings()
        self.width = self.settings.section_width
        self.height = self.settings.section_height

        self.game = game
        self.num = num
        self.left = 0
        self.top = 0
    
    
    def draw_section(self):
        """Draw Sudoku section of blocks"""          
        ## Set section postitions based on num
        if self.num <= 3:
            self.left = float(self.width * (self.num - 1))
            self.top = 0
        elif self.num > 3 and self.num <= 6:
            self.left = float(self.width * (self.num % 3))
            self.top = float(self.height)          
        elif self.num > 6 and self.num <= 9:
            self.left = float(self.width * (self.num % 3))
            self.top = float(self.height * 2)
        
        ## Create rect
        # print(self.left, self.top, self.width, self.height)
        self.rect = pygame.Rect((self.left, self.top),
                                (self.width, self.height))
        
        ## Create 9 blocks for each section
        self.blocks = pygame.sprite.Group()
        for num in range(1,10):
            block = Block(num, self.game)
            self.blocks.add(block)
        
        ## Draw section with blocks
        for block in self.blocks.sprites():
            pygame.draw.rect(rect=self.rect, 
                             color=(0,0,0), 
                             surface=self.screen, 
                             border_radius=0)
            block.draw_block(self.left, self.top)
        
        ## Draw section borders
        pygame.draw.lines(surface=self.screen,
                          color=(0,255,0),
                          closed=True,
                          points = [(self.left, self.top), 
                                    (self.left, self.top + self.height),
                                    (self.left + self.width, self.top + self.height),
                                    (self.left + self.width, self.top)])
        
        # Draw blocks for section
        # for num in range(1,10):
            # for block in self.blocks.sprites():
                # block.draw_block(self.num)
            