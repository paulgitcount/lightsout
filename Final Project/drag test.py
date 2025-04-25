import pygame
pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Example")

image = pygame.image.load("Clock (H).png")
background = pygame.image.load("THE DOORWAY.png")
room = background
item = image.get_rect(center=(width // 2, height // 2))
dragged_item = None
offset_x = 0
offset_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if item.collidepoint(event.pos):
                    dragged_item = item
                    offset_x = item.x - event.pos[0]
                    offset_y = item.y - event.pos[1]
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragged_item = None
        elif event.type == pygame.MOUSEMOTION:
            if dragged_item is not None:
                dragged_item.x = event.pos[0] + offset_x
                dragged_item.y = event.pos[1] + offset_y
    if item.colliderect(pygame.Rect(100,100,100,100)):
        image = pygame.image.load("Fish (O).png")
        background = pygame.image.load("THE DOORWAY solved.png")
        room = background
    screen.blit(image, item)
    screen.blit(room, (0, 0))
    #overlay = pygame.image.load("Clock (H).png")
    #pygame.draw.rect(screen, (0,0,0), item)
    pygame.draw.rect(screen, (0,255,0), (100,100,100,100), 2)
    pygame.display.flip()
##background = pygame.image.load("THE DOORWAY.png")
##running = True
##while running:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            running = False
##        if event.type == pygame.MOUSEBUTTONDOWN:
##            background = pygame.image.load("THE DOORWAY solved.png")
##    screen.blit(background, (0, 0))
##    pygame.display.flip()
pygame.quit()
