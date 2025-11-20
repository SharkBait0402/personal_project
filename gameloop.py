import sys

winning_list = [1, 2, 3, 4]
pressed_boxes = []


def gameloop():
    for box in winning_list:
        if box == pressed:
            continue
        else:
            print("you lose")
            sys.exit()
