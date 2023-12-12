class Vecteur3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norme(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def produit_vectoriel(self, autre_vecteur):
        x = self.y * autre_vecteur.z - self.z * autre_vecteur.y
        y = self.z * autre_vecteur.x - self.x * autre_vecteur.z
        z = self.x * autre_vecteur.y - self.y * autre_vecteur.x
        return Vecteur3D(x, y, z)