import pygame



def collide_logic(box1, box2, box3, box4):

    colors = ["black", "black", "black", "black"]

    mouse_pos = pygame.mouse.get_pos()

    if box1.collidepoint(mouse_pos[0], mouse_pos[1]):
        colors[0] = "red"
        speed = 0
        mouse_pos = (0, 0)
        print("collision detected")
    elif box2.collidepoint(mouse_pos[0], mouse_pos[1]):
        colors[1] = "green"
        speed = 0
        mouse_pos = (0, 0)
        print("collision detected")
    elif box3.collidepoint(mouse_pos[0], mouse_pos[1]):
        colors[2] = "blue"
        speed = 0
        mouse_pos = (0, 0)
        print("collision detected")
    elif box4.collidepoint(mouse_pos[0], mouse_pos[1]):
        colors[3] = "yellow"
        speed = 0
        mouse_pos = (0, 0)
        print("collision detected")
    return colors


