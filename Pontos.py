#importação de bibliotecas e variáveis
import random
import pygame
import Variaveis as v


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

        #impedir que a pontuação renasça em cima de outros objetos
        if self.posicao in lista_posicoes or self.posicao in posicoes_cobra:
            self.aleatorizar_posicao(lista_posicoes, posicoes_cobra)

    # Desenhar a pontuação
    def desenhar(self, superficie):
        fruta = pygame.image.load('img\pontos.png').convert_alpha()
        retangulo = pygame.Rect((self.posicao[0], self.posicao[1]), (v.tamanho_rede, v.tamanho_rede))
        superficie.blit(fruta, retangulo)


