import pygame

def main():

    pygame.init()
    WIDTH = 1280
    HEIGHT = 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    color1, color2, color3, color4 = "black", "black", "black", "black"

    speed = 0

    delay = pygame.event.custom_type()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if box1.collidepoint(mouse_pos[0], mouse_pos[1]):
                        color1 = "red"
                        speed = 0
                        mouse_pos = (0, 0)
                        print("collision detected")



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


        pygame.draw.rect(screen, color1, box1)
        pygame.draw.rect(screen, color2, box2)
        pygame.draw.rect(screen, color3, box3)
        pygame.draw.rect(screen, color4, box4)

        speed += 1

        if speed == 20:
            color1, color2, color3, color4 = "black", "black", "black", "black"
            speed = 0

        pygame.display.flip()

        dt = clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
