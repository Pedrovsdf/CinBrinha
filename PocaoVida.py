#importação de bibliotecas e variáveis
import pygame
import random
import Variaveis as v

# Classe da vida
class Vida(object):
    # Definindo as informações principais da vida
    def __init__(self, lista_posicoes, posicao_cobra):
        self.posicao = (0, 0)
        self.color = v.rosa
        self.aleatorizar_posicao(lista_posicoes, posicao_cobra)

    # Aleatorizar a posição da vida
    def aleatorizar_posicao(self, lista_posicoes, posicao_cobra):
        self.posicao = ((random.randint(0, int(v.largura_rede) - 1) * v.tamanho_rede),
                        (random.randint(0, int(v.altura_rede) - 1) * v.tamanho_rede))
        #impedir que a vida renasça em cima de outros objetos
        if self.posicao in lista_posicoes or self.posicao in posicao_cobra:
            self.aleatorizar_posicao(lista_posicoes, posicao_cobra)

    # Desenhar a vida
    def desenhar(self, superficie):
        vida = pygame.image.load('img\coracao.png').convert_alpha()
        retangulo = pygame.Rect((self.posicao[0], self.posicao[1]), (v.tamanho_rede, v.tamanho_rede))
        superficie.blit(vida,retangulo)
