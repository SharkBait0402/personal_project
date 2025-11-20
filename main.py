import pygame
from boxes import collide_logic

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

    delay = pygame.event.custom_type()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    colors = collide_logic(box1, box2, box3, box4)
                    speed = 0





        screen.fill("gray")

        square_outer_dim = (HEIGHT) / 2
        top = (HEIGHT/2) - square_outer_dim/2
        left = (WIDTH/2) - square_outer_dim
        gap = 5

        mouse_pos = (0, 0)

        box1 = pygame.Rect(left, top, square_outer_dim, square_outer_dim)
        box2 = pygame.Rect((left + square_outer_dim + gap), top, square_outer_dim, square_outer_dim)
        box3 = pygame.Rect(left, (top + square_outer_dim + gap), square_outer_dim, square_outer_dim)
        box4 = pygame.Rect((left + square_outer_dim + gap), (top + square_outer_dim + gap), square_outer_dim, square_outer_dim)


        pygame.draw.rect(screen, colors[0], box1)
        pygame.draw.rect(screen, colors[1], box2)
        pygame.draw.rect(screen, colors[2], box3)
        pygame.draw.rect(screen, colors[3], box4)

        speed += 1

        if speed == 15:
            colors = ["black", "black", "black", "black"]
            speed = 0

        pygame.display.flip()

        dt = clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
