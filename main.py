# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 13:31:18 2023

@author: rira2
"""
import tkinter
import pygame
from pygame.locals import *
import os

# ===== Variables globales ======================

# Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1

nPosX = 390 # Position en X du personnage
nPosY = 510 # Position en Y du personnage
nDirX = 0   # Sens de déplacement du personnage selon X. 0 => il ne bougle pas
nDirY = 0   # Sens de déplacement du personnage selon Y. 0 => il ne bougle pas


# Pour positionner la fenêtre Pygame.
#os.environ['SDL_VIDEO_WINDOW_POS'] = '20,100'
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (120, 200)

# Information sur le display
# https://www.pygame.org/docs/ref/display.html

# Initialisation des modules de Pygame
pygame.init()

# Création d'une fenêtre graphique de Pygame
##fenetre = pygame.display.set_mode((640, 480))

# Permet de rendre la fenêtre de taille ajustable.
fenetre = pygame.display.set_mode((800,600), RESIZABLE)

# Une image pour le fond de la fenêtre
fond = pygame.image.load("C:/Users/Achraf LADHARI/Desktop/tfach2/proj sem/assets/MainScreen/re9ed.png").convert() 


# Ne fonctionne pas !???
#perso1.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent

# Affiche l'image dans la fenêtre
fenetre.blit(fond, (0, 0))

# Affiche le personnage au-dessus de l'herbe

# Actualise la fenêtre
pygame.display.flip()

# Pour avoir un autorepeat si une touche est pressée.
pygame.key.set_repeat(10, 3) # répétition de la touche toutes les ... [ms]

# Pour définir une vitesse d'exécution,
# en limitant en attendant qu'un certain temps se soit écoulé avant de continuer.
myClock = pygame.time.Clock()
#pos button X
lX=[]
for i in range (370,431):
    lX.append(i)
#button posY 
lY=[]
for i in range (497,546):
    lY.append(i)
# ================================================
# Boucle principale
while continuer:

    # Boucle sur tous les événements gérés par Pygame
    for event in pygame.event.get():        
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            # La fenêtre a été fermée ou La touche ESC a été pressée.
            continuer = 0 # Indique de sortir de la boucle.
        
        if event.type == MOUSEBUTTONDOWN and event.pos[0] in lX and  event.pos[1] in lY : # Un bouton de la souris pressé
            if event.button == 1:
                import achraf_ye7lem
                achraf_ye7lem.main(fenetre)

               
            
    
    # Affiche le fond
    fenetre.blit(fond, (0, 0)) # pour laisser les autres objets se dessiner par dessus le fond
    

    # Déplacement de tous les projectiles
    # Affiche les projectiles par dessus ce qui prédèce
    # Il faut parcourir la liste depuis la fin, car len(glaProjectiles) peut changer dans la boucle.

    # Actualise la fenêtre
    pygame.display.flip()

    # Limitation de la vitesse à ... images par seconde
    # 100 => attend que 1000 / 100 [ms] se soit écoulé depuis le dernier appel,
    # avant de continuer.
    # 100 => limite à 100 images par secondes, soit 100 exécutions de la boucle par seconde
    myClock.tick(200) # c.f. https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
  
pygame.display.quit() # ferme la fenêtre, c.f. https://www.pygame.org/docs/ref/display.html
pygame.quit() # quitte pygame, c.f. https://www.pygame.org/docs/ref/pygame.html
