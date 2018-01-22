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
        # 游戏刚启动时处于活动状态
        self.game_active = True
    
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        # 游戏运行期间只创建一个GameStats实例
        # 但玩家开始新游戏时，需要重置一些统计信息，所以在reset_stas()中初始化大部分信息，开始新游戏也能调用这个方法
        self.ships_left = self.ai_settings.ship_limit
