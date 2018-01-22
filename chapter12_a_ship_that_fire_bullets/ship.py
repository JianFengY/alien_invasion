# -*- coding: utf-8 -*-
'''
Created on 2018年1月22日

@author: Jeff Yang
'''

import pygame


class Ship():
    """管理飞船的大部分行为"""

    def __init__(self, ai_settings, screen):  # screen指定要将飞船绘制在什么地方
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载飞船图像并获取其外接矩形
        # 使用位图（.bmp）最为简单，因为pygame默认加载位图
        # pygame能够像处理矩形（rect对象）一样处理游戏元素，因为矩形是简单几何图形，比较高效 
        self.image = pygame.image.load('images/ship.bmp')  # 返回一个表示飞船的surface，存到self.image中
        self.rect = self.image.get_rect()  # 获取surface的属性rect
        self.screen_rect = screen.get_rect()  # 将表示屏幕的矩形存储在self.screen_rect中
        
        # 将每艘新飞船放在屏幕底部中央
        # pygame中，原点(0,0)位于屏幕左上角，向右下方移动时数字增大，1000*550的屏幕上右下角坐标为(1000,550)
        # 处理rect对象时，可使用矩形四角和中心的x和y坐标来指定位置
        # 将self.rect.centerx（飞船的中心的x坐标）设置为表示屏幕的矩形的属性centerx
        # 再将self.rect.bottom（飞船下端边缘的y坐标）设置为屏幕的矩形的属性buttom
        self.rect.centerx = self.screen_rect.centerx  # 对应的还有center,centery
        self.rect.bottom = self.screen_rect.bottom  # 对应的还有top,left,right
        
        # rect的centerx等属性只能存储整数值，所以这里做些修改
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """根据移动标志调整飞船的位置"""
        # 标志为右移且self.rect.right（矩形右侧x坐标）不超出屏幕右侧范围
        if self.moving_right and self.rect.right < self.screen_rect.right:
#             self.rect.centerx += 1
            # 改为更新飞船的center值，而非rect
            self.center += self.ai_settings.ship_speed_factor
        # 标志为左移且self.rect.left（矩形左侧x坐标）不超过屏幕左侧范围
        if self.moving_left and self.rect.left > 0:  # 不用elif使同时按下左右键的时候移动效果更准确
#             self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
