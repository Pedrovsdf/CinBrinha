import pygame
import sys
import random

class Cobra(object):
    # Definindo as informações principais da cobra
    def __init__(self):
        # Tamanho da cobra
        self.tamanho = 1
        # Posição de toda a cobra, começando no meio da tela
        self.posicoes = [((largura / 2), (altura / 2))]
        # Começar se movendo numa direção aleatória
        self.direcao = random.choice([CIMA, BAIXO, ESQUERDA, DIREITA])
        # Cor da cobra
        self.color = verde

    # Saber onde está a cabeça da cobra
    def saber_cabeca(self):
        # O primeiro item da lista é onde está a cabeça
        return self.posicoes[0]

    # Se tentar virar a direção da cobra
    def virar(self, ponto):
        # Checar se a cobra está indo para a mesma direção que tentei virar
        if self.tamanho > 1 and (ponto[0] * -1, ponto[1] * -1) == self.direcao:
            return
        else:
            self.direcao = ponto

    # Mover a cobra
    def mover(self):
        # Saber onde está a cabeça
        atual = self.saber_cabeca()
        # Direções de movimento
        x, y = self.direcao
        # Próxima localização da cobra
        # Qualquer que seja a direção, irá se mover apenas um quadrado por vez
        novo = (((atual[0] + (x * tamanho_rede)) % largura), (atual[1] + (y * tamanho_rede)) % altura)
        # Fazer com que o resto do corpo se mova para o lugar em que o pedaço da frente estava
        # Movendo apenas a "cabeça" e a "cauda"
        if len(self.posicoes) > 2 and novo in self.posicoes[2:]:
            # Colidiu
            self.reset()
        else:
            # A cabeça será adicionada na nova posição
            self.posicoes.insert(0, novo)
            # A "cauda" será apagada, tendo agora uma nova "cauda"
            # Quando resetar, o corpo será apagado, restando apenas a cabeça
            if len(self.posicoes) > self.tamanho:
                self.posicoes.pop()
        

    # Quando a cobra bater no próprio corpo, o jogo resetará
    def reset(self):
        self.tamanho = 1
        self.posicoes = [((largura / 2), (altura / 2))]
        self.direcao = random.choice([CIMA, BAIXO, ESQUERDA, DIREITA])
        global pontuacao
        pontuacao = 0

    # Desenhar o corpo da cobra na superfície
    def desenhar(self, superficie):
        for posicao in self.posicoes:
            retangulo = pygame.Rect((posicao[0], posicao[1]), (tamanho_rede, tamanho_rede))
            pygame.draw.rect(superficie, self.color, retangulo)
            pygame.draw.rect(superficie, preto, retangulo, 1)

    # Comandos
    def comandos(self):
        # Saber tudo o que o jogador faz
        for evento in pygame.event.get():
            # Se sair do jogo
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Se apertar alguma chave
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    self.virar(CIMA)
                elif evento.key == pygame.K_DOWN:
                    self.virar(BAIXO)
                elif evento.key == pygame.K_LEFT:
                    self.virar(ESQUERDA)
                elif evento.key == pygame.K_RIGHT:
                    self.virar(DIREITA)

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

# Pontuação inicial
pontuacao = 0