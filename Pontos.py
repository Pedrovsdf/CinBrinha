import random

import pygame
import Variaveis as v
from Cobra import Cobra

# Classe da pontuação padrão
class Ponto(object):
    # Definindo as informações principais da pontuação
    def __init__(self, posicoes_obj, posicoes_cobra):
        self.posicao = (0, 0)
        self.color = v.amarelo
        self.aleatorizar_posicao(posicoes_obj, posicoes_cobra)

    # Aleatorizar a posição da pontuação
    def aleatorizar_posicao(self, lista_posicoes, posicoes_cobra):
        self.posicao = ((random.randint(0, int(v.largura_rede) - 1) * v.tamanho_rede),
                        (random.randint(0, int(v.altura_rede) - 1) * v.tamanho_rede))
        if self.posicao in lista_posicoes or self.posicao in posicoes_cobra:
            self.aleatorizar_posicao(lista_posicoes, posicoes_cobra)

    # Desenhar a pontuação
    def desenhar(self, superficie):
        retangulo = pygame.Rect((self.posicao[0], self.posicao[1]), (v.tamanho_rede, v.tamanho_rede))
        pygame.draw.rect(superficie, self.color, retangulo)
        pygame.draw.rect(superficie, v.preto, retangulo, 1)
