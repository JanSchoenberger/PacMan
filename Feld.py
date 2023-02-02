import pygame

class Feld:
    object = None
    punktBool = True
    powerUpBool = False
    area = None
    def __init__(self, ob, pu, po, ar):
        Feld.object = ob
        Feld.punktBool = pu
        Feld.powerUpBool = po
        Feld.area = ar

"""
Feld
	Object -> Pacman und Geister
	Punktbool
	PowerUpBool
	Rectangle
"""