import pygame, sys
diff = int(input("input how fast you want the game 60 to infinity"))
pygame.init()
screen = pygame.display.set_mode((600, 200))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Dino
dino = pygame.Rect(50, 140, 30, 30)
vel = 0
ground = 170

# Cactus
cactus = pygame.Rect(600, 140, 20, 30)
speed = 6

score = 0
game_over = False

while True:
    clock.tick(diff)
    screen.fill((255, 255, 255))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            if game_over:
                cactus.x = 600
                score = 0
                game_over = False
            elif dino.bottom == ground:
                vel = -15

    if not game_over:
        # Jump physics
        vel += 1
        dino.y += vel
        if dino.bottom >= ground:
            dino.bottom = ground
            vel = 0

        # Move cactus
        cactus.x -= speed
        if cactus.right < 0:
            cactus.left = 600

        # Collision = death
        if dino.colliderect(cactus):
            game_over = True

        score += 1

    # Draw
    pygame.draw.line(screen, (0,0,0), (0, ground), (600, ground))
    pygame.draw.rect(screen, (0,0,0), dino)
    pygame.draw.rect(screen, (0,0,0), cactus)

    screen.blit(font.render(f"Score: {score}", True, (0,0,0)), (10, 10))

    if game_over:
        text = font.render("GAME OVER - PRESS SPACE", True, (0,0,0))
        screen.blit(text, (200, 90))

    pygame.display.update()

