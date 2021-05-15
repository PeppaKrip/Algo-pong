from pygame import *

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
        if keys_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= win_height - 80:
            self.rect.y += self.speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Ball(GameSprite):
    pass

window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-понг')

clock = time.Clock()
fps = 60
window.fill([255,189,179])
game = True

player1 = Player1('player.jpg',70 , 140, 30, 120, 8)
player2 = Player2('player.jpg',600 , 140, 30, 120, 8)

while game:
    player1.update()
    player1.reset()
    player2.update()
    player2.reset()
    for i in event.get():
        if i.type == QUIT:
            game = False
    display.update()
    clock.tick(fps)