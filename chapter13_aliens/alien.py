# -*- coding: utf-8 -*-
'''
Created on 2018年1月22日

@author: Jeff Yang
'''

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""
    
    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()  # python2.7的语法
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width  # 将外星人的左边距设置为外星人的宽度
        self.rect.y = self.rect.height  # 将外星人的上边距设置为外星人的高度
        
        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        
    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """如果有外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()  # 屏幕的rect
        # 如果外星人的rect的right属性大于或等于屏幕的rect的right属性，就说明位于右边缘
        if self.rect.right >= screen_rect.right:
            return True
        # 如果外星人的rect的left属性小于或等于0说明位于左边缘
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向左或向右移动外星人"""
        # 使用self.x跟踪每个外星人的准确位置，这个属性可存储小数值，然后用这个值更新外星人的rect的位置
        # fleet_direction的正负决定左移还是右移，1则x增大为右移，-1则x减小为左移
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x
    
