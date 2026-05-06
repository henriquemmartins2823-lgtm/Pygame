# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((900, 700))
pygame.display.set_caption('Donkey Kong Remastered (VERSÃO INSPER)')

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((200, 0, 0))  # Preenche com a cor branca
    cor=(245,73,49)
    posicao=[(0,600), (0,500), (900,600), (900,500)]
    pygame.draw.polygon(window,cor,posicao)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  #

