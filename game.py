import pygame
import os
import random

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

WHITE = (255, 255 ,255)
BLACK = (0, 0, 0)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

FPS = 60
VEL = 3
PLAYER_WIDTH, PLAYER_HEIGHT = 16, 128
BALL_WIDTH, BALL_HEIGHT = 16, 16
ball_speed_x = 5
ball_speed_y = 5

LEFT_PLAYER_IMAGE = pygame.image.load(os.path.join('Assets', 'player_left.jpg'))
LEFT_PLAYER = pygame.transform.scale(LEFT_PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
RIGHT_PLAYER_IMAGE = pygame.image.load(os.path.join('Assets', 'player_right.jpg'))
RIGHT_PLAYER = pygame.transform.scale(RIGHT_PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
#BALL_IMAGE = pygame.image.load(os.path.join('Assets', 'ball.jpg'))
ball = pygame.Rect(WIDTH/2 - 16, HEIGHT/2 - 16, 32, 32)

def draw_window(left, right, ball):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, BORDER)
    pygame.draw.rect(WIN, WHITE, ball)
    WIN.blit(LEFT_PLAYER, (left.x, left.y))
    WIN.blit(RIGHT_PLAYER, (right.x, right.y))
    pygame.display.update()

def handle_left_movement(keys_pressed, left):
    if keys_pressed[pygame.K_w] and left.y - VEL > 0:  # UP
        left.y -= VEL
    if keys_pressed[pygame.K_s] and left.y + VEL + left.height < HEIGHT:  # DOWN
        left.y += VEL

def handle_right_movement(keys_pressed, right):
    if keys_pressed[pygame.K_UP] and right.y - VEL > 0:  # UP
        right.y -= VEL
    if keys_pressed[pygame.K_DOWN] and right.y + VEL + right.height < HEIGHT:  # DOWN
        right.y += VEL

def handle_ball_movement(ball):
    ball.x += ball_speed_x
    ball.y += ball_speed_y

def handle_ball_collision(ball, left, right):
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        global ball_speed_y
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        global ball_speed_x
        ball_speed_x *= -1
    if ball.left <= left.x or ball.right >= right.x:
        ball_speed_x *= -1
    if right.y >= ball.top or ball.top <= left.y:
        ball_speed_y *= -1

def main():
    left = pygame.Rect(100, 200, PLAYER_WIDTH, PLAYER_HEIGHT)
    right = pygame.Rect(790, 200, PLAYER_WIDTH, PLAYER_HEIGHT)
    ball = pygame.Rect(450, 250, BALL_WIDTH, BALL_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        handle_left_movement(keys_pressed, left)
        handle_right_movement(keys_pressed, right)
        handle_ball_movement(ball)
        handle_ball_collision(ball, left, right)
        draw_window(left, right, ball)

    pygame.quit()

if __name__ == "__main__":
    main()