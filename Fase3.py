#importação de classes
from Inimigo import Inimigo
from PocaoVida import Vida
from Pontos import Ponto
from Portal import Portal


def Fase3(pygame, relogio, tela, superficie, desenhar_rede, cobra, vida, v, fonte, inimigo_main):
  posicoes_obj = [(int(300), int(300))]
  
  #Sequência de inicializações das Classes
  #Appends para incluir a posição dos objetos a cada inicialização, para evitar que um objeto surja...
  #... no mesmo local que outro
  ponto = Ponto(posicoes_obj, cobra.posicoes)
  posicoes_obj.append(ponto.posicao)

  pocao_vida = Vida(posicoes_obj, cobra.posicoes)
  posicoes_obj.append(pocao_vida.posicao)

  inimigo = Inimigo(posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo.posicao)

  inimigo2 = Inimigo(posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo2.posicao)

  inimigo3 = Inimigo(posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo3.posicao)

  inimigo4 = Inimigo(posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo4.posicao)

  inimigo5 = Inimigo(posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo5.posicao)
  
  inimigo_movel1 = Inimigo(posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo_movel1.posicao)

  inimigo_movel2 = Inimigo(posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo_movel2.posicao)
  
  inimigo_movel3 = Inimigo(posicoes_obj, cobra.posicoes)
  posicoes_obj.append(inimigo_movel3.posicao)
  
  inimigos = [inimigo, inimigo2, inimigo3, inimigo4, inimigo5, inimigo_movel1, inimigo_movel2, inimigo_movel3]
  while True:
    # Mudando a velocidade com que a cobra se move
    relogio.tick(v.vel)
    # Saber se o jogador interagiu
    cobra.comandos()
    # Recriando a rede a cada loop
    desenhar_rede(superficie)
    # Mover o corpo da cobra
    cobra.mover()

    #declaração do movimento dos inimigos móveis
    inimigo_movel1.movel(v.CIMA)
    inimigo_movel2.movel(v.DIREITA)
    inimigo_movel3.movel(v.ESQUERDA)
   
   #pontuação para abrir o portal
    if cobra.pontuacao >= 5:
        #surge o portal no centro
        portal = Portal()
        portal.posicao = (300, 300)
        portal.desenhar(superficie)

        #entra no portal
        if portal.posicao == cobra.saber_cabeca():
            cobra.pontuacao = 0
            portal.posicao = (-1, -1)
            sound7 = pygame.mixer.Sound('som\som_vitoria.mp3')
            pygame.mixer.Sound.play(sound7)
            break            
            
    # Checar se a cobra comeu o ponto
    if cobra.saber_cabeca() == ponto.posicao:
        sound1 = pygame.mixer.Sound('som\comer_maça.mp3')
        pygame.mixer.Sound.play(sound1)
        # Aumenta o tamanho da cobra
        cobra.tamanho += 1
        # Aumenta a pontuação
        cobra.pontuacao += 1
        # O ponto reaparece
        ponto.aleatorizar_posicao(posicoes_obj, cobra.posicoes)

    #cobra coleta a vida (máximo 3)
    elif cobra.saber_cabeca() == pocao_vida.posicao and vida <3:
        sound4 = pygame.mixer.Sound('som\poçao.wav')
        pygame.mixer.Sound.play(sound4)
        # Aumenta a vida
        vida += 1
        # A vida reaparece a cada tempo
        pocao_vida.aleatorizar_posicao(posicoes_obj, cobra.posicoes)

    #funçao para contabilizar o dano da vida
    for inimigo in inimigos:
        if len(cobra.posicoes) > 1 and inimigo.posicao in [cobra.saber_cabeca(), cobra.posicoes[1]]:
            sound2 = pygame.mixer.Sound('som\colisao_inimigo.mp3')
            pygame.mixer.Sound.play(sound2)
            vida, inimigo.posicao = inimigo_main(inimigo, vida, posicoes_obj, cobra.posicoes)
            #break #quando achar um inimigo que bateu, já pode parar de procurar
    # redesenhar a cobra, que pode estar maior do que antes
    cobra.desenhar(superficie)
    # redesenhar 

    ponto.desenhar(superficie)
    #vida só aparece na tela quando tem menos de 3
    if vida < 3:
        pocao_vida.desenhar(superficie)
    inimigo.desenhar(superficie)
    inimigo2.desenhar(superficie)
    inimigo3.desenhar(superficie)
    inimigo4.desenhar(superficie)
    inimigo5.desenhar(superficie)
    inimigo_movel1.desenhar(superficie)
    inimigo_movel2.desenhar(superficie)
    inimigo_movel3.desenhar(superficie)
    # Tendo certeza de que a superfície está na tela
    tela.blit(superficie, (0, 0))
    if cobra.tamanho == 3:
        cobra.pontuacao = 0
     # Texto do placar
    text_pont = fonte.render("Pontos: {0}".format(cobra.pontuacao), True, v.preto)
    text_fase = fonte.render("Fase: 3", True, v.preto)
    text_vida = fonte.render("Vida: {0}".format(vida), True, v.preto)

    # Placar
    tela.blit(text_pont, (5, 10)) #pontuação no canto superior esquerdo
    tela.blit(text_fase, (260, 10)) #fase no meio superior 
    tela.blit(text_vida, (480, 10)) #vida no canto superior direito
    
    # Fazendo a superfície de exibição realmente aparecer no monitor do usuário
    pygame.display.update()
