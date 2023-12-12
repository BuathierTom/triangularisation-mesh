# class imports 
from src.maillage import Maillage
from src.tests import TestsMaillages
# other imports
import os

# !!! AVANT UTILISATION DU CODE : LIRE README.md !!!

# Chemin vers les fichiers de tests
dict_path = {
    0: "./src/assets/00_test.ply",
    1: "./src/assets/01_cube.ply",
    2: "./src/assets/02_cube_3x3.ply",
    3: "./src/assets/03_moomoo.ply",
    4: "./src/assets/04_heptoroid.ply",
    5: "./src/assets/05_bunny.ply",
}

# Choix du fichier de test
maillage = TestsMaillages(dict_path[5])

# ---------------------------------------------------------------------------------------- #

# 1ère & 2ème question : test de la création d'un maillage avec la sauvegarde du fichier

maillage.testCreationMaillage()

# ---------------------------------------------------------------------------------------- #

# 3ème question : 

# maillage.testCalculSurface()

# ---------------------------------------------------------------------------------------- #

# 4ème question : test de l'inversion des normales
# !!! Pour aucune surcharge dans le terminal, prennez un fichier avec peu de sommets

# maillage.testInversionNormales()

# ---------------------------------------------------------------------------------------- #

# 5ème question : test du centrage du maillage
# !!! Pour aucune surcharge dans le terminal, prennez un fichier avec peu de sommets

# maillage.testCentrageMaillage()

# ---------------------------------------------------------------------------------------- #

# 6ème question : test de l'homothétie du maillage
# !!! Pour aucune surcharge dans le terminal, prennez un fichier avec peu de sommets

# maillage.testHomothetieMaillage()

# ---------------------------------------------------------------------------------------- #

# 7ème question : test du bruitage

# Valeur du coefficient de bruitage
coefficient_bruit = 0.3

# maillage.testBruitageMaillage(coefficient_bruit)
