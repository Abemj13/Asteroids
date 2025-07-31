import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
GAME_SPEED = None

#asteroids
ASTEROID_MIN_RADIUS = float(20)
ASTEROID_KINDS = int(3)
ASTEROID_SPAWN_RATE = float(0.8)  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
ASTEROID_SPLIT_COUNT = 3

#Shots
SHOT_RADIUS = 5

#players stats
PLAYER_RADIUS = float(20)
PLAYER_TURN_SPEED = float(300)
PLAYER_SPEED = float(200)
PLAYER_HP = float(10)
PLAYER_INV_FRAMES = float(0.5)
PLAYER_SHOOTING_SPEED = float(500)
PLAYER_SHOOT_COOLDOWN = float(0.3)
KILL_COUNT = 0

#economy stats
BASIC_CURRENCY = float(0)

#colors
black = (0,0,0)
white = (255, 255, 255)
neon_blue = (4,217,255)
neon_purple = (138,0,255)
neon_red = (210,39,48)
grey_purple = (134,111,133)