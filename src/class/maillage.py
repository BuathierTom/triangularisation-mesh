import numpy as np
from plyfile import PlyData, PlyElement

# Import Sommet
from sommet import Sommet
# Import Face
from face import Face
        
class Maillage:
    def __init__(self, fichier_ply):
        self.sommets = []
        self.faces = []
        self.construire_maillage(fichier_ply)

    def ajouter_sommet(self, x, y, z):
        sommet = Sommet(x, y, z)
        self.sommets.append(sommet)
        return sommet

    def construire_maillage(self, fichier_ply):
        
        nb_sommets = 0
        nb_faces = 0
        
        with open(fichier_ply, 'r') as file:
            lines = file.readlines()

            for line in lines:
                if line.startswith("element vertex"):
                    nb_sommets = int(line.split()[2])
                elif line.startswith("element face"):
                    nb_faces = int(line.split()[2])
                elif line.startswith("end_header"):
                    break
                
                
            print("nb_sommets = ", nb_sommets)
            print("nb_faces = ", nb_faces)
            
            for i in range(nb_sommets):
                x, y, z = lines[i+12].split()[:3]
                self.ajouter_sommet(float(x), float(y), float(z))
                
            for i in range(nb_faces):
                s1, s2, s3 = lines[i+12+nb_sommets].split()[1:]
                self.faces.append(Face(self.sommets[int(s1)], self.sommets[int(s2)], self.sommets[int(s3)]))

            



        
        

# Exemple d'utilisation
maillage = Maillage("./src/assets/01_cube.ply")


        