from pygame import *
window = display.set_mode((800,600))
class QWERTY(sprite.Sprite):
    def __init__ (self,x,y,img,speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self, window):
        window.blit(self.image,(self.rect.x,self.rect.y))
class FootbolnyMyachik(QWERTY):
    def __init__(self,x,y,img,speed_x, speed_y, w, h):
        super().__init__(x,y,img,0, w, h)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update_position(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    def update_speeds(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y
class Raketka444 (QWERTY):
    def update_1 (self):
        press = key.get_pressed()
        if press[K_w]:
            self.rect.y -= self.speed
        if press[K_s]:
            self.rect.y += self.speed
    def update_2 (self):
        press = key.get_pressed()
        if press[K_UP]:
            self.rect.y -= self.speed
        if press[K_DOWN]:
            self.rect.y += self.speed
speed_x = 3
speed_y = 3
finish = False
clock = time.Clock()
FPS = 60

myachik = FootbolnyMyachik(500, 200, "tenis_ball.png", 2, 2, 20, 20 )
temnaya_storona = Raketka444(50, 400, "racket.png", 100, 40, 100)
svetlaya_storona = Raketka444(750, 400, "racket.png", 100, 40, 100)
run = True
while run:
    window.fill((255,255,134))
    myachik.reset(window)
    temnaya_storona.reset(window)
    temnaya_storona.update_1()
    svetlaya_storona.reset(window)
    svetlaya_storona.update_2()
    myachik.update_position()
    for e in event.get():
        if e.type == QUIT:
            run = False
    if sprite.collide_rect(temnaya_storona, myachik) or sprite.collide_rect(svetlaya_storona, myachik):
        speed_x *= -1
    if myachik.rect.y > 600 - 20 or myachik.rect.y < 0:
        speed_y *= -1
    myachik.update_speeds(speed_x, speed_y)
    display.update()
    clock.tick(FPS)