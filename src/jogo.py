import pygame # type: ignore
from batalha import desenha_fundo

def realiza_batalha(tela, personagens_selecionados):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        desenha_fundo(tela, personagens_selecionados)
        pygame.display.flip()