from pygame import *
window = display.set_mode((800,800))


class QWERTY(sprite.Sprite):
    def __init__ (self,x,y,img,speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (60,60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self, window):
        window.blit(self.image,(self.rect.x,self.rect.y))

class FootbolnyMyachik(QWERTY):
    def __init__(self,x,y,img,speed_x, speed_y):
        super().__init__(x,y,img,speed)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update_position(self):
        self.rect.x +=
        self.rect.y +=
    def update_speeds(self):
        self.rect_x += self.speed_x
        self.rect_+= self.speed_y



run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
    
