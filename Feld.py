import pygame

class Feld:
    object = None
    punktBool = False
    powerUpBool = False
    area = None
    wall = False
    def __init__(self, obj, pun, pow, area, wall):
        self.object = obj
        self.punktBool = pun
        self.powerUpBool = pow
        self.area = area
        self.wall = wall

"""
Feld
	Object -> Pacman und Geister
	Punktbool
	PowerUpBool
	Rectangle
"""