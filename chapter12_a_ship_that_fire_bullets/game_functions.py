# -*- coding: utf-8 -*-
'''
Created on 2018年1月22日

@author: Jeff Yang
'''

import sys
import pygame
from chapter12_a_ship_that_fire_bullets.bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按下按键的事件"""
    if event.key == pygame.K_RIGHT:  # 按下右键
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # 按下左键
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:  # 按空格键就创建一颗子弹加入到编组中
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """响应按下按键的事件"""
    if event.key == pygame.K_RIGHT:  # 松开右键
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:  # 松开左键
        ship.moving_left = False

            
def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    # 事件都是通过方法pygame.event.get()获取的
    for event in pygame.event.get():  # 事件循环，所有鼠标和键盘事件都将促使for循环运行
        if event.type == pygame.QUIT:  # 点击关闭按钮
            sys.exit()  # 退出游戏
        elif event.type == pygame.KEYDOWN:  # 每次按键都被注册为一个KEYDOWN事件
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    # 删除已消失的子弹
    # for循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            # 如果子弹从屏幕中消失，就从bullets中删除
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:  # 超过最大子弹数则不创建新的子弹
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都重绘屏幕
    # screen.fill()用背景色填充屏幕，接收一个表示颜色的实参
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    # 方法bullets.sprite()返回一个列表，包含编组bullets中所有的sprite
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()  # 绘制飞船
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()  # 每次执行while循环都绘制一个空屏幕，擦去旧屏幕
