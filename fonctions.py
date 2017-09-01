""" fichier de fonction """

import pygame
from pygame.locals import *

from constantes import *
from classes import *

def affiche_temps(temps, fenetre):
    """ Affiche le temps """
    minutes = int(temps / 60)
    secondes = int(temps % 60)
    text_temps = str(minutes)+":"+str(secondes)
    font_temps = pygame.font.Font("freesansbold.ttf", 15)
    surf_temps = font_temps.render(text_temps, True, WHITE)
    rect_temps = surf_temps.get_rect()
    rect_temps.bottomright = ((cote_fenetre - 5),(cote_fenetre + 25))

    fenetre.blit(surf_temps, rect_temps)

def affiche_score(score, fenetre):
    """ Affiche le score """
    text_score = "Score: " + str(score)
    font_score = pygame.font.Font("freesansbold.ttf", 15)
    surf_score = font_score.render(text_score, True, WHITE)
    rect_score = surf_score.get_rect()
    rect_score.bottomleft = (5, (cote_fenetre + 25))

    fenetre.blit(surf_score, rect_score)

def affiche_point(score, temps, fenetre):
    """ """
    point = score - int(temps)
    text_point = "RESULT: " + str(point)
    font_point = pygame.font.Font('freesansbold.ttf', 15)
    surf_point = font_point.render(text_point, True, WHITE)
    rect_point = surf_point.get_rect()
    rect_point.centerx = cote_fenetre / 2
    rect_point.bottom = cote_fenetre + 25

    fenetre.blit(surf_point, rect_point)
