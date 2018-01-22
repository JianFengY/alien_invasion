# -*- coding: utf-8 -*-
'''
Created on 2018年1月22日

@author: Jeff Yang
'''

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):  # 继承Sprite类，可以将游戏中相关的元素编组，进而同时操作编组中的所有元素
    """一个对飞船发射的子弹管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()  # 这里使用了python2.7的语法，也可以写为super().__init__()
        self.screen = screen
        
        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        # 创建了子弹的属性rect，并非基于图像，因此使用pygame.Rect()从空白创建一个矩形，必须提供左上角的x和y坐标还有宽度高度
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        # 将子弹的centerx设置为飞船的rect.centerx
        self.rect.centerx = ship.rect.centerx
        # 子弹应该从飞船顶部射出，所以将子弹的rect.top设置为飞船的rect.top
        self.rect.top = ship.rect.top
        
        # 存储用小数表示的子弹位置，以便能够微调子弹速度
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y
    
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        # 函数draw.rect()使用存储在self.color中的颜色填充表示子弹的rect占据的屏幕部分
        pygame.draw.rect(self.screen, self.color, self.rect)
