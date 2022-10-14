# from tkinter import font
import pygame

import sys
from Cobra import Cobra
from Comida import Comida
from Inimigo import Inimigo
from Velocidade import Velocidade
import Variaveis as v
from Portal import Portal
from PocaoVida import Vida
from Fase1 import Fase1
from Fase2 import Fase2
from Fase3 import Fase3

pygame.init()

# Função da "rede"
def desenhar_rede(superficie):
    # Loop para fazer a "rede"
    for y in range(0, int(v.altura_rede)):
        for x in range(0, int(v.largura_rede)):
            # Fazer os quadrados que estão lado a lado terem cores diferentes
            if ((x + y) % 2) == 0:
                # r = retângulo
                # Definindo o retângulo
                retangulo = pygame.Rect((x * v.tamanho_rede, y * v.tamanho_rede), (v.tamanho_rede, v.tamanho_rede))
                # Desenhar o retângulo
                pygame.draw.rect(superficie, v.branco, retangulo)
            else:
                # rr = retângulo
                retangulo2 = pygame.Rect((x * v.tamanho_rede, y * v.tamanho_rede), (v.tamanho_rede, v.tamanho_rede))
                pygame.draw.rect(superficie, v.cinza, retangulo2)


# Fonte do texto que estará no placar
fonte = pygame.font.Font('freesansbold.ttf', 30)

def inimigo_main(inimigo, vida):
    if vida <= 0:
        pygame.quit()
        sys.exit()
    # Diminui a pontuação
    vida -= 1
    # O inimigo reaparece
    inimigo.aleatorizar_posicao()
    return vida, inimigo.posicao

def main():
    pygame.init()

    # Controla a velocidade com que o jogo roda
    relogio = pygame.time.Clock()
    # Setando a tela
    tela = pygame.display.set_mode((v.largura, v.altura), 0, 32)

    # Setar uma superfície
    # Melhor maneira de ter "múltiplas telas", como menus
    superficie = pygame.Surface(tela.get_size())
    # Muda o formato de pixel de uma imagem
    superficie = superficie.convert()

    # Criando a rede com as especificações da superfície
    # Será criada inicialmente, antes do jogo começar
    desenhar_rede(superficie)

    # Criando instâncias das classes
    cobra = Cobra()
    velocidade = Velocidade()

    #Vida começa com 3
    vida = 3

    Fase1(pygame, relogio, tela, superficie, desenhar_rede, cobra, velocidade, vida, v, fonte, inimigo_main)
    desenhar_rede(superficie)
    Fase2(pygame, relogio, tela, superficie, desenhar_rede, cobra, velocidade, vida, v, fonte, inimigo_main)
    desenhar_rede(superficie)
    Fase3(pygame, relogio, tela, superficie, desenhar_rede, cobra, velocidade, vida, v, fonte, inimigo_main)
    

# Chamando a função main
main()