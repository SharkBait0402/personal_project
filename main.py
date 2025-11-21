import pygame
from boxes import collide_logic, start_pressed, cycle_list

def main():

    pygame.init()
    WIDTH = 1280
    HEIGHT = 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    colors = ["black", "black", "black", "black"]

    speed = 0

    score = 0

    guessing_time = pygame.event.custom_type()
    display_list = pygame.event.custom_type()

    start = False

    winning = [0, 1, 2, 3]

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == display_list:
                cycle_list(winning, colors, screen, boxes)
                speed = 0
                print("displaying list")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    colors = collide_logic(boxes[0], boxes[1], boxes[2], boxes[3])
                    start = start_pressed(start_button)
                    speed = 0




        screen.fill("gray")

        square_outer_dim = (HEIGHT) / 2
        top = (HEIGHT/2) - square_outer_dim/2
        left = (WIDTH/2) - square_outer_dim
        gap = 5

        mouse_pos = (0, 0)

        boxes = [None , None, None, None]
        boxes[0]= pygame.Rect(left, top, square_outer_dim, square_outer_dim)
        boxes[1] = pygame.Rect((left + square_outer_dim + gap), top, square_outer_dim, square_outer_dim)
        boxes[2] = pygame.Rect(left, (top + square_outer_dim + gap), square_outer_dim, square_outer_dim)
        boxes[3] = pygame.Rect((left + square_outer_dim + gap), (top + square_outer_dim + gap), square_outer_dim, square_outer_dim)

        start_width = square_outer_dim / 2
        start_height = start_width / 2
        start_left = WIDTH/2 - (start_width / 2)
        start_top = 950
        start_button = pygame.Rect(start_left, start_top, start_width, start_height)

        if start:
            start = False
            pygame.event.post(pygame.event.Event(display_list))
            



        pygame.draw.rect(screen, colors[0], boxes[0])
        pygame.draw.rect(screen, colors[1], boxes[1])
        pygame.draw.rect(screen, colors[2], boxes[2])
        pygame.draw.rect(screen, colors[3], boxes[3])
        
        pygame.draw.rect(screen, "darkgreen", start_button)

        speed += 1

        if speed == 15:
            colors = ["black", "black", "black", "black"]
            speed = 0

        pygame.display.flip()

        dt = clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
