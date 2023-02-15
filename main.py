import pygame.event
from pygame import *
import Feld
import Wand
import Spielfeld
import os
import csv
import Pacman




def importCSV():
    with open("assets/LVL.CSV") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        temArray = [[]]*22
        lineCounter = 0
        for row in csv_reader:
            temArray[lineCounter]=row
            lineCounter += 1
            #print(lineCounter)
        return temArray

def inputPlayer(Pacman):
    for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_d or event.type == KEYDOWN and event.key == K_RIGHT:
                Pacman.xFeld +=1
            if event.type == KEYDOWN and event.key == K_a or event.type == KEYDOWN and event.key == K_LEFT:
                Pacman.xFeld -=1 
            if event.type == KEYDOWN and event.key == K_w or event.type == KEYDOWN and event.key == K_UP:
                Pacman.yFeld -=1
            if event.type == KEYDOWN and event.key == K_s or event.type == KEYDOWN and event.key == K_DOWN:
                Pacman.yFeld +=1       
            if  event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                return False
    return True
    


def main():
    levelStrArr = importCSV()

    spielfeld = Spielfeld.Spielfeld(levelStrArr)
    fensterbreite = 608
    fensterhöhe = 704
    fenster = pygame.display.set_mode((fensterbreite, fensterhöhe))
    running = True
    clock = pygame.time.Clock()
    frame = 0
    xfeld = 9
    yfeld = 16
    figurPacman = Pacman.Pacman()

    while running:

        clock.tick(14)
        spielfeld.drawSpielfeld(fenster, figurPacman)
        running = inputPlayer(figurPacman)

if __name__ == '__main__':
    main()
# 16, 9