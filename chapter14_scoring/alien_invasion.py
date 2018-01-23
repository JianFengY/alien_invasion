# -*- coding: utf-8 -*-
'''
Created on 2018年1月21日

@author: Jeff Yang
'''

import pygame
from pygame.sprite import Group
from chapter14_scoring.settings import Settings
from chapter14_scoring.ship import Ship
from chapter14_scoring import game_functions as gf
from chapter14_scoring.game_stats import GameStats
from chapter14_scoring.button import Button
from chapter14_scoring.scoreboard import Scoreboard


def run_game():
    """初始化游戏并创建一个屏幕对象"""
    # 初始化背景设置，让pygame能够正确的工作
    pygame.init()
    # 创建一个名为screen的显示窗口，这个游戏的所有图形元素都在其中绘制
    # 实参(1000, 550)是一个元组，指定游戏窗口尺寸，宽1000像素高550像素
    # 对象screen是一个surface，surface是屏幕的一部分，这个游戏中每个元素如飞船等都是surface
    # display.set_mode()返回的surface表示整个游戏窗口
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # 创建play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船
    # 注意，整个游戏运行期间，我们只创建了一个飞船实例
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个用于存储外星人的编组
    aliens = Group()
    
#     # 创建一个外星人
#     alien = Alien(ai_settings, screen)
    
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb,
            play_button, ship, aliens, bullets)  # 检查玩家输入
        if stats.game_active:  # 游戏处于活动状态才调用下列函数
            ship.update()  # 更新飞船位置
            # 子弹相关信息的更新
            gf.update_bullets(ai_settings, screen, stats, sb,
                ship, aliens, bullets)
            # 更新外星人的位置，要先更新子弹，因为要检查是否有子弹撞到了外星人
            gf.update_aliens(ai_settings, screen, stats, sb,
                ship, aliens, bullets)
        # 绘制屏幕
        gf.update_screen(ai_settings, screen, stats, sb,
            ship, aliens, bullets, play_button)


run_game()
