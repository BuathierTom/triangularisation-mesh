class Sommet:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.voisins = []
        
    def ajouter_voisin(self, voisin):
        self.voisins.append(voisin)