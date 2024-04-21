from pygame import*
from random import*

okno = display.set_mode((1200,600))
fps = time.Clock()
game = True

fon = image.load('mramor.jpg')
fon = transform.scale(fon, (1000,600))

points1 = 0
points2= 0
font.init()
wr = font.Font(None, 35)

class gameobj(sprite.Sprite):
    def __init__(self, img, x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))

class player(gameobj):
    def move(self):
        self.ris()
        kn = key.get_pressed()
        if kn[K_LEFT] and self.rect.x > 0:
            self.rect.x -= 7
        elif kn[K_RIGHT] and self.rect. x < 930:
            self.rect.x += 7
platform = player('purple.png', 480,520,100,30)

class player2(gameobj):
    def move(self):
        self.ris()
        kn = key.get_pressed()
        if kn[K_a] and self.rect.x > 0:
            self.rect.x -= 7
        elif kn[K_d] and self.rect. x < 930:
            self.rect.x += 7
platform2 = player2('purple.png', 480,80,100,30)

ball=gameobj("circle.png",600,300,40,40)
dx =1
dy =-1

plita = []
enemies = []

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    okno.fill((0,0,0))
    hp = wr.render(str(points1), False, (255,255,255))
    pp = wr.render(str(points2), False, (255,0,255))
    okno.blit(hp, (1100,40))
    okno.blit(pp, (1100,80))
    
    platform.move()
    platform2.move()
    ball.ris()
    ball.rect.x +=dx
    ball.rect.y +=dy

    if sprite.collide_rect(ball, platform2):
        dy*= -1
        dx = choice([-2,-1,1,2])
    if sprite.collide_rect(ball, platform):
        dy*= -1
        dx = choice([-2,-1,1,2])

    if ball.rect.x <= 0:
        dx*= -1
        dy = choice([-2,-1,1,2])
    if ball.rect.x >= 1000:
        dx*= -1
        dy = choice([-2,-1,1,2])

    if ball.rect.y <= 0:
        points2+=1
        ball.rect.y=300
    if ball.rect.y >= 600:
        points1+=1
        ball.rect.y=300

    fps.tick(60)
    display.update()