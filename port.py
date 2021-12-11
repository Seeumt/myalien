#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/10 20:19
# @Author : Seeumt
# @File : port.py

import pygame

from alien import Alien
from button import Button
from game_stats import GameStats
from gift import Gift
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def pre_prepare(scene):
    game_setting = Setting()

    pygame.mixer.music.load('sound/piano1.mp3')  # 加载背景音乐
    pygame.mixer.music.set_volume(100)  # 设置音量
    pygame.mixer.music.play(-1, 0.0)
    gift_sound = pygame.mixer.Sound('sound/gift4.mp3')
    shot_sound = pygame.mixer.Sound('sound/attack.mp3')
    collision_sound = pygame.mixer.Sound('sound/collision2.mp3')
    screen = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))
    ship = Ship(screen, game_setting)
    pygame.display.set_caption("game")
    bullets = Group()
    aliens = Group()
    alien_bullets_1 = Group()
    gf.create_fleet(game_setting, screen, aliens, scene)
    gifts = Group()
    boss = Alien(screen, game_setting)
    boss.image_url = 'images/boss' + str(scene) + '_right.png'
    boss.image = pygame.image.load(boss.image_url)
    boss.type_ = "boss"
    boss.power = scene + 1

    stats = GameStats(game_setting)
    play_btn = Button(game_setting, screen, "PLAY", 200, 50, screen.get_width() / 2, 200, "images/continue0.png")
    start_btn = Button(game_setting, screen, "START", 200, 50, screen.get_width() / 2, 200, "images/start0.png")
    help_btn = Button(game_setting, screen, "HELP", 200, 50, screen.get_width() / 2, 400, "images/help0.png")
    exit_btn = Button(game_setting, screen, "EXIT", 200, 50, screen.get_width() / 2, 600, "images/exit0.png")
    dest_btn = Button(game_setting, screen, "DESTINATION", 100, 40,
                      screen.get_rect().centerx - pygame.image.load("images/ship_love.png").get_rect().width // 2,
                      screen.get_rect().top, "images/ship_love.png")
    cheers_btn = Button(game_setting, screen, "CHEERS", 100, 40,
                        screen.get_rect().centerx - pygame.image.load("images/cheers0.png").get_rect().centerx, 200,
                        "images/cheers0.png")
    return game_setting, gift_sound, shot_sound, collision_sound, screen, ship, bullets, aliens, alien_bullets_1, gifts, stats, play_btn, start_btn, help_btn, exit_btn, dest_btn, cheers_btn, boss


def game1(scene):
    # todo pygame的内置构建screen对象函数 display.set_mode

    bg = pygame.image.load('./images/bg1.png').convert()
    game_setting, gift_sound, shot_sound, collision_sound, screen, ship, bullets, aliens, alien_bullets_1, gifts, stats, play_btn, start_btn, help_btn, exit_btn, dest_btn, cheers_btn, boss = pre_prepare(
        scene)

    while True:
        # print(ship.wudi_time)
        if ship.wudi:
            ship.wudi_time = ship.wudi_time - 0.5
            if ship.wudi_time <= 0:
                ship.wudi = False
        gf.check_events(game_setting, screen, ship, bullets, aliens, gifts, shot_sound, bg, stats, play_btn, exit_btn,
                        alien_bullets_1, scene)

        if stats.game_active:
            ship.move()
            gf.update_bullets(game_setting, screen, ship, bullets, aliens, gifts, collision_sound, scene)
            gf.update_aliens(game_setting, bullets, aliens, gifts, ship, stats)
            # gf.check_alien(game_setting,screen,aliens,alien_bullets_1)
            gf.update_gifts(game_setting, gifts, ship, gift_sound)
            gf.update_ship(game_setting, ship, stats)
            gf.update_test(ship, boss, aliens)
            # gf.update_knife(game_setting,ship,stats,aliens)
            life_rect = pygame.image.load("images/life.jpeg")
            life_ = pygame.transform.scale(life_rect, (
                life_rect.get_rect()[2] * abs(ship.live_volume), life_rect.get_rect()[3]))
            screen.blit(life_, (10, 10))

        dest_btn.draw_btn()

        gf.update_screen(game_setting, screen, ship, bullets, aliens, gifts, play_btn, exit_btn, stats, alien_bullets_1)

        # if ship.rect.top <= 0 + ship.rect.height // 2:
        #     gf.resetShip(ship, game_setting)
        #     pygame.mouse.set_visible(True)
        #     cheers_btn.draw_btn()
        #     stats.game_active = False
        if ship.win:
            return 2

        pygame.display.flip()


