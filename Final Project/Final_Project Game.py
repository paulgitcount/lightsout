# A dark rooms with 7 environments
# THE DOORWAY : A Clock (H)
# THE HOURGLASS : A Fish (O)
# THE FISHBOWL : Violin (P)
# THE OVENSPACE :  An Ice Cube (R)
# THE TREELINE : A Star (F)
# THE REFRIGERATOR : Ladder (T)
# THE PILLOWLAND : A Key (D)

import pygame

pygame.init()

width = 360
height = 500
screen = pygame.display.set_mode((width, height))

room1 = pygame.image.load("THE DOORWAY.png")
room2 = pygame.image.load("THE HOURGLASS.png")
room3 = pygame.image.load("THE FISHBOWL.png")
room4 = pygame.image.load("THE OVENSPACE.png")
room5 = pygame.image.load("THE TREELINE.png")
room6 = pygame.image.load("THE REFRIGERATOR.png")
room7 = pygame.image.load("THE PILLOWLAND.png")
currentRoom = room1
bulb = pygame.Rect(130, 0, 150, 150)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if bulb.collidepoint(mouse_pos) and currentRoom == room1:
                    currentRoom = room2
                elif bulb.collidepoint(mouse_pos) and currentRoom == room2:
                    currentRoom = room3
                elif bulb.collidepoint(mouse_pos) and currentRoom == room3:
                    currentRoom = room4
                elif bulb.collidepoint(mouse_pos) and currentRoom == room4:
                    currentRoom = room5
                elif bulb.collidepoint(mouse_pos) and currentRoom == room5:
                    currentRoom = room6
                elif bulb.collidepoint(mouse_pos) and currentRoom == room6:
                    currentRoom = room7
                elif bulb.collidepoint(mouse_pos) and currentRoom == room7:
                    currentRoom = room1
    screen.blit(currentRoom, (0, 0))
    #pygame.draw.rect(screen, (248, 171, 166), bulb)
    overlay = pygame.Surface((400, 500), pygame.SRCALPHA)
    pygame.draw.rect(overlay, (0, 0, 0, 128), bulb)  # Black with 50% opacity
    pygame.display.flip()

pygame.quit()




















