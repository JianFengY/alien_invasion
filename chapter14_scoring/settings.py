# -*- coding: utf-8 -*-
'''
Created on 2018年1月22日

@author: Jeff Yang
'''


class Settings():
    """存储《外星人入侵》的所有设置的类"""
    
    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230, 230, 230)  # 设置背景颜色，pygame中，颜色是以RGB值指定的
        
        # 飞船设置
#         self.ship_speed_factor = 1.5  # 速度
        self.ship_limit = 3  # 玩家拥有的飞船数
        
        # 子弹设置，可以随时修改，特别是测试时
        # 宽3像素高15像素的深灰色子弹
#         self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3  # 允许的最大子弹数
        
        # 外星人设置
#         self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
#         # fleet_direction为1表示向右移，为-1表示向左移
#         self.fleet_direction = 1
        
        # 以什么样的速度加快游戏节奏
        # 控制速度的属性，用来与原来的速度相乘达到加快速度的效果
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5  # 飞船速度
        self.bullet_speed_factor = 3  # 子弹速度
        self.alien_speed_factor = 1  # 外星人速度
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        # 记分，随着游戏进行，将提高外星人点数，所以放在initialize_dynamic_settings()里
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale  # 飞船速度
        self.bullet_speed_factor *= self.speedup_scale  # 子弹速度
        self.alien_speed_factor *= self.speedup_scale  # 外星人速度
        self.alien_points = int(self.alien_points * self.score_scale)  # 外星人点数
#         print(self.alien_points)
        
