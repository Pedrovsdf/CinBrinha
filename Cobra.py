import pygame
import sys
import random
import Variaveis as v


class Cobra(object):
    # Definindo as informações principais da cobra
    def __init__(self):
        # Tamanho da cobra
        self.tamanho = 1
        # Posição de toda a cobra, começando no meio da tela
        self.posicoes = [((v.largura / 2), (v.altura / 2))]
        # Começar se movendo numa direção aleatória
        self.direcao = random.choice([v.CIMA, v.BAIXO, v.ESQUERDA, v.DIREITA])
        # Cor da cobra
        self.color = v.verde

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
        novo = (((atual[0] + (x * v.tamanho_rede)) % v.largura), (atual[1] + (y * v.tamanho_rede)) % v.altura)
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
        self.posicoes = [((v.largura / 2), (v.altura / 2))]
        self.direcao = random.choice([v.CIMA, v.BAIXO, v.ESQUERDA, v.DIREITA])
        global pontuacao
        pontuacao = 0

    # Desenhar o corpo da cobra na superfície
    def desenhar(self, superficie):
        for posicao in self.posicoes:
            retangulo = pygame.Rect((posicao[0], posicao[1]), (v.tamanho_rede, v.tamanho_rede))
            pygame.draw.rect(superficie, self.color, retangulo)
            pygame.draw.rect(superficie, v.preto, retangulo, 1)

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
                    self.virar(v.CIMA)
                elif evento.key == pygame.K_DOWN:
                    self.virar(v.BAIXO)
                elif evento.key == pygame.K_LEFT:
                    self.virar(v.ESQUERDA)
                elif evento.key == pygame.K_RIGHT:
                    self.virar(v.DIREITA)


# Pontuação inicial
pontuacao = 0
