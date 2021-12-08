#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/5 21:55
# @Author : Seeumt
# @File : maingame.py
import pygame

from gift import Gift
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
def run_game():
    pygame.init()
    game_setting = Setting()

    pygame.mixer.music.load('./sound/piano1.mp3')  # 加载背景音乐
    pygame.mixer.music.set_volume(100)  # 设置音量
    pygame.mixer.music.play(-1)

    # todo pygame的内置构建screen对象函数 display.set_mode
    screen = pygame.display.set_mode((game_setting.screen_width,game_setting.screen_height))
    ship = Ship(screen,game_setting)
    pygame.display.set_caption("game")
    bullets = Group()
    aliens = Group()

    gf.create_fleet(game_setting,screen,aliens)
    bg = pygame.image.load('./images/bg0.png').convert()
    gifts = Group()
    while True:

        # print("while..........................")
        # 一次循环，可以拿到好几个事件，循环遍历这些事件,但实际程序循环太快了，一次就一个事件
        gf.check_events(game_setting,screen,ship,bullets)
        ship.move()
        gf.update_bullets(game_setting,screen,bullets,aliens,gifts)
        gf.update_aliens(game_setting,aliens,ship)
        gf.update_gifts(game_setting,gifts,ship)
        gf.update_screen(game_setting,screen,ship,bullets,aliens,gifts,bg)

run_game()

