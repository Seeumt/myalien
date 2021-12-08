#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/8 16:48
# @Author : Seeumt
# @File : button.py
import pygame


class Button:
    def __init__(self,game_setting,screen,msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 200
        self.height = 50
        self.button_color = (255, 255, 102)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    # 将字符串渲染为图像
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


