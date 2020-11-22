# -*- coding: utf-8 -*-

import pygame

class Settings:
    
    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg_color = (255, 255, 255)
        
        # Block settings
        self.block_width = 100
        self.block_height = 100
        self.block_color = (0, 255, 255) # cyan
        self.block_puzzle_color = (160, 160, 160) # gray
        self.block_error_color = (255, 155, 145) # salmon
        self.block_border_radius = 2
        self.block_border_color = (0,0,0) # black        
        
        # Section settings
        self.section_width = self.block_width * 3
        self.section_height = self.block_height * 3
        

        # Grid settings

        
        