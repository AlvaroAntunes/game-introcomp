import pygame

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
        - Vivo.
    '''

    def __init__(self, nome, ataque, defesa, vida_max, velocidade, src_imagem):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.vida_max = vida_max
        self.vida = vida_max
        self.velocidade = velocidade
        self.imagem = pygame.image.load(src_imagem)
        self.defesa_ativa = False
        self.habilidade_ativa = False
        self.esta_vivo = True
        self.tamanho_menu = (100, 100)
        self.tamanho_batalha = (200, 200)
        self.imagem_atual = None

        self.redimensionar_para_menu()

    def redimensionar_para_menu(self):
        self.imagem_atual = pygame.transform.scale(self.imagem, self.tamanho_menu)

    def redimensionar_para_batalha(self):
        self.imagem_atual = pygame.transform.scale(self.imagem, self.tamanho_batalha)

    def exibir_imagem(self, tela, pos_x, pos_y):
        tela.blit(self.imagem_atual, (pos_x, pos_y))

    def desenha_personagens(self, tela):
        personagens = []

        # Criando as instâncias dos personagens.
        personagens.append(Personagem(
            'Zeus', 
            ataque=80, 
            defesa=60, 
            vida_max=150, 
            velocidade=70, 
            src_imagem='images/zeus.png'
        ))

        personagens.append(Personagem(
            'Atena', 
            ataque=70, 
            defesa=90, 
            vida_max=130, 
            velocidade=80, 
            src_imagem='images/atena.png'
        ))

        personagens.append(Personagem(
            'Ares', 
            ataque=90, 
            defesa=50, 
            vida_max=140, 
            velocidade=60, 
            src_imagem='images/ares.png'
        ))

        personagens.append(Personagem(
            'Ártemis', 
            ataque=75, 
            defesa=55, 
            vida_max=120, 
            velocidade=90, 
            src_imagem='images/artemis.png'
        ))

        personagens.append(Personagem(
            'Poseidon', 
            ataque=85, 
            defesa=65, 
            vida_max=160, 
            velocidade=65, 
            src_imagem='images/poseidon.png'
        ))