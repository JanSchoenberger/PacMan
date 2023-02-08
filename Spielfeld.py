import Feld
import pygame
from Pacman import *
class Spielfeld:
    feldGroesse = 30
    spielfeldArr = [[]]*22

    #Spielfeldinitialisierung:
    def __init__(self, strArr):
        countLine = 0
        countChar = 0
        self.spielfeldArr = strArr
        for reihe in self.spielfeldArr:
            for char in reihe: # self.spielfeldArr[reihe][charNr]:
                #print(strArr[countLine][countChar], end="")
                tempObj = None
                tempPun = False
                tempPow = False
                tempArea = None
                tempWall = False
                if(char=="W"):
                    tempArea = pygame.Rect(countChar*self.feldGroesse+countChar*2, countLine*self.feldGroesse+countLine*2, self.feldGroesse, self.feldGroesse)
                    tempWall = True
                if(char=="M"):
                    tempPun=True
                    tempArea = pygame.Rect(countChar*self.feldGroesse+countChar*2, countLine*self.feldGroesse+countLine*2, self.feldGroesse, self.feldGroesse)
                if(char=="P"):
                    tempPow=True
                    tempArea = pygame.Rect(countChar*self.feldGroesse+countChar*2, countLine*self.feldGroesse+countLine*2, self.feldGroesse, self.feldGroesse)
                if(char=="E"):
                    tempArea = pygame.Rect(countChar*self.feldGroesse+countChar*2, countLine*self.feldGroesse+countLine*2, self.feldGroesse, self.feldGroesse)
                self.spielfeldArr[countLine][countChar] = Feld.Feld(tempObj, tempPun, tempPow, tempArea, tempWall)
                countChar +=1
            countChar =0
            countLine +=1
        self.spielfeldArr[16][9].object = Pacman()
        self.spielfeldArr[16][9].punktBool = False


    def drawSpielfeld(self, fenster):
        pygame.display.set_caption("Kawaiiman")
        fenster.fill((0, 0, 0))
        for y in self.spielfeldArr:
            for x in y:
                xColor = (0,0,60)
                if x.wall == True:
                    xColor = (40,40,255)
                elif x.object != None:
                    xColor = (180,180,0)
                elif x.punktBool == True:
                    xColor = (120,120,0)
                elif x.powerUpBool == True:
                    xColor = (180,0,180)
                
                pygame.draw.rect(fenster, xColor, x.area)
        pygame.display.update()
"""
Spielfeld
	Array von Feldern 19x22
	Hintergrund Sprite
	Rectangle für Spielfeld
	Rectangle für Score
	pygame.window
"""