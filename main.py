import pygame
import sys
from Cobra import Cobra
from Comida import Comida
from Inimigo import Inimigo
from Velocidade import Velocidade
import Variaveis as v

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
                pygame.draw.rect(superficie, v.cinza, retangulo)
            else:
                # rr = retângulo
                retangulo2 = pygame.Rect((x * v.tamanho_rede, y * v.tamanho_rede), (v.tamanho_rede, v.tamanho_rede))
                pygame.draw.rect(superficie, v.branco, retangulo2)


# Fonte do texto que estará no placar
fonte = pygame.font.Font('freesansbold.ttf', 30)


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
    comida = Comida()
    velocidade = Velocidade()
    inimigo = Inimigo(False)
    inimigo2 = Inimigo(False)
    inimigo3 = Inimigo(False)
    inimigo4= Inimigo(False)
    inimigo5= Inimigo(False)
    inimigo_movel1 = Inimigo(True)
    inimigo_movel2= Inimigo(True)

    # Pontuação começa com 0
    pontuacao = 0

    # Enquanto o jogo estiver rodando, o loop acontecerá
    while True:
        # Mudando a velocidade com que a cobra se move
        relogio.tick(v.vel)
        # Saber se o jogador interagiu
        cobra.comandos()
        # Recriando a rede a cada loop
        desenhar_rede(superficie)
        # Mover o corpo da cobra
        cobra.mover()
        inimigo_movel1.comando(v.CIMA)
        inimigo_movel2.comando(v.DIREITA)

        # Checar se a cobra comeu a comida
        if cobra.saber_cabeca() == comida.posicao:
            # Aumenta o tamanho da cobra
            cobra.tamanho += 1
            # Aumenta a pontuação
            pontuacao += 1
            # A comida reaparece
            comida.aleatorizar_posicao()
        # Checar se a cobra pegou o item de velocidade
        if cobra.saber_cabeca() == velocidade.posicao:
            v.vel += 2
            velocidade.aleatorizar_posicao()
        if cobra.saber_cabeca() == (inimigo.posicao):
            if pontuacao <= 0:
                pygame.quit()
                sys.exit()
            # Diminui a pontuação
            pontuacao -= 1
            # O inimigo reaparece
            inimigo.aleatorizar_posicao()
        elif cobra.saber_cabeca() == (inimigo2.posicao):
            if pontuacao <= 0:
                pygame.quit()
                sys.exit()
            # Diminui a pontuação
            pontuacao -= 1
            # O inimigo reaparece
            inimigo2.aleatorizar_posicao()
        elif cobra.saber_cabeca() == (inimigo3.posicao):
            if pontuacao <= 0:
                pygame.quit()
                sys.exit()
            # Diminui a pontuação
            pontuacao -= 1
            # O inimigo reaparece
            inimigo3.aleatorizar_posicao()
        elif cobra.saber_cabeca() == (inimigo4.posicao):
            if pontuacao <= 0:
                pygame.quit()
                sys.exit()
            # Diminui a pontuação
            pontuacao -= 1
            # O inimigo reaparece
            inimigo3.aleatorizar_posicao()
        elif cobra.saber_cabeca() == (inimigo5.posicao):
            if pontuacao <= 0:
                pygame.quit()
                sys.exit()
            # Diminui a pontuação
            pontuacao -= 1
            # O inimigo reaparece
            inimigo3.aleatorizar_posicao()
        elif cobra.saber_cabeca() == (inimigo_movel1.posicao):
            if pontuacao <= 0:
                pygame.quit()
                sys.exit()
            # Diminui a pontuação
            pontuacao -= 1
            # O inimigo reaparece
            #inimigo_movel1.aleatorizar_posicao()
        elif cobra.saber_cabeca() == (inimigo_movel2.posicao):
            if pontuacao <= 0:
                pygame.quit()
                sys.exit()
            # Diminui a pontuação
            pontuacao -= 1
            # O inimigo reaparece
            #inimigo_movel2.aleatorizar_posicao()
        # redesenhar a cobra, que pode estar maior do que antes
        cobra.desenhar(superficie)
        # redesenhar a comida, que pode ter sido comida
        comida.desenhar(superficie)
        velocidade.desenhar(superficie)
        inimigo.desenhar(superficie)
        inimigo2.desenhar(superficie)
        inimigo3.desenhar(superficie)
        inimigo4.desenhar(superficie)
        inimigo5.desenhar(superficie)
        inimigo_movel1.desenhar(superficie)
        inimigo_movel2.desenhar(superficie)
        # Tendo certeza de que a superfície está na tela
        tela.blit(superficie, (0, 0))
        if cobra.tamanho == 1:
            pontuacao = 0
        # Texto do placar
        text = fonte.render("Pontos: {0}".format(pontuacao), True, v.preto)
        # Placar
        tela.blit(text, (5, 10))
        # Fazendo a superfície de exibição realmente aparecer no monitor do usuário
        pygame.display.update()


# Chamando a função main
main()
