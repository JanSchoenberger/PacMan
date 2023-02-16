import pygame

class Geist:
    
	bildPacMan = pygame.image.load("assets/Geist_rot.png") # Hier leer, wird dann im Konsturkutor 
	feldGroesse = 30
	xGeist = 0
	yGeist = 0
	
	frame = 0

	

	def __init__(self, x, y, bildLader):

		self.xGeist = x
		self.yGeist = y
		self.bildLader = bildLader
	
	def drawGeister(self, fenster):
		
		#Geist1 = Geister[0]
		#Geist2 = Geister[1]
		#Geist3 = Geister[2]
		#Geist4 = Geister[3]

		bildBereiche = [""] #, "", "", "", "", "", "", "", "", ""
		
		bildBereiche[0] = (0 ,0,30,30 )

		frame = 0

		position = (self.xGeist * (Geist.feldGroesse + 2), self.yGeist * (Geist.feldGroesse + 2))
		fenster.blit(self.bildLader, position, bildBereiche[Geist.frame])





# Noch die Assests anpassen und wissen welche wann.

"""
Geister
	Sprite
	Bewegungsrichtung
	FressbarBool
	Startpunkt
	Rectangle
"""