import pygame

def main():

    pygame.init()
    WIDTH = 1280
    HEIGHT = 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


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

        color1 = "black"

        pygame.draw.rect(screen, color1, box1)
        pygame.draw.rect(screen, "black", box2)
        pygame.draw.rect(screen, "black", box3)
        pygame.draw.rect(screen, "black", box4)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()

        if box1.collidepoint(mouse_pos[0], mouse_pos[1]):
            color1 = "red"
            mouse_pos = (0, 0)
            print("collision detected")

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
