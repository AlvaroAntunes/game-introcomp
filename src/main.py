import pygame # type: ignore
from constants import largura_tela, altura_tela
from menu import desenha_menu
from jogo import realiza_batalha

def main():
    pygame.init()

    # Definindo o tamanho da tela.
    tela = pygame.display.set_mode((largura_tela, altura_tela))

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            personagens_selecionados = desenha_menu(tela)
            realiza_batalha(tela, personagens_selecionados)

        # Atualização da tela depois de desenhar.
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()