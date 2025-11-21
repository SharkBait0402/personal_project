import pygame



def collide_logic(box0, box1, box2, box3):

    colors = ["black", "black", "black", "black"]

    mouse_pos = pygame.mouse.get_pos()

    if box0.collidepoint(mouse_pos[0], mouse_pos[1]):
        change_colors(0, colors)
        speed = 0
        mouse_pos = (0, 0)
        print("collision detected")
    elif box1.collidepoint(mouse_pos[0], mouse_pos[1]):
        change_colors(1, colors)
        speed = 0
        mouse_pos = (0, 0)
        print("collision detected")
    elif box2.collidepoint(mouse_pos[0], mouse_pos[1]):
        change_colors(2, colors)
        speed = 0
        mouse_pos = (0, 0)
        print("collision detected")
    elif box3.collidepoint(mouse_pos[0], mouse_pos[1]):
        change_colors(3, colors)
        speed = 0
        mouse_pos = (0, 0)
        print("collision detected")
    return colors

def start_pressed(button):
    mouse_pos = pygame.mouse.get_pos()

    if button.collidepoint(mouse_pos[0], mouse_pos[1]):
        return True
    return False

def change_colors(box_num, colors):
    if box_num == 0:
        color = "red"
    if box_num == 1:
        color = "green"
    if box_num == 2:
        color = "blue"
    if box_num == 3:
        color = "yellow"

    colors[box_num] = color
    return

def cycle_list(key, colors, screen, boxes):
    for color in key:
        change_colors(color, colors)
        pygame.draw.rect(screen, colors[color], boxes[color])
        pygame.time.delay(250)
    return

def show_red():
    pass


