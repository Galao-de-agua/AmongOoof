#Importando bibliotecas
import pygame

def explicacao(window):
    #Criando tela
    WIDTH = 383*2
    HEIGHT = 286*2

    #Criando a cadeia
    cadeia_img = pygame.image.load('imagens/rosa_preso.png').convert() 
    cadeia_img = pygame.transform.scale(cadeia_img, (300, 300))

    #Criando o título
    titulo_img = pygame.image.load('imagens/titulo_among_ooof.png').convert()
    titulo_img = pygame.transform.scale(titulo_img, (203, 47))

    #Definindo all sprites
    all_sprites = pygame.sprite.Group()

    class Rosa(pygame.sprite.Sprite):
        def __init__(self, img):
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH / 2
            self.rect.centery = 420

    class Titulo(pygame.sprite.Sprite):
        def __init__(self, img):
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH / 2
            self.rect.centery = 250

    #Criando o personagem rosa preso
    rosa_preso = Rosa(cadeia_img)
    all_sprites.add(rosa_preso)

    #Criando o título
    titulo = Titulo(titulo_img)
    all_sprites.add(titulo)

    # ----- Inicia estruturas de dados
    game = True

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    FPS = 30

    #Criando a cor branco
    red = (255, 255, 255)
    #Criando a cor vermelho
    white = (255, 0, 0)

    #Criando variáveis
    mensagem_final = ''

    #Criando a fonte para o texto
    font_fim = pygame.font.SysFont(None, 40)


    while game:

        clock.tick(FPS)
        window.fill((0, 0, 0))  # Preenche com a cor preta

        mensagem_final= 'Obrigado pelo trabalho! O policial rosa está preso.'
        superficie_1 = font_fim.render(mensagem_final, True, red)
        window.blit(superficie_1,(383-superficie_1.get_rect().width/2, 20))

        mensagem_final2 = 'Eis a história: ele viu o dono do museu correndo'
        superficie_2 = font_fim.render(mensagem_final2, True, red)
        window.blit(superficie_2,(383-superficie_2.get_rect().width/2, 60))

        mensagem_final3 = 'com o quadro que salvou do incêndio, achou'
        superficie_3 = font_fim.render(mensagem_final3, True, red)
        window.blit(superficie_3,(383-superficie_3.get_rect().width/2, 100))

        mensagem_final4 = 'que ele estava roubando e atirou'
        superficie_4 = font_fim.render(mensagem_final4, True, red)
        window.blit(superficie_4,(383-superficie_4.get_rect().width/2, 140))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        
        # ----- Gera saídas -----
        all_sprites.update()
        all_sprites.draw(window)
        pygame.display.update()  # Mostra o novo frame para o jogador
        window.blit(cadeia_img, (0, 0))

    pygame.quit()
