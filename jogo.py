import pygame
from sys import exit

def personagem1_animacao():
    global indice_personagem
    indice_personagem += 0.10
    if indice_personagem > len(personagem1_parado) -1:
        indice_personagem = 0

    tela.blit(personagem1_parado[int(indice_personagem)], personagem1_retangulo)

def personagem2_animacao():
    global indice_personagem
    indice_personagem += 0.10
    if indice_personagem > len(personagem2_parado) -1:
        indice_personagem = 0

    personagem2_parado_invertido = pygame.transform.flip(personagem2_parado[int(indice_personagem)], True, False)

    tela.blit(personagem2_parado_invertido, personagem2_retangulo)

# Executa o pygame
pygame.init()

# Indica o tamanho da tela
tamanho = (1300, 680)
tela = pygame.display.set_mode(tamanho)

# Coloca o título da janela
pygame.display.set_caption("RAPIDO NO GATILHO")

# Coloca o plano de fundo
fundo = pygame.image.load('assets/Fundo/bamboo bridge.png')

# Transforma a imagem
fundo = pygame.transform.scale(fundo, tamanho)

# Carrega as imagens do personagem1
indice_personagem = 0
personagem1_parado = []
personagem1_atirando = []
personagem1_morte = []

for imagem in range(1, 11):
    img = pygame.image.load(f'assets/Personagem1/parado/Gun_Idle{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (220, 220))
    personagem1_parado.append(img)

personagem1_retangulo = personagem1_parado[indice_personagem].get_rect(center = (150, 370))

# Carrega as imagens do personagem2
personagem2_parado = []
personagem2_atirando = []
personagem2_morte = []

for imagem in range(1, 11):
    img = pygame.image.load(f'assets/Personagem2/parado/Gun_Idle{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (220, 220))
    personagem2_parado.append(img)

    personagem2_retangulo = personagem2_parado[indice_personagem].get_rect(center = (1150, 378))


# Controla o fps
fps = pygame.time.Clock()

while True:
    # EVENTOS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Carrega a imagem de fundo
    tela.blit(fundo, (0, 0))

    personagem1_animacao()

    personagem2_animacao()

    # Atualiza o conteúdo
    pygame.display.update()

    # Quantidade de frames por segundo
    fps.tick(60)