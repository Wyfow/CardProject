"""
Fichier principal du jeu

Contenu: jeuDeCarte.py, constantes.py, classes_jeu.py, classes_cartes.py, fonctions.py
"""

import pygame, sys
##import # autres library

from pygame.locals import *
from constantes import *
from classes_jeu import *
from fonctions import *

pygame.init()

# Declarations des variables necessaire
# set up window
fenetre = pygame.display.set_mode((larg_fenetre, haut_fenetre))
pygame.display.set_caption(titre_fenetre)
##pygame.display.set_icon(icone_fenetre)



# GAME LOOP
while True:
    # INPUT
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            pass
        if event.type == KEYUP:
            pass

    # UPDATE


    # DISPLAY
    pygame.display.flip() # met a jour l'image
