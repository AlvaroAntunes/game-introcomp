import pygame
from constants import largura_tela, altura_tela
from personagem import desenha_personagens

def desenha_menu(tela):
    # Carregando a imagem de fundo do menu e redimesionando para o tamanho da tela.
    img_fundo = pygame.image.load("images/fundo.jpg")
    img_fundo = pygame.transform.scale(img_fundo, (largura_tela, altura_tela))

    # Função para desenhar em cima de uma outra superfície (desenhar a imagem de fundo por cima da tela, partindo do canto superior esquerdo).
    tela.blit(img_fundo, (0, 0))

    # Definindo a fonte, a cor do título e o título que ficará no menu principal.
    font = pygame.font.Font(None, 45)
    cor_titulo = (255, 255, 255)
    texto_titulo = font.render('IntroBattle!', True, cor_titulo)

    # Definindo a posição do texto e escrevendo o título no menu principal.
    largura_texto = texto_titulo.get_width()
    altura_texto = texto_titulo.get_height()
    posicao_texto = ((largura_tela - largura_texto) // 2, 40)
    cor_fundo = (203, 54, 23)
    cor_borda = cor_titulo

    # Desenhando um retângulo para colocar um fundo no título.
    pygame.draw.rect(
        tela, 
        cor_borda,
        (posicao_texto[0] - 27, posicao_texto[1] - 7, largura_texto + 54, altura_texto + 14)
    )

    pygame.draw.rect(
        tela, 
        cor_fundo,
        (posicao_texto[0] - 25, posicao_texto[1] - 5, largura_texto + 50, altura_texto + 10)
    )

    tela.blit(texto_titulo, posicao_texto)

    desenha_personagens(tela)