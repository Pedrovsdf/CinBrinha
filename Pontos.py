import random

import pygame
import Variaveis as v


# Classe da pontuação padrão
class Ponto(object):
    # Definindo as informações principais da pontuação
    def __init__(self):
        self.posicao = (0, 0)
        self.color = v.amarelo
        self.aleatorizar_posicao()

    # Aleatorizar a posição da pontuação
    def aleatorizar_posicao(self):
        self.posicao = (random.randint(0, int(v.largura_rede) - 1) * v.tamanho_rede,
                        random.randint(0, int(v.altura_rede) - 1) * v.tamanho_rede)

    # Desenhar a pontuação
    def desenhar(self, superficie):
        retangulo = pygame.Rect((self.posicao[0], self.posicao[1]), (v.tamanho_rede, v.tamanho_rede))
        pygame.draw.rect(superficie, self.color, retangulo)
        pygame.draw.rect(superficie, v.preto, retangulo, 1)
