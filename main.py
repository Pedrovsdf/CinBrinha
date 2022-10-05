import pygame
import sys
import random
from Cobra import Cobra

pygame.init()



# Classe da comida padrão
class Comida(object):
    # Definindo as informações principais da comida
    def __init__(self):
        self.posicao = (0, 0)
        self.color = vermelho
        self.aleatorizar_posicao()

    # Aleatorizar a posição da comida
    def aleatorizar_posicao(self):
        self.posicao = (random.randint(0, int(largura_rede) - 1) * tamanho_rede,
                        random.randint(0, int(altura_rede) - 1) * tamanho_rede)

    # Desenhar a comida
    def desenhar(self, superficie):
        retangulo = pygame.Rect((self.posicao[0], self.posicao[1]), (tamanho_rede, tamanho_rede))
        pygame.draw.rect(superficie, self.color, retangulo)
        pygame.draw.rect(superficie, preto, retangulo, 1)

class Inimigo(object):
    # Definindo as informações principais da comida
    def __init__(self):
        self.posicao = (0, 0)
        self.color = preto
        self.aleatorizar_posicao()

    # Aleatorizar a posição da comida
    def aleatorizar_posicao(self):
        self.posicao = ((random.randint(0, int(largura_rede) - 1) * tamanho_rede),
                        (random.randint(0, int(altura_rede) - 1) * tamanho_rede))

    # Desenhar a comida
    def desenhar(self, superficie):
        retangulo = pygame.Rect((self.posicao[0], self.posicao[1]), (tamanho_rede, tamanho_rede))
        pygame.draw.rect(superficie, self.color, retangulo)
        pygame.draw.rect(superficie, preto, retangulo, 1)

# Função da "rede"
def desenhar_rede(superficie):
    # Loop para fazer a "rede"
    for y in range(0, int(altura_rede)):
        for x in range(0, int(largura_rede)):
            # Fazer os quadrados que estão lado a lado terem cores diferentes
            if ((x + y) % 2) == 0:
                # r = retângulo
                # Definindo o retângulo
                retangulo = pygame.Rect((x * tamanho_rede, y * tamanho_rede), (tamanho_rede, tamanho_rede))
                # Desenhar o retângulo
                pygame.draw.rect(superficie, cinza1, retangulo)
            else:
                # rr = retângulo
                retangulo2 = pygame.Rect((x * tamanho_rede, y * tamanho_rede), (tamanho_rede, tamanho_rede))
                pygame.draw.rect(superficie, cinza2, retangulo2)


# Na tela, 480/480 é o canto superior esquerdo e 0/0 é o inferior direito
# Largura da tela
largura = 480
# Altura da tela
altura = 480
# Definindo cores rgb
cinza1 = (120, 120, 120)
cinza2 = (170, 170, 170)
vermelho = (200, 40, 40)
verde = (20, 200, 50)
preto = (0, 0, 0)
# Tamanho da rede/cada retângulo
tamanho_rede = 20
# Largura de cada retângulo
largura_rede = largura / tamanho_rede
# Altura de cada retângulo
altura_rede = altura / tamanho_rede

# Posições em que a cobra pode se mover
CIMA = (0, -1)
BAIXO = (0, 1)
ESQUERDA = (-1, 0)
DIREITA = (1, 0)

# Fonte do texto que estará no placar
fonte = pygame.font.Font('freesansbold.ttf', 30)

# Pontuação inicial
pontuacao = 0


def main():
    pygame.init()

    # Controla a velocidade com que o jogo roda
    relogio = pygame.time.Clock()
    # Setando a tela
    tela = pygame.display.set_mode((largura, altura), 0, 32)

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
    inimigo = Inimigo()
    inimigo2 = Inimigo()
    inimigo3 = Inimigo()
    inimigo4 = Inimigo()

    # Pontuação começa com 0
    global pontuacao
    pontuacao = 0

    # Enquanto o jogo estiver rodando, o loop acontecerá
    while True:
        # Mudando a velocidade com que a cobra se move
        relogio.tick(10)
        # Saber se o jogador interagiu
        cobra.comandos()
        # Recriando a rede a cada loop
        desenhar_rede(superficie)
        # Mover o corpo da cobra
        cobra.mover()

        # Checar se a cobra comeu a comida
        if cobra.saber_cabeca() == comida.posicao:
            # Aumenta o tamanho da cobra
            cobra.tamanho += 1
            # Aumenta a pontuação
            pontuacao += 1
            # A comida reaparece
            comida.aleatorizar_posicao()
        if cobra.saber_cabeca() == (inimigo.posicao):
            if pontuacao == 0:
                pygame.quit()
                sys.exit()
            # Diminui a pontuação
            pontuacao -= 1
            # O inimigo reaparece
            inimigo.aleatorizar_posicao()
        elif cobra.saber_cabeca() == (inimigo2.posicao):
            if pontuacao == 0:
                pygame.quit()
                sys.exit()
            # Diminui a pontuação
            pontuacao -= 1
            # O inimigo reaparece
            inimigo2.aleatorizar_posicao()
        elif cobra.saber_cabeca() == (inimigo3.posicao):
            if pontuacao == 0:
                pygame.quit()
                sys.exit()
            # Diminui a pontuação
            pontuacao -= 1
            # O inimigo reaparece
            inimigo3.aleatorizar_posicao()
        elif cobra.saber_cabeca() == (inimigo4.posicao):
            if pontuacao == 0:
                pygame.quit()
                sys.exit()
            # Diminui a pontuação
            pontuacao -= 1
            # O inimigo reaparece
            inimigo4.aleatorizar_posicao()
        # redesenhar a cobra, que pode estar maior do que antes
        cobra.desenhar(superficie)
        # redesenhar a comida, que pode ter sido comida
        comida.desenhar(superficie)
        inimigo.desenhar(superficie)
        inimigo2.desenhar(superficie)
        inimigo3.desenhar(superficie)
        inimigo4.desenhar(superficie)
        # Tendo certeza de que a superfície está na tela
        tela.blit(superficie, (0, 0))
        # Texto do placar
        text = fonte.render("Pontos: {0}".format(pontuacao), True, preto)
        # Placar
        tela.blit(text, (5, 10))
        # Fazendo a superfície de exibição realmente aparecer no monitor do usuário
        pygame.display.update()


# Chamando a função main
main()