class Spielfeld:
    feldGroesse = 20
    spielfeldArr = [[""] * 19] * 22

    def __init__(self, strArr):
        countLine = 0
        countChar = 0
        for reihe in self.spielfeldArr:
            for char in reihe: # self.spielfeldArr[reihe][charNr]:
                print(strArr[countLine][countChar], end="")
                countChar +=1
            print()
            countChar =0
            countLine +=1

    # über CSV Spielfeld

"""
Spielfeld
	Array von Feldern 19x22
	Hintergrund Sprite
	Rectangle für Spielfeld
	Rectangle für Score
	pygame.window
"""