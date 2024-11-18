import pygame
from constants import largura_tela, altura_tela
from menu import desenha_menu


def main():
    pygame.init()

    # Definindo o tamanho da tela.
    tela = pygame.display.set_mode((largura_tela, altura_tela))

    run = True
    main_menu = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if main_menu:
            personagens_escolhidos = desenha_menu(tela)

        # Atualização da tela depois de desenhar.
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()