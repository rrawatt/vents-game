import pygame
import random
from pygame.locals import *
from vents.Die import Die
from vents.Cell import Cell

pygame.init()

skyblue = (140, 206, 235)
skyblue5 = (100, 125, 255)
lightgreen = (144, 238, 144)
lightcoral = (240, 128, 128)
lightpurple=(203, 195, 227)
lemonyellow=(241,235,156)
yellow=(255,150,0)
bluegreen = (8, 143, 143)
lightbrown=(196, 164, 132)
brown=(150,75,0)
darkbrown=(92, 64, 51)
cloud=(123,123,123)
slate=(192, 194, 201)

WIDTH, HEIGHT = 800, 850
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Holes and Vents")

# Grid initialization
mat = [[0 for i in range(10)] for j in range(10)]

# Function to generate vents
def vents():
    vents = []
    for i in range(7):  # Creating vents
        a = random.randrange(2, 98)
        vents.append(a)
    return vents

vent = vents()

def draw_cells():
    for i in range(10):
        for j in range(10):
            state = mat[i][j]
            cell = Cell(i, j, state)
            if j % 2 == 0:
                if (i + 10 * j + 1) in vent:
                    cell.draw_vent(WIN)
                else:
                    cell.draw_cell(WIN)
            else:
                if (9 - i + 10 * j + 1) in vent:
                    cell.draw_vent(WIN)
                else:
                    cell.draw_cell(WIN)

def redraw_window():
    WIN.fill(lightcoral)
    recta = pygame.Rect(105, 65, 540, 540)
    pygame.draw.rect(WIN, bluegreen, recta)
    draw_cells()
    player1.redraw(WIN)
    player2.redraw(WIN)
    die.draw_button(WIN)
    pygame.display.update()


class Player(pygame.sprite.Sprite):
    def __init__(self, col, x, y,n):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.n=n

    def move(self,start,end):
        if ((start-1)//10)%2==0:
            i=(start-1)%10
            j=int((start-1)/10)
        elif ((start-1)//10)%2==1:
            i=10-((start-1)%10+1)
            j=int((start-1)/10)
        for _ in range(abs(end-start)):
            if end>start:
                if i==0 and j==0:
                    i+=1
                elif i!=9 and i!=0:
                    if j%2==0:
                        i+=1
                    else:
                        i-=1
                elif (i==9 and j%2==0):
                    j+=1
                elif(i==0 and j%2==1):
                    j+=1
                elif (i==9 and j%2==1):
                    i-=1
                elif (i==0 and j%2==0):
                    i+=1
                self.rect.x = 100 + i * 60 + 20
                self.rect.y = 600 - j * 60 + 5
            elif start>end:
                if i!=9 and i!=0:
                    if j%2==0:
                        i-=1
                    else:
                        i+=1
                elif (i==9 and j%2==0):
                    i-=1
                elif(i==0 and j%2==1):
                    i+=1
                elif (i==9 and j%2==1):
                    j-=1
                elif (i==0 and j%2==0):
                    j-=1
                self.rect.x = 100 + i * 60 + 20
                self.rect.y = 600 - j * 60 + 5
            redraw_window()

    def redraw(self, WIN):
        WIN.blit(self.image, self.rect.topleft)


def main():
    global player1, player2, die
    run = True
    clock = pygame.time.Clock()
    die = Die()
    player1 = Player((255, 100, 100), 120, 605,0)
    p1=1
    p2=1
    player2 = Player((100, 100, 255), 120, 635,1)
    chance=1

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                break
            elif event.type == MOUSEBUTTONDOWN:
                if die.is_hover(event.pos) and chance==1:
                    die.value = random.randint(1, 6)
                    if p1+die.value>100:
                        die.value=0
                        pass
                    else:
                        player1.move(p1,p1+die.value)

                    p1+=die.value
                    if p1 in vent:
                        x=random.choice(vent)
                        player1.move(p1,x)

                        p1=x
                    chance=2
                    if p1==100:
                        pygame.quit()
                        break
                elif die.is_hover(event.pos) and chance==2:
                    die.value = random.randint(1, 6)
                    if p2+die.value>100:
                        die.value=0
                        pass
                    else:
                        player2.move(p2,p2+die.value)

                    p2+=die.value
                    if p2 in vent:
                        x=random.choice(vent)
                        player2.move(p2,x)

                        p2=x
                    chance=1
                    if p2==100:
                        pygame.quit()
                        break

        redraw_window()
        clock.tick(60)  # Set the frame rate

    pygame.quit()


if __name__ == '__main__':

    main()
