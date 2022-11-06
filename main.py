import sys

import pygame
import Variaveis as v
from Cobra import Cobra
from Fase1 import Fase1
from Fase2 import Fase2
from Fase3 import Fase3
from Inimigo import Inimigo
from PocaoVida import Vida
from Pontos import Ponto
from Portal import Portal

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
                pygame.draw.rect(superficie, v.verde_escuro, retangulo)
            else:
                # rr = retângulo
                retangulo2 = pygame.Rect((x * v.tamanho_rede, y * v.tamanho_rede), (v.tamanho_rede, v.tamanho_rede))
                pygame.draw.rect(superficie, v.verde_escuro, retangulo2)


# Fonte do texto que estará no placar
fonte = pygame.font.Font('freesansbold.ttf', 30)

def inimigo_main(inimigo, vida, posicoes_obj, posicoes_cobra):
    
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

# Chamando a função main

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('CINbrinha')

font = pygame.font.SysFont('Constantia', 30)

#define colours

#define global variable
clicked = False
counter = 0

class button():
		
	#colours for button and text
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

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)

		#add text to button
		text_img = font.render(self.text, True, self.cor_texto)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action



again = button(75, 200, 'Jogar')
play_again = button(75, 200, 'Jogar Novamente', 240)
quit = button(325, 200, 'Sair')

def menu(vitoria = False):
    while True:

        screen.fill(v.verde_claro)

        if vitoria == True:
           text_congrats = fonte.render("Parabens voce ganhou!", True, v.preto)
           screen.blit(text_congrats, (120, 140))

           if play_again.draw_button():
                main()
        else:
            if again.draw_button():
                main()
            
        if quit.draw_button():
            print('Quit')
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()

menu()
