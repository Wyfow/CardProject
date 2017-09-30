"""
Fichier contenant les classes relatives au plateau de jeu

Classe: Plateau
"""

import pygame
from pygame.locals import*
from constantes import*
from fonctions import*

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
        self.map.genere()
        
        self.commande = Commandes()

    def show(self, fenetre):
        """ Affiche """
        self.map.show(fenetre)
        self.commande.show(fenetre)

class Map():
    """
    classe map incluse dans PlayScreen
    """
    def __init__(self):
        """ """
        self.structure = 0;

    def genere(self):
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

    def show(self, fenetre):
        """ Affiche le plan selon sa structure """
##        for lig in range(50):
##            for col in range(50):
##                print(self.structure[lig][col], end='')
##            print("");
        pygame.draw.rect(fenetre, RED, (0,0,800,800))

class Commandes():
    """
    Rectangles des options
    """
    def __init__(self):
        """ Constructeur """
        self.zone = pygame.Rect(0, 0, 200, haut_fenetre)
        self.zone.right = larg_fenetre

        self.etat = 1 # 0,1,2: Choisir perso, Choisir Option, 

        self.titre = set_titre()
        self.button_personnages = set_list_perso()
        self.button_attaquer = set_button('Attaquer', 3)
        self.button_deplacer = set_button('Deplacer', 1)
        self.button_capacite = set_button('Capacité', 2)
                                          
    def show(self, fenetre):
        """ """
        pygame.draw.rect(fenetre, BLACK, self.zone)
        # titre de la fenetre: present dans chaque etat
        pygame.draw.line(fenetre, WHITE, (larg_fenetre-200, 100), (larg_fenetre, 100), 5)
        fenetre.blit(self.titre[0], self.titre[1])

        if(self.etat == 0):
            pass
        elif(self.etat == 1):
            pygame.draw.rect(fenetre, WHITE, self.button_deplacer[2], 2)
            pygame.draw.rect(fenetre, WHITE, self.button_capacite[2], 2)
            pygame.draw.rect(fenetre, WHITE, self.button_attaquer[2], 2)

            fenetre.blit(self.button_deplacer[0], self.button_deplacer[1])
            fenetre.blit(self.button_capacite[0], self.button_capacite[1])
            fenetre.blit(self.button_attaquer[0], self.button_attaquer[1])

        elif(self.etat == 2):
            pass

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


