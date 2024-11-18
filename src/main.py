import pygame
from constants import largura, altura

def main():
    pygame.init()

    # Carregando a imagem de fundo e redimesionando para o tamanho da tela.
    img_fundo = pygame.image.load("images/fundo.jpg")
    img_fundo = pygame.transform.scale(img_fundo, (largura, altura))

    # Definindo o tamanho da tela.
    tela = pygame.display.set_mode((largura, altura))

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Função para desenhar em cima de uma outra superfície (desenhar a imagem de fundo por cima da tela, partindo do canto superior esquerdo).
        tela.blit(img_fundo, (0, 0))

        # Atualização da tela depois de desenhar.
        pygame.display.flip()


    pygame.quit()

if __name__ == '__main__':
    main()