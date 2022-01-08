# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 14:12:19 2022

@author: Fernando
"""

#Empezamos el juego abriendo una ventana vacia en pygame. Luego dibujaremos los
#elementos del juego, como las nves y los extraterrestres. También haremos que 
#nuestro juego responda a entrada de usuario, configuraremos el color de fondo 
#y cargaremos una imagen de una nave

################################################################
#Crear una ventana en pygame y resònder a entrada de usuario
################################################################
#Haremos una ventana en pygame ccreando una clase que represente el juego

import sys
import pygame  #Contiene la funcionalidad que se necesita para hacer el juego

class AlienInvasion:
   """Clase general para gestionar los recursos y el comportamiento del juego."""
   
   def __init__(self):
       """Inicializa el juego y crea recursos."""
       
       pygame.init() #Inicializa la configuración de fondo que necesita Pygame
       self.screen = pygame.display.set_mode((1200, 800)) # Creamos la ventana
       pygame.display.set_caption("Alien Invasion")
       
       #Configuramos el color de fondo
       self.bg_color = (230, 230, 230)
       
   def run_game(self):
        """Inicializa el bucle principal para el juego."""
        
        while True:
            #Busca eventos de teclado y ratón
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Redibuja la pantalla en cada paso por el bucle.
            self.screen.fill(self.bg_color)
            
            #Hace visible la última pantalla dibujada
            pygame.display.flip()

if __name__ == '__main__':
    #hace una instancia del juego y lo ejecuta.
    ai = AlienInvasion()
    ai.run_game()
