from pygame import *
window = display.set_mode((800,800))

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
