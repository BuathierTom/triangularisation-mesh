# class imports 
from src.maillage import Maillage
# other imports
import os

# Path: main.py

# Chemin vers les fichiers de tests
dict_path = {
    0: "./src/assets/00_test.ply",
    1: "./src/assets/01_cube.ply",
    2: "./src/assets/02_cube_3x3.ply",
    3: "./src/assets/03_moomoo.ply",
    4: "./src/assets/04_heptoroid.ply",
    5: "./src/assets/05_bunny.ply",
}


# On construit le maillage
maillage = Maillage(dict_path[5])

# on supprime le fichier s'il existe deja
if os.path.exists("./src/tests/SaveFile.ply"):
    os.remove("./src/tests/SaveFile.ply")

maillage.sauvegarderMaillage("./src/tests/SaveFile.ply")
