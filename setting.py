#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/6 10:03
# @Author : Seeumt
# @File : setting.py
class Setting:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.background = "images/bg0.png"
        self.ship_speed = 1
        self.ship_live = 3
        self.ship_live_volume = 10
        self.ship_wudi_time = 80
        self.ship_image = ["images/ship0.png","images/ship1.png"]
        self.gift_image = ["images/gift0.png","images/gift1.png","images/gift2.png"]
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 2
        self.alien_speed = 1
        self.alien_number = 6
        self.alien_drop_speed = 1
        self.alien_direction = 1
        self.alien_image = ["images/player_right.png","images/player_left.png", ]


