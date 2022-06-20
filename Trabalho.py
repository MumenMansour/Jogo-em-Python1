from lib2to3.pygram import python_grammar_no_print_statement


import pygame

#funçao para randozimar valores
from random import randint

#inicializaçao da aplicaçao
pygame.init 
#variaveis 
x = 380
y = 350
velocidade = 15
pos_x = 150
pos_y = 650
pos_y_a= 800
pos_y_b= 800

velocidadeoutros = 15

#importar imagem
fundo = pygame.image.load("FUNDO.png")
carro3 = pygame.image.load("carro3.png")
carro = pygame.image.load("carro.png")
carro1 = pygame.image.load("carro1.png")
carro2 = pygame.image.load("carro2.png")

#criar janela + tamanho da janela
janela = pygame.display.set_mode((800,600))
#nome da janela
pygame.display.set_caption("Jogo em Phyton")
#comandos para manter a janela aberta ate fechar manualmente
janela_aberta = True
while janela_aberta :
    #comando repeat a cada 50 milisegunos
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    #comando da movimentaçao
    comandos = pygame.key.get_pressed()

    #comado seta pra cima
    #if comandos[pygame.K_UP]:
        #decrementar
        #y -= velocidade

    #comando seta pra baixo    
    #if comandos[pygame.K_DOWN]:
        #encrementar
        #y += velocidade
        
    #comando seta direita
    if comandos[pygame.K_RIGHT] and x <= 625:
        #decrementar
        x += velocidade

    #comando seta esquerda 
    if comandos[pygame.K_LEFT] and x >= 99 :
        #decrementar
        x -= velocidade
    if(pos_y <= -300):
       pos_y = 600
       pos_y -= velocidadeoutros 

    #detecta colisao direito
    if ((x + 50 > pos_x and y + 101 > pos_y)):
        #sumir o carro da tela caso bata
        y = 1200
    
    #colisao lateral esquerdo
    if ((x - 50 < pos_x - 101 and y + 101 > pos_y_a)): 
        #sumir o carro da tela caso bata
        y = 1200
    
    #colisao central
    if ((x - 50 < pos_x -101 and y + 101 > pos_y_a)) and ((x + 50 > pos_x and y + 101 > pos_y)) :
        #sumir o carro da tela caso bata
        y = 1200

    #movimentaçao dos npc's
    if(pos_y <= -80) :
        pos_y = randint(800,2000)
        
        
    if (pos_y_a <= -80) :   
        pos_y_a = randint(1200,2000)
    
    if (pos_y_b <= -80) :
        pos_y_b = randint(2200,3000)


    #comando para mudar velocidade dos npc
    pos_y -= velocidadeoutros
    pos_y_a -= velocidadeoutros +3
    pos_y_b -= velocidadeoutros +5
    

    #comando para n deixa rrastro do item
    #janela.fill((0,0,0))                    
                     #(janela,(cor),(local),tamanho-px)            
    #pygame.draw.circle(janela,(0,255,0),(x,y),25)
    #comando para aparecer a imagen no console
    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(carro1,(pos_x ,pos_y))
    janela.blit(carro2,(pos_x +200,pos_y_a))
    janela.blit(carro3,(pos_x +450,pos_y_b))


    
    pygame.display.update()


#fechamento do jogo/comando
pygame.QUIT()


