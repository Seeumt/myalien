#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/8 16:48
# @Author : Seeumt
# @File : button.py
import pygame


class Button:
    def __init__(self,game_setting,screen,msg,width,height,x=0,y=0,path=""):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = width
        self.height = height
        self.button_color = (255, 255, 102)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        if path=="":
            self.rect = pygame.Rect(x,y,self.width,self.height)
        else:
            self.rect = pygame.image.load(path).get_rect()
            self.image = pygame.image.load(path)
        self.rect.x = x
        self.rect.y = y
        # self.rect.center = self.screen_rect.center

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

    def draw_btn(self):
        # 绘制一个用颜色填充的按钮，再绘制文本


        self.screen.blit(self.image,(self.rect.x,self.rect.y))
        # self.rect = pygame.image.load(path).get_rect()


