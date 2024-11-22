import pygame # type: ignore
from constants import largura_tela, altura_tela

def desenha_fundo(tela):
    img_fundo = pygame.image.load('images/batalha/fundo-batalha.jpg')
    img_fundo = pygame.transform.scale(img_fundo, (largura_tela, altura_tela))
    tela.blit(img_fundo, (0, 0))
    # tela.fill((255, 129, 214))