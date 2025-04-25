import pygame

pygame.init()

width = 360
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lights Out Demo")

room1 = pygame.image.load("THE DOORWAY.png")
room2 = pygame.image.load("THE HOURGLASS.png")
room3 = pygame.image.load("THE FISHBOWL.png")
room4 = pygame.image.load("THE OVENSPACE.png")
room5 = pygame.image.load("THE TREELINE.png")
room6 = pygame.image.load("THE REFRIGERATOR.png")
room7 = pygame.image.load("THE PILLOWLAND.png")
currentRoom = room1
EXIT = 0
bulb = pygame.Rect(130, 0, 150, 150)
door = pygame.Rect(90, 90, 200, 400)
key1 = pygame.image.load("Clock (H).png")
key2 = pygame.image.load("Fish (O).png")
key3 = pygame.image.load("Violin (P).png")
key4 = pygame.image.load("Icecube (R).png")
key5 = pygame.image.load("Star (F).png")
key6 = pygame.image.load("Ladder (T).png")
key7 = pygame.image.load("Key (D).png")
image = key1
item = image.get_rect(center=(width // 2, height // 2))
dragged_item = None
offset_x = 0
offset_y = 0

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
                    door = pygame.Rect(145, 145, 90, 90)
                elif bulb.collidepoint(mouse_pos) and currentRoom == room2:
                    currentRoom = room3
                    door = pygame.Rect(0, 145, 360, 400)
                elif bulb.collidepoint(mouse_pos) and currentRoom == room3:
                    currentRoom = room4
                    door = pygame.Rect(0, 340, 360, 300)
                elif bulb.collidepoint(mouse_pos) and currentRoom == room4:
                    currentRoom = room5
                    door = pygame.Rect(50, 90, 300, 400)
                elif bulb.collidepoint(mouse_pos) and currentRoom == room5:
                    currentRoom = room6
                    door = pygame.Rect(50, 145, 280, 200)
                elif bulb.collidepoint(mouse_pos) and currentRoom == room6:
                    currentRoom = room7
                    door = pygame.Rect(80, 160, 90, 180)
                elif bulb.collidepoint(mouse_pos) and currentRoom == room7:
                    currentRoom = room1
                    door = pygame.Rect(90, 90, 200, 400)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if item.collidepoint(event.pos):
                    dragged_item = item
                    offset_x = item.x - event.pos[0]
                    offset_y = item.y - event.pos[1]
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragged_item = None
        if event.type == pygame.MOUSEMOTION:
            if dragged_item is not None:
                dragged_item.x = event.pos[0] + offset_x
                dragged_item.y = event.pos[1] + offset_y
    if item.colliderect(door) and image == key1 and currentRoom == room2:
        image = key2
        room2 = pygame.image.load("THE HOURGLASS solved.png")
        currentRoom = room2
    elif item.colliderect(door) and image == key2 and currentRoom == room4:
        image = key3
        room4 = pygame.image.load("THE OVENSPACE solved.png")
        currentRoom = room4
    elif item.colliderect(door) and image == key3 and currentRoom == room7:
        image = key4
        room7 = pygame.image.load("THE PILLOWLAND solved.png")
        currentRoom = room7
    elif item.colliderect(door) and image == key4 and currentRoom == room6:
        image = key5
        room6 = pygame.image.load("THE REFRIGERATOR solved.png")
        currentRoom = room6
    elif item.colliderect(door) and image == key5 and currentRoom == room3:
        image = key6
        room3 = pygame.image.load("THE FISHBOWL solved.png")
        currentRoom = room3
    elif item.colliderect(door) and image == key6 and currentRoom == room5:
        image = key7
        room5 = pygame.image.load("THE TREELINE solved.png")
        currentRoom = room5
    elif item.colliderect(door) and image == key7 and currentRoom == room1: 
        item = pygame.Rect(0, 0, 0, 0)
        room1 = pygame.image.load("THE DOORWAY solved.png")
        currentRoom = room1
        EXIT = 1
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if door.collidepoint(mouse_pos) and currentRoom == room1 and EXIT == 1:
                running = False
                print("Congratulations, You win the Demo")
    screen.blit(currentRoom, (0, 0))
    screen.blit(image, item)
    overlay = pygame.Surface((400, 500), pygame.SRCALPHA)
    pygame.draw.rect(overlay, (0, 0, 0, 128), bulb)
    pygame.draw.rect(overlay, (0, 0, 0, 128), door)
    pygame.display.flip()

pygame.quit()
