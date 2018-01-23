# -*- coding: utf-8 -*-
'''
Created on 2018年1月22日

@author: Jeff Yang
'''


class GameStats():
    """跟踪游戏的统计信息"""
    
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 让游一开始处于非活动状态
        self.game_active = False
        # 在任何情况下都不应重置最高得分,所以在__init__()中初始化high_score
        self.high_score = 0
    
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        # 游戏运行期间只创建一个GameStats实例
        # 但玩家开始新游戏时，需要重置一些统计信息，所以在reset_stas()中初始化大部分信息，开始新游戏也能调用这个方法
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0  # 记分，每次开始游戏都重置得分，因此不放在__init__()中
        self.level = 1  # 等级，消灭一波外星人升一级
