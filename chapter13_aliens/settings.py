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
        self.screen_height = 700
        self.bg_color = (230, 230, 230)  # 设置背景颜色，pygame中，颜色是以RGB值指定的
        
        # 飞船设置
        self.ship_speed_factor = 1.5  # 速度
        self.ship_limit = 3  # 玩家拥有的飞船数
        
        # 子弹设置，可以随时修改，特别是测试时
        # 宽3像素高15像素的深灰色子弹
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3  # 允许的最大子弹数
        
        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1