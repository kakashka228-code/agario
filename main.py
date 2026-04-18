from pygame import *
from random import randint
from math import hypot

init()

WINDOW_SIZE = 800, 600
FPS = 60

running = True
lose = False

screen = display.set_mode(WINDOW_SIZE)
display.set_caption("AGAR.IO")

clk = time.Clock()

class Player:
    def __init__(self,x,y,r,name,color=(255,0,0)):
        self.x = x
        self.y = y
        self.r = r
        self.name = name
        self.color = color

    def move (self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.y -= 5
        if keys[K_s]:
            self.y += 5 
        if keys[K_a]:
            self.x -= 5
        if keys[K_d]:
            self.x += 5

    def draw(self, scale):
        draw.circle(screen, self.color, (400,300), self.r*scale)


class Food:
    def __init__(self):
        self.x = randint(-2000,2000)
        self.y = randint(-2000,2000)
        self.r = 10
        self.color = (randint(10,255),randint(10,255),randint(10,255))

    def check_collission(self,player):
        dx = self.x - player.x
        dy = self.y - player.y
        return hypot(dx,dy) < self.r + player.r
    
    def draw(self,sx,sy):
        draw.circle(screen, self.color, (sx,sy), self.r)



my_Player = Player(0,0,30,"Player")
foods = [Food() for _ in range(300)]




while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    screen.fill((255,255,255))

    scale = max(0.3, min(50, my_Player.r / 50))
    my_Player.move()
    my_Player.draw(scale)

    to_remove = []
    for f in foods:
        if f.check_collission(my_Player):
            my_Player.r += int(f.r * 0.2)
            to_remove.append(f)
        else:
            sx = int((f.x - my_Player.x) * scale + 400)
            sy = int((f.y - my_Player.y) * scale + 300)
            f.draw(sx,sy)

    for f in to_remove: foods.remove(f)


    display.update()
    clk.tick(FPS)
