"""
Fichier des fonctions pour le jeu
"""

import pygame
from pygame.locals import*
from constantes import*

def set_titre():
    """ """
    font_titre = pygame.font.Font('freesansbold.ttf', 30)
    surf_titre = font_titre.render(text_titre, True, WHITE)
    rect_titre = surf_titre.get_rect()
    rect_titre.center = (larg_fenetre-100, 50)

    return (surf_titre, rect_titre)

def set_list_perso():
    """ """
    ## TODO: creer une list des personnages avant
    pass

def set_button(text, ordre):
    """ """
    font_button = pygame.font.Font('freesansbold.ttf', 20)
    surf_button = font_button.render(text, True, WHITE)
    rect_button = surf_button.get_rect()
    rect_button.center = (larg_fenetre-100, (haut_fenetre/2)+100*(ordre-2))

    cadre = pygame.Rect(0, 0, 200, 100)
    cadre.center = (larg_fenetre-100, haut_fenetre/2 + 100*(ordre-2))

    return (surf_button, rect_button, cadre)

