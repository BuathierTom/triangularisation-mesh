# mesh-triangularisation

TP sur la triangularisation et le maillage fait avec python.

## Sujet du TP

Juste ici : [Sujet du TP](https://github.com/BuathierTom/mesh-triangularisation/wiki/Sujet-TP)

## Installation

Installation dépendences :

```bash
pip install -r requirements.txt
```

## CheckList

- [x] Tache 1 : Class Sommet, Face, Maillage // Méthode permettant de construire un maillage.
- [x] Tache 2 : Méthode permettant de sauver le maillage dans un fichier au format PLY.
- [x] Tache 3 : Méthode qui calcule la surface de l’objet.
- [x] Tache 4 : Méthode permettant d’inverser les normales des faces du maillage triangulaire.
- [x] Tache 5 : Méthode permettant de centrer le maillage.
- [x] Tache 6 : Méthode permettant de faire une homotéthie du maillage.
- [x] Tache 7 : Méthode pour bruiter le maillage.
- [ ] Tache 8 : Méthode permettant de sauvegarder le maillage dans un fichier au format STL puis au format COLLADA.
- [ ] Tache 9 : Méthode permettant de vérifier que toutes les arêtes partagent exactement deux faces.
- [ ] Tache 10 : Méthode permettant de faire la subdivision de Loop.

## Utilisation

Pour chaque tâche il y a une fonction qui permet de tester la fonctionnalité en détails que ce soit en créant un fichier et en montrant aussi le détail des sommets. Tous les fichiers sauvegardés sont mis dans le dossier `src/tests/`.

Pour tester, il vous suffira d'aller dans le fichier `main.py` et de commenter et décommenter les lignes qui vous intéresse pour tester.

Pour plus de détails : 
- Le fichier `maillage.py` contient une classe **Maillage** qui a toutes les méthodes pour le TP.
- Le fichier `sommet.py` contient une classe **Sommet** avec les méthodes pour translater et faire l'homothétie.
- Le fichier `face.py` contient une classe **Face** avec une représentation des faces.
- Le fichier `vecteur3D.py` contient une classe **Vecteur3D** avec les méthodes pour la surface de l’objet.

## Auteur

- [@BuathierTom](https://www.github.com/BuathierTom)