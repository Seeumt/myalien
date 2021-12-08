#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/6 10:39
# @Author : Seeumt
# @File : ship.py
import pygame


class Ship:
    # todo 如何把一个对象放到屏幕上，用pygame构造的屏幕对象
    # todo 将settings作为构造函数的参数，传入对象内
    def __init__(self, screen, game_setting):
        self.screen = screen

        self.level = 0
        self.image = pygame.image.load(game_setting.ship_image[self.level])
        # 图片的矩形，就作为飞船的矩形
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.ship_speed = game_setting.ship_speed

        self.direction = "up"



    def appear(self):
        # todo 在屏幕指定位置绘制对象,显示对象,screen内置的
        self.screen.blit(self.image, self.rect)

    def move(self):
        # todo 对象矩形右边缘&屏幕右边缘
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx = self.rect.centerx + self.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx = self.rect.centerx - self.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.centery = self.rect.centery - self.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery = self.rect.centery + self.ship_speed

    # def check_role_position(self):