def game2(scene):
    bg = pygame.image.load('./images/bg2.png').convert()
    game_setting, gift_sound, shot_sound, collision_sound, screen, ship, bullets, aliens, alien_bullets_1, gifts, stats, play_btn, start_btn, help_btn, exit_btn, dest_btn, cheers_btn, boss = pre_prepare(
        scene)
    while True:
        # print(ship.wudi_time)
        if ship.wudi:
            ship.wudi_time = ship.wudi_time - 0.5
            if ship.wudi_time <= 0:
                ship.wudi = False
        gf.check_events(game_setting, screen, ship, bullets, aliens, gifts, shot_sound, bg, stats, play_btn, exit_btn,
                        alien_bullets_1, scene)

        if stats.game_active:
            ship.move()
            gf.update_bullets(game_setting, screen, ship, bullets, aliens, gifts, collision_sound, scene)
            gf.update_aliens(game_setting, bullets, aliens, gifts, ship, stats)
            # gf.check_alien(game_setting,screen,aliens,alien_bullets_1)
            gf.update_gifts(game_setting, gifts, ship, gift_sound)
            gf.update_ship(game_setting, ship, stats)
            gf.update_test(ship, boss, aliens)
            # gf.update_knife(game_setting,ship,stats,aliens)
            life_rect = pygame.image.load("images/life.jpeg")
            life_ = pygame.transform.scale(life_rect, (
                life_rect.get_rect()[2] * abs(ship.live_volume), life_rect.get_rect()[3]))
            screen.blit(life_, (10, 10))

        dest_btn.draw_btn()

        gf.update_screen(game_setting, screen, ship, bullets, aliens, gifts, play_btn, exit_btn, stats, alien_bullets_1)

        if ship.win:
            return 3
        pygame.display.flip()


def game3(scene):
    bg = pygame.image.load('./images/bg3.png').convert()
    game_setting, gift_sound, shot_sound, collision_sound, screen, ship, bullets, aliens, alien_bullets_1, gifts, stats, play_btn, start_btn, help_btn, exit_btn, dest_btn, cheers_btn, boss = pre_prepare(
        scene)
    while True:
        # print(ship.wudi_time)
        if ship.wudi:
            ship.wudi_time = ship.wudi_time - 0.5
            if ship.wudi_time <= 0:
                ship.wudi = False
        gf.check_events(game_setting, screen, ship, bullets, aliens, gifts, shot_sound, bg, stats, play_btn, exit_btn,
                        alien_bullets_1, scene)

        if stats.game_active:
            ship.move()
            gf.update_bullets(game_setting, screen, ship, bullets, aliens, gifts, collision_sound, scene)
            gf.update_aliens(game_setting, bullets, aliens, gifts, ship, stats)
            # gf.check_alien(game_setting,screen,aliens,alien_bullets_1)
            gf.update_gifts(game_setting, gifts, ship, gift_sound)
            gf.update_ship(game_setting, ship, stats)
            gf.update_test(ship, boss, aliens)
            # gf.update_knife(game_setting,ship,stats,aliens)
            life_rect = pygame.image.load("images/life.jpeg")
            life_ = pygame.transform.scale(life_rect, (
                life_rect.get_rect()[2] * abs(ship.live_volume), life_rect.get_rect()[3]))
            screen.blit(life_, (10, 10))

        dest_btn.draw_btn()

        gf.update_screen(game_setting, screen, ship, bullets, aliens, gifts, play_btn, exit_btn, stats, alien_bullets_1)

        if ship.win:
            return 4
        pygame.display.flip()
