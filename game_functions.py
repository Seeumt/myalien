#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/6 13:30
# @Author : Seeumt
# @File : game_functions.py
import sys
import random
import pygame
from bullet import Bullet
from alien import Alien
from gift import Gift
from pygame.sprite import Group
import time


def change_alien_direction(game_setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y = alien.rect.y + game_setting.alien_drop_speed
    game_setting.alien_direction = game_setting.alien_direction * -1


def check_fleet_edges(game_setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            # change_alien_direction(game_setting,aliens)
            alien.change_direction()
            break


# todo 飞船和怪物碰撞时。。。。
def update_aliens(game_setting, aliens, ship, stats):
    check_fleet_edges(game_setting, aliens)
    aliens.update()
    # todo 新函数 spritecollideany(ship,aliens)
    if pygame.sprite.spritecollideany(ship, aliens):
        ship.live = ship.live - 1
        ship.center_ship()
        if ship.live == 0:
            stats.game_active = False
            pygame.mouse.set_visible(True)
        # pass


def update_gifts(game_setting, gifts, ship, gift_sound):
    # todo 新函数 spritecollideany(ship,aliens)
    if pygame.sprite.spritecollideany(ship, gifts):
        ship.live = ship.live + 1
        gift_sound.play()
        game_setting.alien_speed = game_setting.alien_speed + 0.3
        # play_gift_sound()
        collisions = pygame.sprite.spritecollideany(ship, gifts)
        if ship.level < len(game_setting.ship_image) - 1:
            ship.level = ship.level + 1
            ship.image = pygame.image.load(game_setting.ship_image[ship.level])
        collisions.remove(gifts)


def update_bullets(game_setting, screen, bullets, aliens, gifts, collision_sound):
    # todo 通过让Sprite的Group() 数组里的每个bullet对象调用update()方法，让子弹出现
    # 装好子弹后，直接将Sprite的Group数组对象调用update()方法
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= bullet.screen_rect.top:
            bullets.remove(bullet)
        if bullet.rect.top >= bullet.screen_rect.bottom:
            bullets.remove(bullet)
        if bullet.rect.left >= bullet.screen_rect.right:
            bullets.remove(bullet)
        if bullet.rect.right <= bullet.screen_rect.left:
            bullets.remove(bullet)
    # todo pygame.sprite.groupcollide 碰撞功能 除此之外，如何实现掉落

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        collision_sound.play()
    for bullet in collisions:  # each bullet
        for alien in collisions[bullet]:  # each alien that collides with that bullet
            # print(alien.rect.x,alien.rect.y)
            gift = Gift(screen, game_setting)
            gift.rect.x = alien.rect.x
            gift.rect.y = alien.rect.y
            gifts.add(gift)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(game_setting, screen, aliens)


# def appear_gift(screen, game_setting, x, y):
#     gift = Gift(screen, game_setting)
#     gift.rect.centerx = x
#     gift.rect.centery = y
#     gift.update()


# 1.创建子弹，将子弹加入Sprites的Group数组中
def fire_bullet(game_setting, screen, ship, bullets):
    if len(bullets) < game_setting.bullet_allowed:
        new_bullet = Bullet(game_setting, screen, ship)
        new_bullet.direction = ship.direction
        new_bullet.host = 'ship'
        # print("new_bullet.direction:", new_bullet.direction)
        bullets.add(new_bullet)


def alien_attack(game_setting, screen, aliens, alien_bullets_1):
    for alien in aliens.sprites():
        new_bullet = Bullet(game_setting, screen, alien)
        new_bullet.host = 'alien'
        # new_bullet.direction = ship.direction
        # print("new_bullet.direction:", new_bullet.direction)
        alien_bullets_1.add(new_bullet)
    # for alien in aliens.sprites():
    #     alien_bullets = Group()
    #     alien_bullets = alien_fire_bullet(game_setting, screen, alien, alien_bullets)
    #     alien_bullets.update()
    #     alien_bullets_1.add(alien_bullets)


def alien_fire_bullet(game_setting, screen, alien, alien_bullets):
    new_bullet = Bullet(game_setting, screen, alien)
    new_bullet.host = 'alien'
    new_bullet.direction = alien.direction
    # new_bullet.direction = ship.direction
    # print("new_bullet.direction:", new_bullet.direction)
    alien_bullets.add(new_bullet)

    return alien_bullets


def check_keydown_events(event, game_setting, screen, ship, bullets, shot_sound, aliens, alien_bullets_1):
    if event.key == pygame.K_RIGHT:
        # print("向右走")
        ship.moving_right = True
        ship.direction = "right"
        ship.image = pygame.image.load('images/' + ship.direction + str(ship.level) + '.png')
    if event.key == pygame.K_LEFT:
        # print("向左走")
        ship.moving_left = True
        ship.direction = "left"
        ship.image = pygame.image.load('images/' + ship.direction + str(ship.level) + '.png')
    if event.key == pygame.K_UP:
        # print("向上走")
        ship.moving_up = True
        ship.direction = "up"
        ship.image = pygame.image.load('images/' + ship.direction + str(ship.level) + '.png')
    if event.key == pygame.K_DOWN:
        # print("向下走")
        ship.moving_down = True
        ship.direction = "down"
        ship.image = pygame.image.load('images/' + ship.direction + str(ship.level) + '.png')

    elif event.key == pygame.K_SPACE:
        if len(bullets)<game_setting.bullet_allowed:
            shot_sound.play()
        fire_bullet(game_setting, screen, ship, bullets)
    elif event.key == pygame.K_F1:
        alien_attack(game_setting, screen, aliens, alien_bullets_1)


def check_play_button(game_setting, screen, stats, play_btn, ship, aliens, bullets, gifts, mouse_x, mouse_y):
    btn_clicked = play_btn.rect.collidepoint(mouse_x, mouse_y)
    if btn_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)

        stats.game_active = True
        game_setting.alien_speed = 1
        aliens.empty()
        bullets.empty()
        gifts.empty()

        create_fleet(game_setting, screen, aliens)
        ship.center_ship()
        ship.live = game_setting.ship_live


def check_events(game_setting, screen, ship, bullets, aliens, gifts, shot_sound, bg, stats, play_btn, alien_bullets_1):
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 必须要写大前提事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_setting, screen, ship, bullets, shot_sound, aliens, alien_bullets_1)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        # todo 监听鼠标点击事件
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_setting, screen, stats, play_btn, ship, aliens, bullets, gifts, mouse_x, mouse_y)


