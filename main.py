import pygame
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

if __name__ == '__main__':
    main()
