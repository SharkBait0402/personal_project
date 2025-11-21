import pygame
import sys
import random
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
    true_colors = ["red", "green", "blue", "yellow"]

    speed = 0

    score = 0

    guessing_time = False
    display_list = pygame.event.custom_type()

    start = False
    count = 0
    score = 0

    starting_box = random.randint(0,3)
    winning = [starting_box]

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == display_list:
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                for color in winning:

                    pygame.draw.rect(screen, true_colors[color], boxes[color])
                    pygame.display.flip()

                    pygame.time.delay(1000)

                    pygame.draw.rect(screen, "black", boxes[color])
                    pygame.display.flip()

                    pygame.time.delay(250)

                pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                print("select the boxes in the order they appeared")

                guessing_time = True
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    start = start_pressed(start_button)
                    if guessing_time:
                        collide = collide_logic(boxes[0], boxes[1], boxes[2], boxes[3])
                        speed = 0
                        colors = collide[0]
                        picked_box = collide[1]


                        if count == (len(winning) - 1):
                            guessing_time = False
                            winning.append(random.randint(0,3))
                            count = 0
                            score += 1
                            print(f'score: {score}')
                            pygame.time.set_timer(display_list, 1000, loops = 1)
                            continue



                        if picked_box == winning[count]:
                            count += 1
                        else:
                            print(f"you lose\nscore: {score}")
                            sys.exit()
                        speed = 0
                    else:
                        print("press the green button to start the round")




        screen.fill((75,75,75))

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
        
        pygame.draw.rect(screen, (46, 143, 37), start_button)

        speed += 1

        if speed == 15:
            colors = ["black", "black", "black", "black"]
            speed = 0

        pygame.display.flip()

        dt = clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
