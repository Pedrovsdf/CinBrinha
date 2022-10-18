import pygame
import random
import Variaveis as v
from Cobra import Cobra

# Classe da vida
class Vida(object):
    # Definindo as informações principais da comida
    def __init__(self, lista_posicoes, posicao_cobra):
        self.posicao = (0, 0)
        self.color = v.rosa
        self.aleatorizar_posicao(lista_posicoes, posicao_cobra)


    # Aleatorizar a posição da comida
    def aleatorizar_posicao(self, lista_posicoes, posicao_cobra):
        self.posicao = ((random.randint(0, int(v.largura_rede) - 1) * v.tamanho_rede),
                        (random.randint(0, int(v.altura_rede) - 1) * v.tamanho_rede))
        if self.posicao in lista_posicoes or self.posicao in posicao_cobra:
            self.aleatorizar_posicao(lista_posicoes, posicao_cobra)

    # Desenhar a comida
    def desenhar(self, superficie):
        retangulo = pygame.Rect((self.posicao[0], self.posicao[1]), (v.tamanho_rede, v.tamanho_rede))
        pygame.draw.rect(superficie, self.color, retangulo)
        pygame.draw.rect(superficie, v.preto, retangulo, 1)
