# -*- coding: utf-8 -*-
'''
Created on 2018年1月22日

@author: Jeff Yang
'''


class Settings():
    """存储《外星人入侵》的所有设置的类"""
    
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 550
        self.bg_color = (230, 230, 230)  # 设置背景颜色，pygame中，颜色是以RGB值指定的
        
        # 飞船的速度设置
        self.ship_speed_factor = 1.5
        
        # 子弹设置
        # 宽3像素高15像素的深灰色子弹
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3  # 允许的最大子弹书