def update_screen(game_setting, screen, ship, bullets, aliens, gifts, play_btn, stats, alien_bullets_1):
    # screen.fill(game_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.appear()
    for gift in gifts.sprites():
        gift.appear()

    for alien_bullet in alien_bullets_1.sprites():
        alien_bullet.appear()

    # for alien in aliens.sprites():
    #     alien.appear()
    # todo aliens.draw(screen) 与 appear关系
    ship.appear()
    aliens.draw(screen)
    # print((x,y))
    # appear_gift(screen, game_setting, x, y)
    # alien.appear()
    if not stats.game_active:
        play_btn.draw_button()
    pygame.display.flip()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


def create_fleet(game_setting, screen, aliens):
    alien = Alien(screen, game_setting)
    # number_aliens_x = get_number_alien_x(game_setting, alien.rect.width)
    number_aliens_x = 5
    for alien_number in range(number_aliens_x):
        create_alien(game_setting, screen, aliens, alien_number)


def get_number_alien_x(game_setting, alien_width):
    available_space_x = game_setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(game_setting, screen, aliens, alien_number):
    alien = Alien(screen, game_setting)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = random.randrange(0, game_setting.screen_width - alien_width)
    alien.rect.y = random.randrange(0, game_setting.screen_height - alien_height)

    aliens.add(alien)


def check_alien(game_setting, screen, aliens, alien_bullets_1):
    pass
