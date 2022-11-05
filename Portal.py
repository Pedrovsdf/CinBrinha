import pygame
import random
import Variaveis as v


# Classe do portal
class Portal(object):
    # Definindo as informações principais do portal
    def __init__(self):
        self.posicao = (300, 300)
        self.color = v.azul

    # Desenhar a comida
    def desenhar(self, superficie):
        portal = pygame.image.load('img\portal.png').convert_alpha()
        retangulo = pygame.Rect((self.posicao[0], self.posicao[1]), (v.tamanho_rede, v.tamanho_rede))
        superficie.blit(portal,retangulo)