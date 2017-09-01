"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""

import pygame, sys
from pygame.locals import *

from constantes import *
from classes import *
from fonctions import *

pygame.init()

# set up fenetre
fenetre = pygame.display.set_mode((cote_fenetre, (cote_fenetre + 30)))
# icone
icone = pygame.image.load(img_icone)
pygame.display.set_icon(icone)
# titre
pygame.display.set_caption(titre_fenetre)

# chargement des fonds
accueil = pygame.image.load(img_accueil)
fond = pygame.image.load(img_fond)

pygame.key.set_repeat(200,150)
# boucle principale
while True:
    
    choix = ' '
    pygame.display.flip()
    
    # boucle de menu
    while True:
        pygame.time.Clock().tick(30)
        # INPUT
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_F1:
                    choix = '1'
                elif event.key == K_F2:
                    choix = '2'
                elif event.key == K_F3:
                    choix = '3'
        # UPDATE
        if choix != ' ':
            nom = "niveaux/n" + choix + ".txt"
            niv = Niveau(nom)
            niv.genere()

            temps, score = 0.0, 0
            
            dk = Perso(img_dkd, img_dkg, img_dkh, img_dkb, niv)
            break

        # DISPLAY
        fenetre.blit(accueil, (0,0))
        pygame.draw.line(fenetre, WHITE,(0,cote_fenetre),(cote_fenetre,cote_fenetre))
        pygame.display.flip()

    # boucle de jeu
    while True:
        pygame.time.Clock().tick(30)
        temps += 1/30
        deplacement, menu = ' ', False
        # INPUT
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu = True
                if event.key == K_RIGHT:
                    deplacement = 'droite'
                elif event.key == K_LEFT:
                    deplacement = 'gauche'
                elif event.key == K_UP:
                    deplacement = 'haut'
                elif event.key == K_DOWN:
                    deplacement = 'bas'
           
        # UPDATE
        dk.move(deplacement)
        score = dk.mange(niv, score) # what he does if eat
        if dk.gagne() or menu:
            affiche_point(score, temps, fenetre)
            break
        # DISPLAY
        fenetre.fill(BLACK)
        fenetre.blit(fond, (0,0))
        niv.affiche(fenetre)
        dk.affiche(fenetre)
        affiche_temps(temps, fenetre)
        affiche_score(score, fenetre)
        pygame.display.flip()

        
