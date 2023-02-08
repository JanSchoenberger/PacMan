import Feld
import pygame
class Spielfeld:
    feldGroesse = 20
    spielfeldArr = [[]]*22

    #Spielfeldinitialisierung:
    def __init__(self, strArr):
        countLine = 0
        countChar = 0
        for reihe in self.spielfeldArr:
            for char in reihe: # self.spielfeldArr[reihe][charNr]:
                #print(strArr[countLine][countChar], end="")
                tempObj = None
                tempPun = False
                tempPow = False
                tempArea = None
                tempWall = False
                if(char=="W"):
                    tempArea = pygame.Rect(countLine*self.feldGroesse, countChar*self.feldGroesse, self.feldGroesse, self.feldGroesse)
                    tempWall = True
                if(char=="M"):
                    tempPun=True
                    tempArea = pygame.Rect(countLine*self.feldGroesse, countChar*self.feldGroesse, self.feldGroesse, self.feldGroesse)
                if(char=="P"):
                    tempPow=True
                    tempArea = pygame.Rect(countLine*self.feldGroesse, countChar*self.feldGroesse, self.feldGroesse, self.feldGroesse)
                if(char=="E"):
                    tempArea = pygame.Rect(countLine*self.feldGroesse, countChar*self.feldGroesse, self.feldGroesse, self.feldGroesse)
                self.spielfeldArr[countLine][countChar] = Feld.Feld(tempObj, tempPun, tempPow, tempArea, tempWall)
                countChar +=1
            countChar =0
            countLine +=1


    def drawSpielfeld(self, fenster):
        pygame.display.set_caption("Kawaiiman")
        fenster.fill((0, 110, 110))
        for y in self.spielfeldArr:
            for x in y:
                pygame.draw.rect(fenster, (100,0,0), x.area)
                print(type(x)) #Kein Output!!! !!! !!! !!! !!!
        pygame.display.update()
"""
Spielfeld
	Array von Feldern 19x22
	Hintergrund Sprite
	Rectangle für Spielfeld
	Rectangle für Score
	pygame.window
"""