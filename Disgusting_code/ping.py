from pygame import *
from random import randint

win_height = 500 
win_width = 700

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 2:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= win_height - 120:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 2:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= win_height - 120:
            self.rect.y += self.speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Ball(GameSprite):
    def start():
        pass
    def fly():
        pass
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-понг')

clock = time.Clock()
fps = 60
game = True

ball = Ball('ball.jpg',330 , 230, 30, 30, 8)
player1 = Player('player.jpg',70 , 180, 30, 120, 8)
player2 = Player('player.jpg',600 , 180, 30, 120, 8)

ball_speed_x = 3
ball_speed_y = 3

font.init()
font1 = font.SysFont('Arial', 50)

player1_win = font1.render('Игрок справа победил!', 1, (254,214,218))
player2_win = font1.render('Игрок слева победил!', 1, (254,214,218))

while game:
    window.fill([255,189,179])
    if game != False:
        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y
    if ball.rect.y > win_height - 30 or ball.rect.y < 0:
        ball_speed_y *= -1
    if ball.rect.x > win_width:
        window.blit(player2_win, (150, 220))
    if ball.rect.x < 0:
        window.blit(player1_win, (150, 220))
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        ball_speed_x *= -1
    for i in event.get():
        if i.type == QUIT:
            game = False
    ball.reset()
    player1.update_r()
    player1.reset()
    player2.update_l()
    player2.reset()

    display.update()
    clock.tick(fps)