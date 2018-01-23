# -*- coding: utf-8 -*-
'''
Created on 2018年1月23日

@author: Jeff Yang
'''

import pygame.font
from pygame.sprite import Group

from chapter14_scoring.ship import Ship  # 先导入标准库空一行再导入自己编写的模块


class Scoreboard():
    """显示得分信息的类"""
    
    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分设计的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
    
        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # 准备包含初始得分和最高得分的图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        # round()四舍五入，第二个参数表示保留小数位数，负数表示圆整到10,100,1000等整数倍，-1表示圆整到10的整数倍
        # python2.7中round()总是返回一个小数值，所以使用int()确保得分为整数，python3可以省略int()
        rounded_score = int(round(self.stats.score, -1))
        # 使用逗号做千分位分隔符，使输出像1,000,000
        score_str = "Score: " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
            self.text_color, self.ai_settings.bg_color)
        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        # 让score_rect右边缘与屏幕右边缘相距20像素
        self.score_rect.right = self.screen_rect.right - 20
        # 让score_rect上边缘与屏幕上边缘也相距20像素
        self.score_rect.top = 20
        
    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "Record: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.ai_settings.bg_color)
        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        # 将最高分rect的top属性设置为当前得分图像rect的top属性
        self.high_score_rect.top = self.score_rect.top
    
    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render("Level: " + str(self.stats.level), True,
            self.text_color, self.ai_settings.bg_color)
        # 将登记放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right  # 等级的rect的right属性设为得分的right属性
        self.level_rect.top = self.score_rect.bottom + 10  # top属性比得分的bottom属性大10
    
    def prep_ships(self):
        """显示还余下多少飞船"""
        self.ships = Group()  # 创建一个空编组
        for ship_number in range(self.stats.ships_left):  # 根据剩余飞船数循环
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width  # 位于屏幕左边距左边缘10像素
            ship.rect.y = 10  # 距上边缘10像素
            self.ships.add(ship)
    
    def show_score(self):
        """在屏幕上显示得分最高分和等级"""
        self.screen.blit(self.score_image, self.score_rect)  # 得分图像放在score_rect指定位置上
        self.screen.blit(self.high_score_image, self.high_score_rect)  # 最高分图像
        self.screen.blit(self.level_image, self.level_rect)  # 等级图像
        self.ships.draw(self.screen)  # 剩余飞船
