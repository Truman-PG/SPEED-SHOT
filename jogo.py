import pygame
from sys import exit
from time import sleep

def personagem1_animacao_parado():
    global indice_personagem
    indice_personagem += 0.10
    if indice_personagem > len(personagem1_parado) - 1:
        indice_personagem = 0

    tela.blit(personagem1_parado[int(indice_personagem)], personagem1_retangulo)

def personagem1_animacao_atirando():
    global indice_personagem

    indice_personagem += 0.10

    if indice_personagem > len(personagem1_atirando) - 1:
        indice_personagem = 0

    tela.blit(personagem1_atirando[int(indice_personagem)], personagem1_retangulo)

def tiro_perso1():
    global velocidade

    retangulo_tiro.x += velocidade

    if retangulo_tiro.x < 0:
        retangulo_tiro.x += velocidade

    tela.blit(tiro, retangulo_tiro)

def tiro_perso2():
    global velocidade
    if retangulo_tiro2.x > 0:
        retangulo_tiro2.x -= velocidade

    tela.blit(tiro,retangulo_tiro2)
    
def personagem2_animacao_parado():
    global indice_personagem
    indice_personagem += 0.10
    if indice_personagem > len(personagem2_parado) - 1:
        indice_personagem = 0

    personagem2_parado_invertido = pygame.transform.flip(personagem2_parado[int(indice_personagem)], True, False)

    tela.blit(personagem2_parado_invertido, personagem2_retangulo)

def personagem2_animacao_atirando():
    global indice_personagem
    indice_personagem += 0.10

    if indice_personagem > len(personagem2_atirando) - 1:
        indice_personagem = 0

    personagem2_atirando_invertido = pygame.transform.flip(personagem2_atirando[int(indice_personagem)], True, False)
    
    tela.blit(personagem2_atirando_invertido, personagem2_retangulo)

def personagem2_animacao_morte():
    global indice_personagem
    indice_personagem += 0.10
    if indice_personagem > len(personagem2_morte) - 1:
        indice_personagem = 0

    personagem2_morte_invertido = pygame.transform.flip(personagem2_parado[int(indice_personagem)], True, False)

    tela.blit(personagem2_morte_invertido, personagem2_retangulo)

def mostra_empate():
    empate = pygame.image.load('assets/Empate/imagem_empate.png').convert_alpha()
    empate = pygame.transform.scale(empate, (500, 500))
    tela.blit(empate, (400, 150))
    
def mostra_texto():
    global contador_segundos

    fonte = pygame.font.Font(None, 60)
    tempo_texto = fonte.render(f"TEMPO: {contador_segundos}", True, (255, 255, 255))

    tela.blit(tempo_texto, (545, 250))


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

# Personagem 1 parado
for imagem in range(1, 11):
    img = pygame.image.load(f'assets/Personagem1/parado/Gun_Idle{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (220, 220))
    personagem1_parado.append(img)

# Personagem 1 atirando
for imagem in range(1, 11):
    img = pygame.image.load(f'assets/Personagem1/atirando/Gun_Attack{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (220, 220))
    personagem1_atirando.append(img)


personagem1_retangulo = personagem1_parado[indice_personagem].get_rect(center=(150, 370))

# Carrega as imagens do personagem2
personagem2_parado = []
personagem2_atirando = []
personagem2_morte = []

# Personagem 2 parado
for imagem in range(1, 11):
    img = pygame.image.load(f'assets/Personagem2/parado/Gun_Idle{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (220, 220))
    personagem2_parado.append(img)

# Personagem 2 atirando
for imagem in range(1, 11):
    img = pygame.image.load(f'assets/Personagem2/atirando/2Gun_Attack{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (220, 220))
    personagem2_atirando.append(img)

# Personagem 2 morte
for imagem in range(1, 11):
    img = pygame.image.load(f'assets/Personagem2/morte/Rambo_Die{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (220, 220))
    personagem2_morte.append(img)

personagem2_retangulo = personagem2_parado[indice_personagem].get_rect(center=(1150, 378))

# Tempo(cronometro)
tempo_evento = pygame.USEREVENT + 1
tempo_ms = 500
pygame.time.set_timer(tempo_evento, tempo_ms)

contador_segundos = 0

# Número de apertos da tecla
tecla_a = 0
tecla_l = 0

# Pega a imagem do tiro
velocidade = 8
tiro = pygame.image.load('assets/Tiro/Imagem/Bullet.png').convert_alpha()
tiro = pygame.transform.scale(tiro, (40, 40))

# Retangulo do tiro personagem 1
retangulo_tiro = tiro.get_rect(center=(300, 420))

# Retangulo do tiro personagem 2
retangulo_tiro2 = tiro.get_rect(center=(1000, 420))

# Controla o fps
fps = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if evento.type == tempo_evento:
            contador_segundos += 1

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                if contador_segundos < 10: tecla_a += 1
        
            if evento.key == pygame.K_l:
                if contador_segundos < 10: tecla_l += 1

    # Carrega a imagem de fundo
    tela.blit(fundo, (0, 0))

    if contador_segundos >= 10:
        if tecla_a > tecla_l:
            personagem1_animacao_atirando()

            personagem2_animacao_parado()

            tiro_perso1()
        elif tecla_a < tecla_l:
            personagem2_animacao_atirando()

            personagem1_animacao_parado()

            tiro_perso2()

        else:
            mostra_empate()
    else:    
        personagem1_animacao_parado()

        personagem2_animacao_parado()


    
    mostra_texto()

    # Atualiza o conteúdo
    pygame.display.update()

    # Quantidade de frames por segundo
    fps.tick(60)