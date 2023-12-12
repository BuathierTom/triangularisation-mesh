from src.maillage import Maillage
import os

class TestsMaillages:
    
    def __init__(self, fichier_ply):
        self.maillage = Maillage(fichier_ply)
        
        
    def testCreationMaillage(self):
        """
        Teste la création d'un maillage.
        """
        # on supprime le fichier s'il existe deja
        if os.path.exists("./src/tests/saveMaillage.ply"):
            os.remove("./src/tests/saveMaillage.ply")
            
        self.maillage.sauvegarderMaillage("./src/tests/saveMaillage.ply")
        
    def testCalculSurface(self):
        """
        Teste le calcul de la surface d'un maillage.
        """
        aire = self.maillage.calculerSurface()
        print(f"Aire du maillage : {aire}")
    

    def testInversionNormales(self):
        """
        Teste l'inversion des normales d'un maillage.
        """
        
        print("Avant l'inversion des normales :")
        print("Faces du maillage :")
        for i, face in enumerate(self.maillage.faces):
            print(f"Face {i + 1}: {face.sommets}")

        self.maillage.inverserNormales()

        print("\nAprès l'inversion des normales :")
        print("Faces du maillage :")
        for i, face in enumerate(self.maillage.faces):
            print(f"Face {i + 1}: {face.sommets}")

        # on supprime le fichier s'il existe deja
        if os.path.exists("./src/tests/saveInversion.ply"):
            os.remove("./src/tests/saveInversion.ply")
            
        self.maillage.sauvegarderMaillage("./src/tests/saveInversion.ply")

    def testCentrageMaillage(self):
        """
        Teste le centrage d'un maillage.
        """
        # test fait sur un fichier sans trop de sommets
        print("Avant le centrage du maillage :")
        print("Coordonnées des sommets :")
        for sommet in self.maillage.sommets:
            print(f"Sommet : ({sommet.x}, {sommet.y}, {sommet.z})")

        self.maillage.centrerMaillage()

        print("\nAprès le centrage du maillage :")
        print("Coordonnées des sommets :")
        for sommet in self.maillage.sommets:
            print(f"Sommet : ({sommet.x}, {sommet.y}, {sommet.z})")
            
            
        # on supprime le fichier s'il existe deja
        if os.path.exists("./src/tests/saveCentrer.ply"):
            os.remove("./src/tests/saveCentrer.ply")
            
        self.maillage.sauvegarderMaillage("./src/tests/saveCentrer.ply")



    def testHomothetieMaillage(self):
        """
        Teste l'homothétie d'un maillage.
        """

        print("Avant l'homothétie :")
        print("Coordonnées des sommets :")
        for sommet in self.maillage.sommets:
            print(f"Sommet : ({sommet.x}, {sommet.y}, {sommet.z})")

        facteur_echelle = 10.0 
        self.maillage.homothetie(facteur_echelle)

        print("\nAprès l'homothétie :")
        print("Coordonnées des sommets :")
        for sommet in self.maillage.sommets:
            print(f"Sommet : ({sommet.x}, {sommet.y}, {sommet.z})")
            
        # on supprime le fichier s'il existe deja
        if os.path.exists("./src/tests/saveHomothetie.ply"):
            os.remove("./src/tests/saveHomothetie.ply")
            
        self.maillage.sauvegarderMaillage("./src/tests/saveHomothetie.ply")       
        

    def testBruitageMaillage(self, coefficient_bruit):
        """
        Teste le bruitage d'un maillage.

        Args:
            coefficient_bruit (float): coefficient de bruitage
        """

        self.maillage.bruitage(coefficient_bruit)
        
        # on supprime le fichier s'il existe deja
        if os.path.exists("./src/tests/saveBruite.ply"):
            os.remove("./src/tests/saveBruite.ply")
            
        self.maillage.sauvegarderMaillage("./src/tests/saveBruite.ply") 

