#importação de bibliotecas e variáveis
import pygame
import random

import Variaveis as v


class Inimigo(object):
    # Definindo as informações principais do inimigo
    def __init__(self, lista_posicoes, posicoes_cobra):
        self.posicao = (0, 0)
        self.aleatorizar_posicao(lista_posicoes, posicoes_cobra)

    # Aleatorizar a posição do inimigo
    def aleatorizar_posicao(self, lista_posicoes, posicoes_cobra):
        self.posicao = ((random.randint(0, int(v.largura_rede) - 1) * v.tamanho_rede),
                        (random.randint(0, int(v.altura_rede) - 1) * v.tamanho_rede))
        #impede que o inimigo renasça numa posição que já é ocupada pela cobra ou por outro objeto
        if self.posicao in lista_posicoes or self.posicao in posicoes_cobra:
            self.aleatorizar_posicao(lista_posicoes, posicoes_cobra)

    # Desenhar o inimigo
    def desenhar(self, superficie):
        inimigo = pygame.image.load('img\inimigo.png').convert_alpha()
        retangulo = pygame.Rect((self.posicao[0], self.posicao[1]), (v.tamanho_rede, v.tamanho_rede))
        superficie.blit(inimigo,retangulo)


    def movel(self, direcao):
        x, y = direcao
        #pega a posicao atual do inimigo e adiciona a tupla correspondente a direção (multiplicada pelo tamanho do 'quadradinho' da tela)
        #anda-se uma 'casa' nessa direção
        self.posicao = (((self.posicao[0] + (x * v.tamanho_rede)) % v.largura), (self.posicao[1] + (y * v.tamanho_rede)) % v.altura)
