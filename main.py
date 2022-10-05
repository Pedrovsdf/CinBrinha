import pygame
import sys
import random

pygame.init()


# Classe da cobra
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


# Classe da comida padrão
class Comida(object):
    # Definindo as informações principais da comida
    def __init__(self):
        self.posicao = (0, 0)
        self.color = vermelho
        self.aleatorizar_posicao()

    # Desenhar a comida
    def desenhar(self, superficie):
        retangulo = pygame.Rect((self.posicao[0], self.posicao[1]), (tamanho_rede, tamanho_rede))
        pygame.draw.rect(superficie, self.color, retangulo)
        pygame.draw.rect(superficie, preto, retangulo, 1)

    # Aleatorizar a posição da comida
    def aleatorizar_posicao(self):
        self.posicao = (random.randint(0, int(largura_rede) - 1) * tamanho_rede,
                        random.randint(0, int(altura_rede) - 1) * tamanho_rede)


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
                pygame.draw.rect(superficie, branco, retangulo)
            else:
                # rr = retângulo
                retangulo2 = pygame.Rect((x * tamanho_rede, y * tamanho_rede), (tamanho_rede, tamanho_rede))
                pygame.draw.rect(superficie, cinza, retangulo2)

# Posições em que a cobra pode se mover
CIMA = (0, -1)
BAIXO = (0, 1)
ESQUERDA = (-1, 0)
DIREITA = (1, 0)

# Na tela, 480/480 é o canto superior esquerdo e 0/0 é o inferior direito
# Largura da tela
largura = 480
# Altura da tela
altura = 480
# Definindo cores rgb
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (170, 170, 170)
vermelho = (200, 40, 40)
verde = (20, 200, 50)
# Tamanho da rede/cada retângulo
tamanho_rede = 20
# Largura de cada retângulo
largura_rede = largura / tamanho_rede
# Altura de cada retângulo
altura_rede = altura / tamanho_rede

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
        # redesenhar a cobra, que pode estar maior do que antes
        cobra.desenhar(superficie)
        # redesenhar a comida, que pode ter sido comida
        comida.desenhar(superficie)
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
