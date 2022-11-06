#importação de bibliotecas e variáveis
import random
import sys
import pygame
import Variaveis as v

#classe da cobra
class Cobra(object):
    # Definindo as informações principais da cobra
    def __init__(self):
        # Tamanho da cobra
        self.tamanho = 3
        # Posição de toda a cobra, começando no meio da tela
        self.posicoes = [(int(v.largura / 2), int(v.altura / 2))]
        # Começar se movendo numa direção aleatória
        self.direcao = random.choice([v.CIMA, v.BAIXO, v.ESQUERDA, v.DIREITA])
        # Pontuacao da cobra
        self.pontuacao = 0

        # adicionando os gráficos
        # gráficos da cabeça
        self.cabeça_direita = pygame.image.load('img\head_right.png').convert_alpha()
        self.cabeça_esquerda = pygame.image.load('img\head_left.png').convert_alpha()
        self.cabeça_cima = pygame.image.load('img\head_up.png').convert_alpha()
        self.cabeça_baixo = pygame.image.load('img\head_down.png')

        # gráficos da cauda
        self.cauda_baixo = pygame.image.load('img\cauda_down.png').convert_alpha()
        self.cauda_esquerda = pygame.image.load('img\cauda_left.png').convert_alpha()
        self.cauda_direita = pygame.image.load('img\cauda_right.png').convert_alpha()
        self.cauda_cima = pygame.image.load('img\cauda_up.png').convert_alpha()
        
        # gráficos corpo

        self.corpo_vertical = pygame.image.load('img\corpo_vertical.png').convert_alpha()
        self.corpo_horizontal = pygame.image.load('img\corpo_horizontal.png').convert_alpha()

        # gráficos quinas

        self.cornerTL = pygame.image.load('img\corpo_topleft.png').convert_alpha()
        self.cornerTR = pygame.image.load('img\corpo_topright.png').convert_alpha()
        self.cornerBL = pygame.image.load('img\corpo_bottomleft.png').convert_alpha()
        self.cornerBR = pygame.image.load('img\corpo_bottomright.png').convert_alpha()
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
        novo = (int((atual[0] + (x * v.tamanho_rede)) % v.largura), int(atual[1] + (y * v.tamanho_rede)) % v.altura)
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
        sound2 = pygame.mixer.Sound('som\colisao_inimigo.mp3')
        pygame.mixer.Sound.play(sound2)
        self.tamanho = 3
        self.posicoes = [((v.largura / 2), (v.altura / 2))]
        self.direcao = random.choice([v.CIMA, v.BAIXO, v.ESQUERDA, v.DIREITA])
        self.pontuacao = 0
        return self.tamanho, self.posicoes, self.direcao, self.pontuacao

    # Desenhar o corpo da cobra na superfície

    def desenhar(self, superficie):

        for index,posicao in enumerate(self.posicoes):
            retangulo = pygame.Rect((posicao[0], posicao[1]), (v.tamanho_rede, v.tamanho_rede))
            # inserir a imagem da cobra
            # se o index for 0 é a cabeça
            if index == 0:
                # mudanca do grafico quando a cabeça muda de direção
                if self.direcao == v.DIREITA:
                    superficie.blit(self.cabeça_direita,retangulo)
                elif self.direcao == v.ESQUERDA:
                    superficie.blit(self.cabeça_esquerda,retangulo)
                elif self.direcao == v.CIMA:
                    superficie.blit(self.cabeça_cima,retangulo)
                elif self.direcao == v.BAIXO:
                    superficie.blit(self.cabeça_baixo,retangulo)
            elif index == len(self.posicoes) - 1:
                tail_relationX = self.posicoes[-2][0] - self.posicoes[-1][0]
                tail_relationY = self.posicoes[-2][1] - self.posicoes[-1][1]

                # mudanca do grafico quando a cauda muda de direção
                if tail_relationX == 20 and tail_relationY == 0:
                    superficie.blit(self.cauda_esquerda,retangulo)
                elif tail_relationX == -20 and tail_relationY == 0:
                    superficie.blit(self.cauda_direita,retangulo)
                elif tail_relationX == 0 and tail_relationY == 20:
                    superficie.blit(self.cauda_cima,retangulo)
                elif tail_relationX == 0 and tail_relationY == -20:
                    superficie.blit(self.cauda_baixo,retangulo)

                #direcao_anterior = self.direcao
                
            else:
                bloco_anteriorX = self.posicoes[index + 1][0] - posicao[0]
                bloco_posteriorX = self.posicoes[index - 1][0] - posicao[0]

                bloco_anteriorY = self.posicoes[index + 1][1] - posicao[1]
                bloco_posteriorY = self.posicoes[index - 1][1] - posicao[1]

                if bloco_anteriorX == bloco_posteriorX:
                    superficie.blit(self.corpo_vertical,retangulo)
                elif bloco_anteriorY == bloco_posteriorY:
                    superficie.blit(self.corpo_horizontal,retangulo)
                else:
                    if bloco_anteriorX == -20 and bloco_posteriorY == -20 or bloco_anteriorY == -20 and bloco_posteriorX == -20 :
                        superficie.blit(self.cornerTL,retangulo)
                    elif bloco_anteriorX == -20 and bloco_posteriorY == 20 or bloco_anteriorY == 20 and bloco_posteriorX == -20 :
                        superficie.blit(self.cornerBL,retangulo)
                    elif bloco_anteriorX == 20 and bloco_posteriorY == -20 or bloco_anteriorY == -20 and bloco_posteriorX == 20 :
                        superficie.blit(self.cornerTR,retangulo)
                    elif bloco_anteriorX == 20 and bloco_posteriorY == 20 or bloco_anteriorY == 20 and bloco_posteriorX == 20 :
                        superficie.blit(self.cornerBR,retangulo)

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
