import pygame # type: ignore
from constants import largura_tela, altura_tela

def desenha_fundo(tela, personagens_selecionados):
    img_fundo = pygame.image.load('images/batalha/fundo-batalha.png')
    img_fundo = pygame.transform.scale(img_fundo, (largura_tela, altura_tela))
    tela.blit(img_fundo, (0, 0))

    img_info_batalha = pygame.image.load('images/batalha/info-batalha.png')
    tela.blit(img_info_batalha, (30, 550))

    img_info_personagens = pygame.image.load('images/batalha/info-personagens.png')
    tela.blit(img_info_personagens, (largura_tela // 2 + 170, 550))
