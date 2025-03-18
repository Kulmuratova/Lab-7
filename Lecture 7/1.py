import pygame
import time
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickey Mouse Clock")
main_clock = pygame.transform.scale(pygame.image.load("mickeyclock.png"), (800, 600))
right_hand = pygame.image.load("right_hand.png")
left_hand = pygame.image.load("left_hand.png")
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    min_angle = (minutes * 6 + (seconds / 60) * 6) 
    sec_angle = seconds * 6  
    screen.blit(main_clock, (0, 0))

    rotated_right = pygame.transform.rotate(pygame.transform.scale(right_hand, (800, 600)), -min_angle)
    right_rect = rotated_right.get_rect(center=(800 // 2, 600 // 2 + 12))
    screen.blit(rotated_right, right_rect)
    rotated_left =  pygame.transform.rotate(pygame.transform.scale(left_hand, (40.95, 682.5)), -sec_angle)
    left_rect = rotated_left.get_rect(center=(800 // 2, 600 // 2 + 10))
    screen.blit(rotated_left, left_rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()