import pygame

W = 800
H = 600
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
NAVY = (0, 0, 128)

pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('текст')
screen.fill(NAVY)
pygame.display.flip()
pygame.mouse.set_visible(False)

font = pygame.font.SysFont('Arial', 96, True, False)
font2 = pygame.font.SysFont('Arial', 48, True, False)
font_box = pygame.Surface((W - 30, font.get_height()))
font2_box = pygame.Surface((W - 30, font.get_height()))

text = font.render("Всем привет", True, WHITE)
screen.blit(text, (100, 200))
text = font2.render("с вами джокер виктор дудка", True, YELLOW)
screen.blit(text, (70, 300))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False


    pygame.display.update()
