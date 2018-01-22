# -*- coding: utf-8 -*-
'''
Created on 2018年1月22日

@author: Jeff Yang
'''

import sys
from time import sleep
import pygame
from chapter13_aliens.bullet import Bullet
from chapter13_aliens.alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按下按键的事件"""
    if event.key == pygame.K_RIGHT:  # 按下右键
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # 按下左键
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:  # 按空格键就创建一颗子弹加入到编组中
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:  # 按下q键退出游戏
        sys.exit()


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


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    # 删除已消失的子弹
    # for循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            # 如果子弹从屏幕中消失，就从bullets中删除
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """响应子弹和外星人的碰撞"""
    # 检查是否有子弹击中了外星人，如果有，就删除相应的子弹和外星人
    # 方法sprite.groupcollide()检查两个编组之间的元素有没有发生碰撞
    # 它返回一个字典，键是子弹，值是被该子弹击中的外星人，每当有子弹和外星人的rect重叠，就在返回的字典中添加一个键值对
    # 如果第一个布尔值设为False，第二个设为True的话，子弹击中一个外星人后也不会消失，外星人会消失（模拟超级子弹）
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()  # 删除编组中余下的所有元素
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:  # 超过最大子弹数则不创建新的子弹
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都重绘屏幕
    # screen.fill()用背景色填充屏幕，接收一个表示颜色的实参
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    # 方法bullets.sprite()返回一个列表，包含编组bullets中所有的sprite
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()  # 绘制飞船
    # 对编组调用draw()时，pygame将自动绘制编组的每个元素，绘制位置由元素的属性rect决定
    aliens.draw(screen)  # 绘制外星人群
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()  # 每次执行while循环都绘制一个空屏幕，擦去旧屏幕


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少外星人"""
    # 屏幕宽度减去左右各空一个外星人的宽度
    available_space_x = ai_settings.screen_width - 2 * alien_width  # 计算一行容纳多少个外星人
    # 相邻外星人之间的间距为一个外星人宽度，int()舍去小数部分，range()也需要整数
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    # 屏幕高度减去上方空一个外星人高度和飞船的高度还有留两个空行留给玩家射杀外星人的时间
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    # 相邻外星人间隔一个外星人高度
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width  # 外星人的宽度
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)  # 添加到编组中


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应措施"""
    for alien in aliens.sprites():
        if alien.check_edges():  # 检查每个外星人有没有碰到边缘
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移,并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed  # 下移外星人
    ai_settings.fleet_direction *= -1  # 乘以-1达到改变方向的效果


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """响应外星人撞到飞船"""
    if stats.ships_left > 0:
        # 将ship_left减1
        stats.ships_left -= 1
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人，并将飞船放到屏幕中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停
        sleep(1)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达了底部"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:  # 外星人底部坐标大于或等于屏幕底部坐标
            # 像飞船被撞到一样处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人位于屏幕边缘，并更新整群外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # 检查外星人和飞船之间的碰撞
    # 方法sprite.spritecollideany()接受两个实参，一个sprite一个编组
    # 它检查sprite是否与编组的成员发生碰撞，返回第一个与飞船发生碰撞的外星人，如果没有碰撞将返回None
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    
    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
