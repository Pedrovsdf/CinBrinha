from Comida import Comida
from Inimigo import Inimigo
from PocaoVida import Vida
from Portal import Portal


def Fase2(pygame, relogio, tela, superficie, desenhar_rede, cobra, velocidade, vida, v, fonte, inimigo_main):
  comida = Comida()
  pocao_vida = Vida()
  inimigo = Inimigo(False)
  inimigo2 = Inimigo(False)
  inimigo3 = Inimigo(False)
  inimigo4 = Inimigo(False)
  inimigo5 = Inimigo(False)
  inimigo_movel1 = Inimigo(True)
  inimigo_movel2 = Inimigo(True)
  inimigo_movel3 = Inimigo(True)
  inimigo_movel4 = Inimigo(True)
  
  inimigos = [inimigo, inimigo2, inimigo3, inimigo4, inimigo5, inimigo_movel1, inimigo_movel2, inimigo_movel3, inimigo_movel4]
  print(f"teste{cobra.pontuacao}")
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
    inimigo_movel3.comando(v.ESQUERDA)
    inimigo_movel4.comando(v.BAIXO)
    if cobra.pontuacao >= 5:
        portal = Portal()
        portal.posicao = (300, 300)
        portal.desenhar(superficie)
        if portal.posicao == cobra.saber_cabeca():
            cobra.pontuacao = 0
            portal.posicao = (-1, -1)
            break
    # Checar se a cobra comeu a comida
    if cobra.saber_cabeca() == comida.posicao:
        # Aumenta o tamanho da cobra
        cobra.tamanho += 1
        # Aumenta a pontuação
        cobra.pontuacao += 1
        # A comida reaparece
        comida.aleatorizar_posicao()
    
    # Checar se a cobra pegou o item de velocidade
    if cobra.saber_cabeca() == velocidade.posicao:
        v.vel += 2
        cobra.pontuacao += 3
        cobra.tamanho += 1
        velocidade.aleatorizar_posicao()
    
    elif cobra.saber_cabeca() == pocao_vida.posicao and vida <3:
        # Aumenta a vida
        vida += 1
        # A vida reaparece a cada tempo
        pocao_vida.aleatorizar_posicao()

    #funçao para contabilizar o dano da vida
    for inimigo in inimigos:
        if cobra.saber_cabeca() == (inimigo.posicao):
            vida, inimigo.posicao = inimigo_main(inimigo, vida)
            break #quando achar um inimigo que bateu, já pode parar de procurar
    # redesenhar a cobra, que pode estar maior do que antes
    cobra.desenhar(superficie)
    # redesenhar a comida, que pode ter sido comida
    comida.desenhar(superficie)
    velocidade.desenhar(superficie)
    pocao_vida.desenhar(superficie)
    inimigo.desenhar(superficie)
    inimigo2.desenhar(superficie)
    inimigo3.desenhar(superficie)
    inimigo4.desenhar(superficie)
    inimigo5.desenhar(superficie)
    inimigo_movel1.desenhar(superficie)
    inimigo_movel2.desenhar(superficie)
    inimigo_movel3.desenhar(superficie)
    inimigo_movel4.desenhar(superficie)
    pocao_vida.desenhar(superficie)
    # Tendo certeza de que a superfície está na tela
    tela.blit(superficie, (0, 0))
    if cobra.tamanho == 1:
        cobra.pontuacao = 0
    # Texto do placar
    text_pont = fonte.render(f"Pontos: {cobra.pontuacao}", True, v.preto)
    text_vel = fonte.render("Velocidade: {0}".format(v.vel), True, v.preto)
    text_vida = fonte.render("Vida: {0}".format(vida), True, v.preto)
    # Placar
    tela.blit(text_pont, (5, 10)) #pontuação no canto superior esquerdo
    tela.blit(text_vel, (210, 10)) #velocidade no meio superior 
    tela.blit(text_vida, (480, 10)) #velocidade no canto superior direito
    # Fazendo a superfície de exibição realmente aparecer no monitor do usuário
    pygame.display.update()
