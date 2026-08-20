import pygame

pygame.init()

window = pygame.display.set_mode((512, 512))
pygame.display.set_caption("Football Game")

clock = pygame.time.Clock()

green = (0, 247, 66)
blue = (0, 0, 255)

player_width = 50
player_height = 70

player_x = 50
player_y = 200

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player_x -= 5

    if keys[pygame.K_d]:
        player_x += 5

    if keys[pygame.K_w]:
        player_y -= 5

    if keys[pygame.K_s]:
        player_y += 5

    if player_x < 0:
        player_x = 0

    if player_x > 512 - player_width:
        player_x = 512 - player_width

    if player_y < 0:
        player_y = 0

    if player_y > 512 - player_height:
        player_y = 512 - player_height

    window.fill(green)

    pygame.draw.rect(
        window,
        blue,
        (player_x, player_y, player_width, player_height)
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
