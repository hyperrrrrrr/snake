import pygame as p
from time import sleep
import random

width, height = 300, 300
window = p.display.set_mode((width, height))
p.display.set_caption("Snake")


black = (0, 0, 0)
white = (255, 255, 255)
snakeAsset = p.image.load('assets/snake.png')
foodAsset = p.image.load('assets/food.png')

movementDirection = 2  # 0 = up 1 = down 2= left and 3 = right
movementDistance = 10
movementDelay = 0.19


def draw(dots):
    window.fill(black)
    for dot in dots:
        window.blit(snakeAsset, dot)
    p.display.update()


def dotCheck(dots):
    """
    dots - list, contains coordinates of the snake 

    Checks the position of the snake relitave to boundaries (borders)
    """
    if dots[0][0] < 0 or dots[0][1] < 0 or dots[0][0] > width or dots[0][1] > height:
        return False
    for dot in dots[1:len(dots)]:
        if dot == dots[0]:
            return False
    return True


def food(foodList, dots):
    while len(foodList) != 5:
        found = True
        while found:
            found = False
            new = random.randint(0, width/movementDistance) * movementDistance, random.randint(
                0, height/movementDistance) * movementDistance
            for dot in dots:
                if dot == new:
                    found = True
            for food in foodList:
                if food == new:
                    found = True
        foodList.append([new])
    return foodList


def drawFood(foodList):
    for food in foodList:
        window.blit(foodAsset, food[0])
    p.display.update()


def eatFood(foodList, head):
    for food in foodList:
        if head == food[0]:
            foodList.remove(food)
            return True


def movement(dots, add):
    temp = 0
    newDot = []
    for dot in dots:
        if temp == 0:
            if movementDirection == 0:
                newDot.append((dot[0], dot[1] - movementDistance))
            elif movementDirection == 1:
                newDot.append((dot[0], dot[1] + movementDistance))
            elif movementDirection == 2:
                newDot.append((dot[0] - movementDistance, dot[1]))
            elif movementDirection == 3:
                newDot.append((dot[0] + movementDistance, dot[1]))
            temp = dot
        else:
            newDot.append(temp)
            temp = dot
    if add:
        newDot.append(temp)
    return newDot


dots = [(250, 250)]
run = True
foodList = []
while run:
    pause = False
    run = dotCheck(dots)
    sleep(movementDelay)
    foodList = food(foodList, dots)
    dots = movement(dots, eatFood(foodList, dots[0]))
    draw(dots)
    drawFood(foodList)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT and movementDirection != 3:
                movementDirection = 2
            if event.key == p.K_RIGHT and movementDirection != 2:
                movementDirection = 3
            if event.key == p.K_UP and movementDirection != 1:
                movementDirection = 0
            if event.key == p.K_DOWN and movementDirection != 0:
                movementDirection = 1
                

            if event.key == p.K_:
                movementDirection = 1

