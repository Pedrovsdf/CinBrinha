import pygame
import random
import Variaveis as v


# Classe da comida padrão
class Comida(object):
    # Definindo as informações principais da comida
    def __init__(self):
        self.posicao = (0, 0)
        self.color = v.amarelo
        self.aleatorizar_posicao()

    # Aleatorizar a posição da comida
    def aleatorizar_posicao(self):
        self.posicao = (random.randint(0, int(v.largura_rede) - 1) * v.tamanho_rede,
                        random.randint(0, int(v.altura_rede) - 1) * v.tamanho_rede)

    # Desenhar a comida
    def desenhar(self, superficie):
        retangulo = pygame.Rect((self.posicao[0], self.posicao[1]), (v.tamanho_rede, v.tamanho_rede))
        pygame.draw.rect(superficie, self.color, retangulo)
        pygame.draw.rect(superficie, v.preto, retangulo, 1)