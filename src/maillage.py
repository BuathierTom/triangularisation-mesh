import numpy as np
from plyfile import PlyData, PlyElement
import os

# Import Sommet
from sommet import Sommet
# Import Face
from face import Face
# Import Vecteur3D
from vecteur3D import Vecteur3D
        
class Maillage:
    def __init__(self, fichier_ply):
        self.sommets = []
        self.faces = []
        self.construireMaillage(fichier_ply)

    def ajouterSommet(self, x, y, z):
        sommet = Sommet(x, y, z)
        self.sommets.append(sommet)
        return sommet

    def ajouterFace(self, s1, s2, s3):
        face = Face(s1, s2, s3)
        self.faces.append(face)
        return face
    
    def getSommets(self):
        return self.sommets
    
    def getFaces(self):
        return self.faces
    
    ### CONSTRUCTION MAILLAGE ###
    
    def construireMaillage(self, fichier_ply):
        plydata = PlyData.read(fichier_ply)

        # Accéder aux données des sommets
        for i, sommet_data in enumerate(plydata['vertex'].data):
            x, y, z = sommet_data[0], sommet_data[1], sommet_data[2]
            # print(f"Sommet {i} : ({x}, {y}, {z})")
            self.ajouterSommet(x, y, z)

        # Accéder aux données des faces
        for i, face_data in enumerate(plydata['face'].data):
            
            # on enleve l'array
            face_data = face_data.tolist()
            face_data = face_data[0]          
              
            s1, s2, s3 = face_data[0], face_data[1], face_data[2]
            self.ajouterFace(s1, s2, s3)
        
        print("Maillage construit !")
        
    ### SAUVEGARDE DU MAILLAGE ###

    def sauvegarderMaillage(self, fichier_ply_sauvegarde):
        
        vertex = np.array([(sommet.x, sommet.y, sommet.z) for sommet in self.sommets], 
                          dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4')])
        
        
        faces = np.array([(face.sommets[0], face.sommets[1], face.sommets[2]) for face in self.faces],
                         dtype=[('s1', 'f4'), ('s2', 'f4'), ('s3', 'f4')])
        
        
        # On crée le fichier ply avec un open
        with open(fichier_ply_sauvegarde, 'w') as file:
            # Écriture de l'en-tête
            file.write("ply\n")
            file.write("format ascii 1.0\n")
            file.write("comment zipper output\n")
            file.write("element vertex {}\n".format(len(self.sommets)))
            file.write("property float x\n")
            file.write("property float y\n")
            file.write("property float z\n")
            file.write("element face {}\n".format(len(self.faces)))
            file.write("property list uchar int vertex_indices\n")
            file.write("end_header\n")
            
            # Écriture des sommets
            for v in vertex:
                file.write("{} {} {}\n".format(v[0], v[1], v[2]))
                
            # Écriture des faces
            for f in faces:
                file.write("3 {} {} {}\n".format(int(f[0]), int(f[1]), int(f[2])))
            
        print("Maillage sauvegardé !")
    
    ### INVERSER NORMALES ###
    
    def inverserNormales(self):
        for face in self.faces:
            # Inverser l'ordre des sommets
            face.sommets = [face.sommets[0], face.sommets[2], face.sommets[1]]

        print("Normales inversées !")

    ### CENTRER MAILLAGE ###
    
    def trouverExtremites(self):
        min_x = min_y = min_z = float('inf')
        max_x = max_y = max_z = float('-inf')

        for sommet in self.sommets:
            min_x = min(min_x, sommet.x)
            min_y = min(min_y, sommet.y)
            min_z = min(min_z, sommet.z)
            max_x = max(max_x, sommet.x)
            max_y = max(max_y, sommet.y)
            max_z = max(max_z, sommet.z)

        return min_x, min_y, min_z, max_x, max_y, max_z

    def calculerVecteurTranslation(self, min_x, min_y, min_z, max_x, max_y, max_z):
        centre_x = (min_x + max_x) / 2
        centre_y = (min_y + max_y) / 2
        centre_z = (min_z + max_z) / 2

        translation_x = -centre_x
        translation_y = -centre_y
        translation_z = -centre_z
        
        print(f"Centre : ({centre_x}, {centre_y}, {centre_z})")
        print(f"Translation : ({translation_x}, {translation_y}, {translation_z})")

        return translation_x, translation_y, translation_z

    def translater(self, translation_x, translation_y, translation_z):
        for sommet in self.sommets:
            sommet.translater(translation_x, translation_y, translation_z)

    def centrerMaillage(self):
        min_x, min_y, min_z, max_x, max_y, max_z = self.trouverExtremites()
        translation_x, translation_y, translation_z = self.calculerVecteurTranslation(min_x, min_y, min_z, max_x, max_y, max_z)

        self.translater(translation_x, translation_y, translation_z)

        print("Maillage centré !")

    ### HOMOTETHIE MAILLAGE ###
    
    def homothetie(self, facteur_echelle):
        for sommet in self.sommets:
            sommet.homothetie(facteur_echelle)
            
        print("Maillage homothétisé !")
        
    ### BRUITAGE MAILLAGE ###
    
    def bruitage(self, coefficient_bruit):
        for sommet in self.sommets:
            bruit_x = np.random.uniform(-coefficient_bruit, coefficient_bruit)
            bruit_y = np.random.uniform(-coefficient_bruit, coefficient_bruit)
            bruit_z = np.random.uniform(-coefficient_bruit, coefficient_bruit)

            sommet.x += bruit_x
            sommet.y += bruit_y
            sommet.z += bruit_z
            
        print("Maillage bruité !")

### TESTS ###

def testInversionNormales():
    
    maillage = Maillage("./src/assets/01_cube.ply")
    print("Avant l'inversion des normales :")
    print("Faces du maillage :")
    for i, face in enumerate(maillage.faces):
        print(f"Face {i + 1}: {face.sommets}")

    maillage.inverserNormales()

    print("\nAprès l'inversion des normales :")
    print("Faces du maillage :")
    for i, face in enumerate(maillage.faces):
        print(f"Face {i + 1}: {face.sommets}")

# print("Test d'inversion des normales :")
# testInversionNormales()

def testCentrageMaillage():
    # test fait sur un fichier sans trop de sommets
    maillage = Maillage("./src/assets/01_cube.ply")
    print("Avant le centrage du maillage :")
    print("Coordonnées des sommets :")
    for sommet in maillage.sommets:
        print(f"Sommet : ({sommet.x}, {sommet.y}, {sommet.z})")

    maillage.centrerMaillage()

    print("\nAprès le centrage du maillage :")
    print("Coordonnées des sommets :")
    for sommet in maillage.sommets:
        print(f"Sommet : ({sommet.x}, {sommet.y}, {sommet.z})")

# print("Test de centrage du maillage :")
# testCentrageMaillage()

def testHomothetieMaillage():

    maillage = Maillage("./src/assets/01_cube.ply")
    print("Avant l'homothétie :")
    print("Coordonnées des sommets :")
    for sommet in maillage.sommets:
        print(f"Sommet : ({sommet.x}, {sommet.y}, {sommet.z})")

    facteur_echelle = 10.0 
    maillage.homothetie(facteur_echelle)

    print("\nAprès l'homothétie :")
    print("Coordonnées des sommets :")
    for sommet in maillage.sommets:
        print(f"Sommet : ({sommet.x}, {sommet.y}, {sommet.z})")
        
    maillage.sauvegarderMaillage("homothetie.ply")        
# print("Test d'homothétie du maillage :")
testHomothetieMaillage()

def testBruitageMaillage():

    maillage = Maillage("./src/assets/03_moomoo.ply")
    print("Avant le bruitage :")
    print("Coordonnées des sommets :")
    for sommet in maillage.sommets:
        print(f"Sommet : ({sommet.x}, {sommet.y}, {sommet.z})")

    coefficient_bruit = 5 
    maillage.bruitage(coefficient_bruit)

    print("\nAprès le bruitage :")
    print("Coordonnées des sommets :")
    for sommet in maillage.sommets:
        print(f"Sommet : ({sommet.x}, {sommet.y}, {sommet.z})")
        
    maillage.sauvegarderMaillage("bruite.ply") 
    
# print("Test de bruitage du maillage :")
# testBruitageMaillage()