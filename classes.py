"""
Fichier des classes

Contient les classe:
Niveau qui gere le niveau
Perso qui gere le perso
"""

import pygame

from pygame.locals import *
from constantes import *

# classe niveau
class Niveau:
    """ classe niveau """
    def __init__(self, fichier):
        """ Constucteur """
        self.fichier = fichier
        self.structure = 0

    def genere(self):
        """ Genere le plan a partir du fichier """
        with open(self.fichier, 'r') as fichier:
            structure_niv = []
            # pour chaque ligne du fichier
            for ligne in fichier:
                ligne_niv = []
                # pour chaque caractere de la ligne
                for char in ligne:
                    # si ce n'est pas un '\n'
                    if char != '\n':
                        ligne_niv.append(char)
                #on ajoute la ligne a la structure
                structure_niv.append(ligne_niv)
            # on sauvegarde la structure dans l'objet
            self.structure = structure_niv

    def affiche(self, fenetre):
        """ Affiche le plan selon sa structure """
        # load des images
        mur = pygame.image.load(img_mur).convert()
        depart = pygame.image.load(img_depart).convert()
        arrivee = pygame.image.load(img_arrivee).convert()
        fruits = pygame.image.load(img_fruits).convert_alpha()
        
        for lig in range(nombre_case):
            for col in range(nombre_case):
                # calcul de la position
                pos_x = col * taille_case
                pos_y = lig * taille_case
                # test de l'img a afficher
                if self.structure[lig][col] == 'a':
                    fenetre.blit(arrivee, (pos_x,pos_y))
                elif self.structure[lig][col] == 'b':
                    fenetre.blit(fruits, (pos_x,pos_y))
                elif self.structure[lig][col] == 'd':
                    fenetre.blit(depart, (pos_x,pos_y))
                elif self.structure[lig][col] == 'm':
                    fenetre.blit(mur, (pos_x,pos_y))
                    

# classe personnage
class Perso:
    """ Classe personnage """
    def __init__(self, img_d, img_g, img_h, img_b, niveau):
        """ Constructeur """
        # images
        self.img_d = pygame.image.load(img_d).convert_alpha()
        self.img_g = pygame.image.load(img_g).convert_alpha()
        self.img_b = pygame.image.load(img_h).convert_alpha()
        self.img_h = pygame.image.load(img_b).convert_alpha()
        # position
        self.cur_img = self.img_d
        self.pos_x = 0
        self.pos_y = 0
        self.pixel_x = 0
        self.pixel_y = 0
        # niveau dans lequel il se trouve
        self.niveau = niveau

    def move(self, deplacement):
        """ deplace le singe """
        if deplacement == 'droite':
            self.cur_img = self.img_d
            if self.pos_x < (nombre_case - 1):
                if self.niveau.structure[self.pos_y][self.pos_x+1] != 'm':
                    self.pos_x += 1
                    self.pixel_x = self.pos_x * taille_case
        elif deplacement == 'gauche':
            self.cur_img = self.img_g
            if self.pos_x > 0:
                if self.niveau.structure[self.pos_y][self.pos_x-1] != 'm':
                    self.pos_x -= 1
                    self.pixel_x = self.pos_x * taille_case
        elif deplacement == 'haut':
            self.cur_img = self.img_h
            if self.pos_y > 0 :
                if self.niveau.structure[self.pos_y-1][self.pos_x] != 'm':
                    self.pos_y -= 1
                    self.pixel_y = self.pos_y * taille_case
        elif deplacement == 'bas':
            self.cur_img = self.img_b
            if self.pos_y < (nombre_case - 1):
                if self.niveau.structure[self.pos_y+1][self.pos_x] != 'm':
                    self.pos_y += 1
                    self.pixel_y = self.pos_y * taille_case

    def mange(self, niveau, score):
        """ """
        if niveau.structure[self.pos_y][self.pos_x] == 'b':
            score += 10
            niveau.structure[self.pos_y][self.pos_x] = '0'
            self.niveau = niveau
        return score
        
    def affiche(self, fenetre):
        """ affiche le singe """
        fenetre.blit(self.cur_img, (self.pixel_x, self.pixel_y))

    def gagne(self):
        """ Check if has reached the bananas """
        if self.niveau.structure[self.pos_y][self.pos_x] == 'a':
            return True
        else:
            return False
            
    









