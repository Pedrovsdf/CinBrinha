from Inimigo import Inimigo
from PocaoVida import Vida
from Pontos import Ponto
from Portal import Portal


def Fase3(pygame, relogio, tela, superficie, desenhar_rede, cobra, vida, v, fonte, inimigo_main):
  posicoes_obj = [(int(300), int(300))]
  
  ponto = Ponto(posicoes_obj, cobra.posicoes)
  posicoes_obj.append(ponto.posicao)

  pocao_vida = Vida(posicoes_obj, cobra.posicoes)
  posicoes_obj.append(pocao_vida.posicao)

  inimigo = Inimigo(False, posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo.posicao)

  inimigo2 = Inimigo(False, posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo2.posicao)

  inimigo3 = Inimigo(False, posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo3.posicao)

  inimigo4 = Inimigo(False, posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo4.posicao)

  inimigo5 = Inimigo(False, posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo5.posicao)

  inimigo6 = Inimigo(False, posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo6.posicao)
  
  inimigo7 = Inimigo(False, posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo7.posicao)
  
  inimigo_movel1 = Inimigo(True, posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo_movel1.posicao)

  inimigo_movel2 = Inimigo(True, posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo_movel2.posicao)
  
  inimigo_movel3 = Inimigo(True, posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo_movel3.posicao)
  
  inimigo_movel4 = Inimigo(True, posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo_movel4.posicao)
  
  inimigo_movel5 = Inimigo(True, posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo_movel5.posicao)

  inimigo_movel6 = Inimigo(True, posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo_movel6.posicao)
  
  inimigos = [inimigo, inimigo2, inimigo3, inimigo4, inimigo5, inimigo_movel1, inimigo_movel2, inimigo_movel3, inimigo_movel4, inimigo6, inimigo7, inimigo_movel5, inimigo_movel6]
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
    inimigo_movel5.comando(v.CIMA)
    inimigo_movel6.comando(v.ESQUERDA)
   
   
    if cobra.pontuacao >= 15:
        portal = Portal()
        portal.posicao = (300, 300)
        portal.desenhar(superficie)
        if portal.posicao == cobra.saber_cabeca():
            cobra.pontuacao = 0
            portal.posicao = (-1, -1)
            break


    # Checar se a cobra comeu o ponto
    if cobra.saber_cabeca() == ponto.posicao:
        # Aumenta o tamanho da cobra
        cobra.tamanho += 1
        # Aumenta a pontuação
        cobra.pontuacao += 1
        # O ponto reaparece
        ponto.aleatorizar_posicao()
    
    elif cobra.saber_cabeca() == pocao_vida.posicao and vida <5:
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
    # redesenhar 

    ponto.desenhar(superficie)
    pocao_vida.desenhar(superficie)
    inimigo.desenhar(superficie)
    inimigo2.desenhar(superficie)
    inimigo3.desenhar(superficie)
    inimigo4.desenhar(superficie)
    inimigo5.desenhar(superficie)
    inimigo6.desenhar(superficie)
    inimigo7.desenhar(superficie)
    inimigo_movel1.desenhar(superficie)
    inimigo_movel2.desenhar(superficie)
    inimigo_movel3.desenhar(superficie)
    inimigo_movel4.desenhar(superficie)
    inimigo_movel5.desenhar(superficie)
    inimigo_movel6.desenhar(superficie)
    pocao_vida.desenhar(superficie)
    # Tendo certeza de que a superfície está na tela
    tela.blit(superficie, (0, 0))
    if cobra.tamanho == 1:
        cobra.pontuacao = 0
     # Texto do placar
    text_pont = fonte.render("Pontos: {0}".format(cobra.pontuacao), True, v.preto)
    text_fase = fonte.render("Fase: 2", True, v.preto)
    text_vida = fonte.render("Vida: {0}".format(vida), True, v.preto)

    # Placar
    tela.blit(text_pont, (5, 10)) #pontuação no canto superior esquerdo
    tela.blit(text_fase, (260, 10)) #fase no meio superior 
    tela.blit(text_vida, (480, 10)) #vida no canto superior direito
    
    # Fazendo a superfície de exibição realmente aparecer no monitor do usuário
    pygame.display.update()