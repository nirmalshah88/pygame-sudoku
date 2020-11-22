# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite
from sudoku_settings import Settings

class Block(Sprite):
    
    def __init__(self, num, game):
        """Initialize Sudoku block"""
        super().__init__()
        
        ## Initialize vars
        self.screen = game.screen
        
        self.settings = Settings()
        self.width = self.settings.block_width
        self.height = self.settings.block_height
        self.block_color = self.settings.block_color
        
        self.game = game
        self.num = num
        self.left = 0
        self.top = 0
        
        
    def draw_block(self, section_left, section_top):
        print(section_top)
        """Draw a block"""
        ## Set block positions based on num
        if self.num <= 3:
            # self.left = float(self.width * (self.num - 1))
            self.left = float((self.width * (self.num - 1)) + section_left)
            self.top = 0 
            # self.top = float(section_top)
        elif self.num > 3 and self.num <= 6:
            # self.left = float(self.width * (self.num % 3))
            self.left = float((self.width * (self.num % 3)) + section_left)
            self.top = float(self.height)
            # self.top = float(self.height + section_top)
            # self.top = float((self.height * (self.num % 3)) + section_top)
        elif self.num > 6 and self.num <= 9:
            # self.left = float(self.width * (self.num % 3))
            self.left = float((self.width * (self.num % 3)) + section_left)
            self.top = float(self.height * 2)
            # self.top = float((self.height * 2) + section_top)
            # self.top = float(((self.height * 2) * (self.num % 3)) + section_top)
        
        ## Update block coordinates based on section coordinates
        # self.left = self.section_left
        # self.top = self.section_top
        
        ## Create rect
        self.rect = pygame.Rect((self.left, 
                                 (self.top)),
                                (self.width, 
                                 self.height))
        
        ## Draw block
        pygame.draw.rect(rect=self.rect, 
                         color=self.block_color, 
                         surface=self.screen, 
                         border_radius=0)
        
        ## Draw block borders
        pygame.draw.lines(surface=self.screen,
                          color=(0,0,0),
                          closed=True,
                          points = [(self.left, self.top), 
                                    (self.left, self.top + self.height),
                                    (self.left + self.width, self.top + self.height),
                                    (self.left + self.width, self.top)])
        