import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame 01")
running = True
sara = pygame.image.load("sara/sara-cal1.png")
clock = pygame.time.Clock()
while running: #gAME lOOP
    clock.tick(60)
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont("Arial", 30)
    text = font.render(f"{clock.get_fps():.2f}", True, (0, 0, 0))
    screen.blit(sara, (50, 50))
    screen.blit(text, (300, 230))
    pygame.display.update()
    
pygame.quit()