import pygame # type: ignore

class Personagem:
    
    '''
    Atributos dos personagens:
        - Nome;
        - Ataque;
        - Defesa;
        - Vida máxima;
        - Vida atual;
        - Velocidade;
        - Imagem;
        - Defesa ativa;
        - Habilidade ativa;
        - Posição no menu principal;
        - Foi selecionado;
        - Vivo.
    '''

    def __init__(self, nome, ataque, defesa, vida_max, velocidade, src_imagem, src_imagem_menu, src_imagem_menu_selecionado):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.vida_max = vida_max
        self.vida = vida_max
        self.velocidade = velocidade
        self.imagem = pygame.image.load(src_imagem)
        self.defesa_ativa = False
        self.habilidade_ativa = False
        self.posicao_menu = None
        self.selecionado = False
        self.esta_vivo = True
        self.imagem_menu = pygame.image.load(src_imagem_menu)
        self.imagem_menu_selecionado = pygame.image.load(src_imagem_menu_selecionado)

    def exibir_imagem(self, tela, pos_x, pos_y):
        tela.blit(self.imagem_atual, (pos_x, pos_y))

    @staticmethod
    def cria_personagens():
        # Criando as instâncias dos personagens e salvando em uma lista.
        return [
            Personagem('Zeus', 80, 60, 150, 70, 'images/batalha/zeus.png', 'images/menu/zeus-menu.png', 'images/menu/zeus-menu-selecionado.png'),
            Personagem('Atena', 70, 90, 130, 80, 'images/batalha/atena.png', 'images/menu/atena-menu.png', 'images/menu/atena-menu-selecionado.png'),
            Personagem('Ares', 90, 50, 140, 60, 'images/batalha/ares.png', 'images/menu/ares-menu.png', 'images/menu/ares-menu-selecionado.png'),
            Personagem('Ártemis', 75, 55, 120, 90, 'images/batalha/artemis.png', 'images/menu/artemis-menu.png', 'images/menu/artemis-menu-selecionado.png'),
            Personagem('Poseidon', 85, 65, 160, 65, 'images/batalha/poseidon.png', 'images/menu/poseidon-menu.png', 'images/menu/poseidon-menu-selecionado.png')
        ]