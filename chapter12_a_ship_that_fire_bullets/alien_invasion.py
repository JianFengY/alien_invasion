# -*- coding: utf-8 -*-
'''
Created on 2018年1月21日

@author: Jeff Yang
'''

import pygame
from pygame.sprite import Group
from chapter12_a_ship_that_fire_bullets.settings import Settings
from chapter12_a_ship_that_fire_bullets.ship import Ship
from chapter12_a_ship_that_fire_bullets import game_functions as gf


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
    
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)  # 检查玩家输入
        ship.update()  # 更新飞船位置
        gf.update_bullets(bullets)  # 更新子弹位置
        gf.update_screen(ai_settings, screen, ship, bullets)  # 绘制屏幕


run_game()
