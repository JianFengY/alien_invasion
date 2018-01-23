# -*- coding: utf-8 -*-
'''
Created on 2018年1月23日

@author: Jeff Yang
'''

import pygame.font  # 让pygame能将文本渲染到屏幕上


class Button():
    """按钮类"""

    def __init__(self, ai_settings, screen, msg):  # msg为按钮要显示的文本
        """初始化按钮属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)  # 设置字体，None让pygame使用默认字体，48为字号
        
        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # 按钮的标签只需创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        # font.render()方法将存储在msg中的文本转化为图像，并存储在msg_image中
        # 布尔值指定开启或关闭反锯齿功能（反锯齿让文本边缘更平滑），余下两个参数为文本颜色和背景色（不指定背景色则透明）
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.rect)  # 绘制表示按钮的矩形
        self.screen.blit(self.msg_image, self.msg_image_rect)
