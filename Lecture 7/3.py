import pygame
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Circle")
ball_color = pygame.Color('red')
background = pygame.Color('white')
ball_gr = [400, 300]
ball_radius = 25
speed = 20
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_gr[1] = max(ball_gr[1] - speed, ball_radius)
    if keys[pygame.K_DOWN]:
        ball_gr[1] = min(ball_gr[1] + speed, size[1] - ball_radius)
    if keys[pygame.K_LEFT]:
        ball_gr[0] = max(ball_gr[0] - speed, ball_radius)
    if keys[pygame.K_RIGHT]:
        ball_gr[0] = min(ball_gr[0] + speed, size[0] - ball_radius)
    
    screen.fill(background)
    pygame.draw.circle(screen, ball_color, ball_gr, ball_radius)
    pygame.display.flip()
    pygame.time.Clock().tick(24)