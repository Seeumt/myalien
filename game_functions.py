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


def update_aliens(game_setting, aliens, ship):
    check_fleet_edges(game_setting, aliens)
    aliens.update()
    # todo 新函数 spritecollideany(ship,aliens)
    if pygame.sprite.spritecollideany(ship, aliens):
        # print("Oops")
        pass


def update_gifts(game_setting, gifts, ship):
    # todo 新函数 spritecollideany(ship,aliens)
    if pygame.sprite.spritecollideany(ship, gifts):

        play_gift_sound()
        collisions = pygame.sprite.spritecollideany(ship, gifts)
        if ship.level < len(game_setting.ship_image)-1:
            ship.level = ship.level + 1
            ship.image = pygame.image.load(game_setting.ship_image[ship.level])
        collisions.remove(gifts)

def play_gift_sound():
    pygame.mixer.music.load('sound/gift.mp3')  # 加载背景音乐
    pygame.mixer.music.set_volume(100)  # 设置音量
    pygame.mixer.music.play()

def update_bullets(game_setting, screen, bullets, aliens, gifts):
    # todo 通过让Sprite的Group() 数组里的每个bullet对象调用update()方法，让子弹出现
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
#     # todo 加了pygame.display.flip()为啥只是闪了一下

def fire_bullet(game_setting, screen, ship, bullets):
    if len(bullets) < game_setting.bullet_allowed:
        new_bullet = Bullet(game_setting, screen, ship)
        new_bullet.direction = ship.direction
        # print("new_bullet.direction:", new_bullet.direction)
        bullets.add(new_bullet)


def check_keydown_events(event, game_setting, screen, ship, bullets):
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
        # print("攻击")
        fire_bullet(game_setting, screen, ship, bullets)


def check_events(game_setting, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 必须要写大前提事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(game_setting, screen, ship, bullets, aliens, gifts, bg):
    screen.blit(bg, (0, 0))
    # screen.fill(game_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.appear()
    for gift in gifts.sprites():
        gift.appear()
    # for alien in aliens.sprites():
    #     alien.appear()
    # todo aliens.draw(screen) 与 appear关系
    ship.appear()
    aliens.draw(screen)
    # print((x,y))
    # appear_gift(screen, game_setting, x, y)
    # alien.appear()
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
