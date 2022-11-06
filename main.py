import sys

import pygame
import Variaveis as v
from Cobra import Cobra
from Fase1 import Fase1
from Fase2 import Fase2
from Fase3 import Fase3

pygame.init()

# Função da "rede"
def desenhar_rede(superficie):
    # Loop para fazer a "rede"
    for y in range(0, int(v.altura_rede)):
        for x in range(0, int(v.largura_rede)):
            retangulo2 = pygame.Rect((x * v.tamanho_rede, y * v.tamanho_rede), (v.tamanho_rede, v.tamanho_rede))
            pygame.draw.rect(superficie, v.verde_escuro, retangulo2)


# Fonte do texto que estará no placar
fonte = pygame.font.Font('freesansbold.ttf', 30)

def inimigo_main(inimigo, vida, posicoes_obj, posicoes_cobra):
    #reseta o jogo quando a vida fica menor que 0
    if vida <= 0:
        sound6 = pygame.mixer.Sound('som\gameover.wav')
        pygame.mixer.Sound.play(sound6)
        menu()
    # Diminui a pontuação
    vida -= 1
    # O inimigo reaparece
    inimigo.aleatorizar_posicao(posicoes_obj, posicoes_cobra) 
    return vida, inimigo.posicao

def main():
    sound5 = pygame.mixer.music.load('som\som_ambiente.mp3')
    pygame.mixer.music.play(-1,0)
    pygame.init()
    pygame.mixer.init()
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

    #Vida começa com 3
    vida = 3

    vida = Fase1(pygame, relogio, tela, superficie, desenhar_rede, cobra, vida, v, fonte, inimigo_main)
    desenhar_rede(superficie)
    vida = Fase2(pygame, relogio, tela, superficie, desenhar_rede, cobra, vida, v, fonte, inimigo_main)
    desenhar_rede(superficie)
    Fase3(pygame, relogio, tela, superficie, desenhar_rede, cobra, vida, v, fonte, inimigo_main)
    menu(True)

screen = pygame.display.set_mode((v.largura, v.altura))
pygame.display.set_caption('CINbrinha')

font = pygame.font.SysFont('Constantia', 30)

#define variável global
clicked = False
counter = 0

class button():
		
	#cores para o botão e o texto
	button_col = (255, 0, 0)
	hover_col = (75, 225, 255)
	click_col = (50, 150, 255)
	cor_texto = v.preto
	height = 70

	def __init__(self, x, y, text, width = 180):
		self.x = x
		self.y = y
		self.text = text
		self.width = width


	def draw_button(self):

		global clicked
		action = False

		#obtem posição do mouse
		pos = pygame.mouse.get_pos()

		#cria o retângulo para o botão
		button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
		
		#checa se o mouse tá em cima do botão
		if button_rect.collidepoint(pos):
            #checa se o mouse foi clicado
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
            #checa se o mouse foi 'solto' e o click foi computado
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)

		#adiciona a fonte na 
		text_img = font.render(self.text, True, self.cor_texto)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action


#inicialização de botões
play = button(75, 200, 'Jogar')
play_again = button(75, 200, 'Jogar Novamente', 240)
quit = button(325, 200, 'Sair')

#função do menu
def menu(vitoria = False):
    while True:

        #preenche a tela
        screen.fill(v.verde_claro)

        #tela de vitória
        if vitoria == True:
            text_congrats = fonte.render("Parabéns você ganhou!", True, v.preto)
            screen.blit(text_congrats, (120, 140))

            #jogar novamente
            if play_again.draw_button():
                    main()
        else:
            if play.draw_button():
                main()
            
        #botão de sair
        if quit.draw_button():
            pygame.quit()
            sys.exit()

        #encerra o jogo se ele for fechado na aba
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()

menu()
