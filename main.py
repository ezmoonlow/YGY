import pygame 

W = 800
H = 600
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 60)
kx = 375
gg = 1

pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Всяка')




font = pygame.font.SysFont('Arial', 61, True, False)
font2 = pygame.font.SysFont('Arial', 41, True, False)





run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
    screen.fill(BLUE)
    screen.blit(font.render("Всем привет", True, WHITE), (210, 260))
    screen.blit(font2.render("задание на урок", True, YELLOW), (240, 340))
    surf = pygame.Surface((50, 50))
    surf.fill((200, 0, 0))
    screen.blit(surf, (kx, 200))
    if gg == 1:
        kx = kx + 0.1
    if kx == 850:
        kx = 1
    pygame.display.update()            
