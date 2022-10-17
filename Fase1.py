from Inimigo import Inimigo
from PocaoVida import Vida
from Pontos import Ponto
from Portal import Portal


def Fase1(pygame, relogio, tela, superficie, desenhar_rede, cobra, vida, v, fonte, inimigo_main):
  ponto = Ponto()
  pocao_vida = Vida()
  inimigo = Inimigo(False)
  inimigo2 = Inimigo(False)
  inimigo3 = Inimigo(False)
  inimigo4 = Inimigo(False)
  inimigo_movel1 = Inimigo(True)
  inimigos = [inimigo, inimigo2, inimigo3, inimigo4, inimigo_movel1]
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
    if cobra.pontuacao >= 10: #a pontuação necessária para passar de fase é 5
        portal = Portal()
        portal.posicao = (300, 300)
        portal.desenhar(superficie)
        if portal.posicao == cobra.saber_cabeca():
            cobra.pontuacao = 0
            portal.posicao = (-1, -1)
            break
    if cobra.saber_cabeca() == ponto.posicao:
        # Aumenta o tamanho da cobra
        cobra.tamanho += 1
        # Aumenta a pontuação
        cobra.pontuacao += 1
        # O ponto reaparece
        ponto.aleatorizar_posicao()

    elif cobra.saber_cabeca() == pocao_vida.posicao and vida < 3:
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
    # redesenhar tudo, pode ter sido comido
    ponto.desenhar(superficie)
    pocao_vida.desenhar(superficie)
    inimigo.desenhar(superficie)
    inimigo2.desenhar(superficie)
    inimigo3.desenhar(superficie)
    inimigo4.desenhar(superficie)
    inimigo_movel1.desenhar(superficie)
    pocao_vida.desenhar(superficie)
    # Tendo certeza de que a superfície está na tela
    tela.blit(superficie, (0, 0))
    if cobra.tamanho == 1:
        cobra.pontuacao = 0
    # Texto do placar
    text_pont = fonte.render("Pontos: {0}".format(cobra.pontuacao), True, v.preto)
    text_fase = fonte.render("Fase: 1", True, v.preto)
    text_vida = fonte.render("Vida: {0}".format(vida), True, v.preto)

    # Placar
    tela.blit(text_pont, (5, 10)) #pontuação no canto superior esquerdo
    tela.blit(text_fase, (260, 10)) #fase no meio superior 
    tela.blit(text_vida, (480, 10)) #vida no canto superior direito


    # Fazendo a superfície de exibição realmente aparecer no monitor do usuário
    pygame.display.update()
