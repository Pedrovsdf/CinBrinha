import pygame
import sys
import random

import Variaveis as v


class Inimigo(object):
    # Definindo as informações principais da comida
    def __init__(self, movel):
        self.posicao = (0, 0)
        
        if movel == True: 
            self.color = v.roxo
        else:
            self.color = v.preto
        self.aleatorizar_posicao()
        self.movel = movel

    # Aleatorizar a posição da comida
    def aleatorizar_posicao(self):
        self.posicao = ((random.randint(0, int(v.largura_rede) - 1) * v.tamanho_rede),
                        (random.randint(0, int(v.altura_rede) - 1) * v.tamanho_rede))

    # Desenhar a comida
    def desenhar(self, superficie):
        retangulo = pygame.Rect((self.posicao[0], self.posicao[1]), (v.tamanho_rede, v.tamanho_rede))
        pygame.draw.rect(superficie, self.color, retangulo)
        pygame.draw.rect(superficie, v.preto, retangulo, 1)

    def comando(self, direcao):
        x, y = direcao
        novo = (((self.posicao[0] + (v.tamanho_rede)) % v.largura), (self.posicao[1] + (y * v.tamanho_rede)) % v.altura
        self.posicao = novo