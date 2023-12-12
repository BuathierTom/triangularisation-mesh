class Sommet:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.voisins = []
        
    def setVoisins(self, voisin: list):
        self.voisins.append(voisin)
        
    def getVoisins(self):
        return self.voisins
    
    def translater(self, translation_x, translation_y, translation_z):
        self.x += translation_x
        self.y += translation_y
        self.z += translation_z
        
    def homothetie(self, facteur_echelle):
        self.x *= facteur_echelle
        self.y *= facteur_echelle
        self.z *= facteur_echelle
    
    def __repr__(self):
        return f"Sommet({self.x}, {self.y}, {self.z})"