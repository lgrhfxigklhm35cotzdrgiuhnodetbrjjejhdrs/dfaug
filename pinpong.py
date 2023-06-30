from pygame import *
from random import randint
'''Необходимые классы'''


#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y,player_width, player_height, player_speed):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

        

back = (200,255,255)
#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
#Персонажи игры:
player = Player('WhatsApp Image 2023-06-10 at 19.27.20.jpeg', 30,200,50,150,4)
player2 = Player('WhatsApp Image 2023-06-10 at 19.27.20.jpeg', 520,200,50,150,4)
ball = GameSprite('WhatsApp Image 2023-06-10 at 19.27.20(1).jpeg', 200,200,50,50,4)

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180,0,0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180,0,0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    if finish != True:
        window.fill(back)
        player.update()
        player2.update2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player,ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = Truewindow.blit(lose1, (200,200))
            game_over = True

        player.reset()
        player2.reset()
        ball.reset()


        display.update()
        clock.tick(FPS)