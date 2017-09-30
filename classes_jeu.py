"""
Fichier contenant les classes relatives au plateau de jeu

Classe: Plateau
"""

###############################################################
####                    Ecran d'accueil
###############################################################

class StartScreen():
    """
    classe de l'écran d'accueil / ouverture
    - Titre;
    - Slogan ou courte introduction
    - Menu d'option pré jeu
    - Explication : le jeu, les règles, les auteurs ...
    """

    def __init__(self):
        """ Constucteur de la classe """


    def show(self):
        """ Méthode pour afficher la classe """

###############################################################
####                    Ecran de jeu
###############################################################

class PlayScreen():
    """
    classe de l'ecran de jeu
    """

    def __init__(self):
        """ Constructeur de la classe """
        self.map = Map()
        self.map.set()

    def show(self):
        """ Affiche """
        self.map.show()

class Map():
    """
    classe map incluse dans PlayScreen
    """
    def __init__(self):
        """ """
        self.structure = 0;

    def set(self):
        """ Genere la map """
        with open("map_basic.txt", 'r') as fichier:
            structure_map = []
            for ligne in fichier:
                ligne_map = []
                for char in ligne:
                    if char != '\n':
                        ligne_map.append(char)
                structure_map.append(ligne_map)
            self.structure = structure_map

    def show(self):
        """ Affiche le plan selon sa structure """
        for lig in range(50):
            for col in range(50):
                print(self.structure[lig][col], end='')
            print("");

###############################################################
####                    Ecran de fin
###############################################################

class EndScreen():
    """
    classe de l'écran de fin de jeu
    - Résultat / score de la partie
    - Meilleur score si battu
    - Bonus / Malus sur le niveau du joueur
    - Menu de retour au jeu, quitter jeu,
    """

    def __init__(self):
        """ Constucteur de la classe """


    def show(self):
        """ Méthode pour afficher la classe """


