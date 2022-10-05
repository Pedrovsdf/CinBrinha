class Variaveis(object):
    def __init__(self):
        # Na tela, 480/480 é o canto superior esquerdo e 0/0 é o inferior direito
        # Largura da tela
        self.largura = 480
        # Altura da tela
        self.altura = 480
        # Definindo cores rgb
        self.preto = (0, 0, 0)
        self.branco = (255, 255, 255)
        self.cinza = (170, 170, 170)
        self.vermelho = (200, 40, 40)
        self.verde = (20, 200, 50)
        self.amarelo = (243, 213, 0)
        # Tamanho da rede/cada retângulo
        self.tamanho_rede = 20
        # Largura de cada retângulo
        self.largura_rede = Variaveis.largura / Variaveis.tamanho_rede
        # Altura de cada retângulo
        self.altura_rede = Variaveis.altura / Variaveis.tamanho_rede

        # Posições em que a cobra pode se mover
        self.CIMA = (0, -1)
        self.BAIXO = (0, 1)
        self.ESQUERDA = (-1, 0)
        self.DIREITA = (1, 0)
    
    
    