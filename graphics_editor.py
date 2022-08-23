import pygame
import random
import time
from PIL import Image
from pathlib import Path

pygame.init()

#images
firstbutton = pygame.image.load('first.png')
secondbutton = pygame.image.load('second.png')
thirdbutton = pygame.image.load('third.png')
right = pygame.image.load('leftPanel.png')
logo = pygame.image.load('logo.png')
mainImg = 1
f1 = pygame.font.Font(None, 20)
text = f1.render('', 1, (0, 255, 0))

#win settings
width = 600
height = 600
screensize = 500
a = 1
colorsA = 5

#button settings
buttonWidth = 166
buttonHeight = 100

#brush settings
size = 3  
fir = 0
sec = 0
thir = 0

#other settings
run = True
wannaMakeSomeStrange = False
start = True
gone = False
inDrawing = False

#functions
def randomPaint():
    x = 0
    y = 0

    while y <= 500:
        pygame.draw.rect(win, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (x, y, colorsA, colorsA))
        x = x + colorsA
        if x == screensize:
            x = 0
            y = y + colorsA

def makeButtons():
    pygame.draw.rect(win, (100, 100, 100), (0, screensize, buttonWidth + 5, buttonHeight))
    win.blit(firstbutton, (0, screensize))
    pygame.draw.rect(win, (50, 50, 50), (buttonWidth, screensize, buttonWidth + 5, buttonHeight))
    #win.blit(thirdbutton, (buttonWidth, screensize))
    pygame.draw.rect(win, (100, 100, 100), (buttonWidth + buttonWidth, screensize, buttonWidth + 5, buttonHeight))
    pygame.draw.rect(win, (fir, sec, thir), (screensize, 400, 100, 100))
    win.blit(right, (screensize, 0))
    win.blit(secondbutton, (buttonWidth + buttonWidth, screensize))
    pygame.draw.rect(win, (fir, sec, thir), (screensize, 300, 110, 105))

def drawPoint(cx, cy, size):
    pygame.draw.rect(win, (fir, sec, thir), (((round(cx/a)*a) - (size / 2)), ((round(cy/a)*a) - (size / 2)), size, size))

def drawLine(x1, y1, x2, y2, size):
    pygame.draw.line(win, (fir, sec, thir), [x1, y1], [x2, y2], size)
    #pygame.draw.line(win, (fir, sec, thir), (x1, y1, size, size))

#things to start
win = pygame.display.set_mode((width, height))
pygame.display.flip()
win.fill((255,255,255))

while run:
    #if gone == False:
        #win.blit(logo, (0, 0))
        #time.sleep(3)
        #gone = True
        #start = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                cx, cy = pygame.mouse.get_pos()
                x1, y1 = pygame.mouse.get_pos()
                if cy <= screensize:
                    inDrawing = True
                    drawPoint(cx, cy, size)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                inDrawing = False
                cx, cy = pygame.mouse.get_pos()
                drawPoint(cx, cy, size)
        if event.type == pygame.MOUSEMOTION:
            if inDrawing:
                x2, y2 = pygame.mouse.get_pos()
                drawLine(x1, y1, x2, y2, size)
                x1 = x2
                y1 = y2

        if event.type == pygame.MOUSEBUTTONDOWN:
            if cy > screensize or cx > screensize:
                if cx <=buttonWidth:
                    wannaMakeSomeStrange = True
                if cx <= (buttonWidth + buttonWidth + buttonWidth):
                    pygame.image.save(win, 'image.png')
                    mainImg = pygame.image.load('image.png')
                    imgfile = Path('image.png')
                    img = Image.open(imgfile)
                    width = img.size[0]
                    height = img.size[1]
                    img3 = img.crop((0, 0, width-100, height-100))
                    img3.save('image.png')
                if cx > screensize and cy > screensize and a > 1:
                        a = a - 1
                        size = a
                        text = f1.render(str(size), 1, (0, 255, 0))
                if cx > screensize and  cy > (screensize - 100) and cy < 500:
                        a = a + 1
                        size = a
                        text = f1.render(str(size), 1, (0, 255, 0))

                if cx > screensize and cx < (screensize + 50) and  cy > (screensize - 300) and cy < 300 and thir <= 250:
                    thir = thir + 5
                    print(thir)
                if cx > (screensize + 50) and  cy > (screensize - 300) and cy < 300 and thir > 0:
                    thir = thir - 5
                    print(thir)
                if cx > screensize and cx < (screensize + 50) and  cy > 100 and cy < 200 and sec <= 250:
                    sec = sec + 5
                    print(sec)
                if cx > (screensize + 50) and  cy > 100 and cy < 200 and sec > 0:
                    sec = sec - 5
                    print(sec)
                if cx > screensize and cx < (screensize + 50) and  cy > 0 and cy < 100 and fir <= 250:
                    fir = fir + 5
                    print(fir)
                if cx > (screensize + 50) and  cy > (screensize - 500) and cy < 100 and fir > 0:
                    fir = fir - 5
                    print(fir)

    if wannaMakeSomeStrange:
        randomPaint()
        wannaMakeSomeStrange = False

    if start:
        makeButtons()

    win.blit(text, (screensize, screensize))
    win.blit(text, (screensize, screensize - 95))

    pygame.display.update()
 
