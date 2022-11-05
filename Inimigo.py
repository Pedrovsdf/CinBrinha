import pygame
import sys
import random

import Variaveis as v
from Cobra import Cobra


class Inimigo(object):
    # Definindo as informações principais do inimigo
    def __init__(self, movel, lista_posicoes, posicoes_cobra):
        self.posicao = (0, 0)
        
        if movel == True: 
            self.color = v.roxo
        else:
            self.color = v.preto
        self.aleatorizar_posicao(lista_posicoes, posicoes_cobra)
        self.movel = movel

    # Aleatorizar a posição do inimigo
    def aleatorizar_posicao(self, lista_posicoes, posicoes_cobra):
        self.posicao = ((random.randint(0, int(v.largura_rede) - 1) * v.tamanho_rede),
                        (random.randint(0, int(v.altura_rede) - 1) * v.tamanho_rede))
        if self.posicao in lista_posicoes or self.posicao in posicoes_cobra:
            self.aleatorizar_posicao(lista_posicoes, posicoes_cobra)

    # Desenhar o inimigo
    def desenhar(self, superficie):
        iminigo_fixo = pygame.image.load('img\inimigo.png').convert_alpha()
        retangulo = pygame.Rect((self.posicao[0], self.posicao[1]), (v.tamanho_rede, v.tamanho_rede))
        superficie.blit(iminigo_fixo,retangulo)
        #pygame.draw.rect(superficie, self.color, retangulo)
        #pygame.draw.rect(superficie, v.preto, retangulo, 1)

    def comando(self, direcao):
        x, y = direcao
        novo = (((self.posicao[0] + (v.tamanho_rede)) % v.largura), (self.posicao[1] + (y * v.tamanho_rede)) % v.altura)
        self.posicao = novo
