import pygame.event
from pygame import *
import Feld
import Wand
import Spielfeld
import os
import csv

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

def main():
    levelStrArr = importCSV()

    spielfeld = Spielfeld.Spielfeld(levelStrArr)
    fensterbreite = 800
    fensterhöhe = 400
    fenster = pygame.display.set_mode((fensterbreite, fensterhöhe))
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        spielfeld.drawSpielfeld(fenster)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False

if __name__ == '__main__':
    main()
