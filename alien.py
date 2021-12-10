#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/7 14:31
# @Author : Seeumt
# @File : alien.py
import random

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, screen, game_setting):
        super(Alien, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_setting = game_setting

        self.image = pygame.image.load("images/down11.png")
        self.rect = self.image.get_rect()

        # todo centerx 与 x 的区别
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        self.direction = 1

        self.stop = False

    def update(self):
        # print(self.stop)
        if not self.stop:
            self.x = self.x + self.game_setting.alien_speed * self.direction
            self.rect.x = self.x


    def check_edges(self):
        if self.rect.right >= self.screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True
        if self.rect.bottom >= self.screen_rect.bottom:
            return True
        if self.rect.top <= 0:
            return True

    def change_direction(self):

        self.rect.y = self.rect.y + self.game_setting.alien_drop_speed*self.direction
        self.direction = self.direction * -1
