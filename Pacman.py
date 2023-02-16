import pygame
import Spielfeld
import time as t
from main import *

class Pacman:
    
	sprite = None
	bewegungsRichtung = None
	bildPacMan = pygame.image.load("assets/PacMan.png")
	frame = 0
	feldGroesse = 30
	xFeld = 9
	yFeld = 16

	def __init__ (self):
		self.bewegungsRichtung = "links"

	@staticmethod # Nochmal überarbeiten, denn mal sage ich es ist static, aber in der main.py übergebe ich dann ein Objekt.
	def drawPacman(fenster, Pacman):
		bildBereiche = ["", "", ""] #, "", "", "", "", "", "", "", "", ""
		bildBereiche[0] = (0 ,0, 30,30 )
		bildBereiche[1] = (31,0, 30,30 )
		bildBereiche[2] = (61,0, 30,30 )
		#bildBereiche[3] = (136,0, 45,45 )
		#bildBereiche[4] = (181,0, 45,45 )
		#bildBereiche[5] = (226,0, 45,45 )
		#bildBereiche[6] = (271,0, 45,45 )
		#bildBereiche[7] = (316,0, 45,45 )
		#bildBereiche[8] = (361,0, 45,45 )
		#bildBereiche[9] = (406,0, 45,45 )
		#bildBereiche[10] = (451,0, 45,45 )
		#bildBereiche[11] = (496,0, 45,45 )
		
		Pacman.frame += 1

		if Pacman.frame > 2: # 11:
			Pacman.frame = 0
		position = (Pacman.xFeld * (Pacman.feldGroesse + 2), Pacman.yFeld * (Pacman.feldGroesse + 2))
		fenster.blit(Pacman.bildPacMan, position, bildBereiche[Pacman.frame])
		# t.sleep(0.2)
# (0,0, 45,45 )
"""
Pacman
	Sprite
	Bewegungsrichtung
	Startpunkt
	Rectangle
"""