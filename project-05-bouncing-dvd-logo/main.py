"""Simulation of the DVD logo bouncing on the screen"""

from sys import exit, stdout
from time import sleep
import random
import bext

N_LOGOS = 5
FRAME_TIME = 0.1
COLORS = ["red", "green", "yellow", "blue", "purple", "cyan", "white"]
WIDTH = bext.size()[0]-1
HEIGHT = bext.size()[1]-1

# directions:
UP_RIGHT = "ur"
UP_LEFT = "ul"
DOWN_RIGHT = "dr"
DOWN_LEFT = "dl"
DIRECTIONS = [UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT]

# dictionary keys:
COLOR = "color"
X = "x"
Y = "y"
DIRECTION = "direction"

def main() -> None:
    bext.clear()
    word = input("Type the word you want to see bouncing:\n> ").strip().upper()
    word_len = len(word) +1
    
    bext.clear()

    words_config = []
    for _ in range(N_LOGOS):
        words_config.append({
            COLOR: random.choice(COLORS),
            X: random.randint(1, WIDTH-word_len),
            Y: random.randint(1, HEIGHT-1),
            DIRECTION: random.choice(DIRECTIONS)
            })

    while True:
        for config in words_config:
            bext.goto(config[X], config[Y])
            print(" "*word_len, end="")

            loop_initial_direction = config[DIRECTION]

            # control corners:
            if config[X] <= 1 and config[Y] <= 0:
                config[DIRECTION] = DOWN_RIGHT
            elif config[X] <= 1 and config[Y] >= HEIGHT:
                config[DIRECTION] = UP_RIGHT
            elif config[X] >= WIDTH-word_len and config[Y] >= HEIGHT:
                config[DIRECTION] = UP_LEFT
            elif config[X] >= WIDTH-word_len and config[Y] <= 0:
                config[DIRECTION] = DOWN_LEFT

            # control right edge:
            elif config[X] >= WIDTH-word_len and config[DIRECTION] == DOWN_RIGHT:
                config[DIRECTION] = DOWN_LEFT
            elif config[X] >= WIDTH-word_len and config[DIRECTION] == UP_RIGHT:
                config[DIRECTION] = UP_LEFT

            # control left edge:
            elif config[X] <= 1 and config[DIRECTION] == DOWN_LEFT:
                config[DIRECTION] = DOWN_RIGHT
            elif config[X] <= 1 and config[DIRECTION] == UP_LEFT:
                config[DIRECTION] = UP_RIGHT

            # control top edge:
            elif config[Y] <= 0 and config[DIRECTION] == UP_LEFT:
                config[DIRECTION] = DOWN_LEFT
            elif config[Y] <= 0 and config[DIRECTION] == UP_RIGHT:
                config[DIRECTION] = DOWN_RIGHT

            # control bottom edge:
            elif config[Y] >= HEIGHT and config[DIRECTION] == DOWN_LEFT:
                config[DIRECTION] = UP_LEFT
            elif config[Y] >= HEIGHT and config[DIRECTION] == DOWN_RIGHT:
                config[DIRECTION] = UP_RIGHT
            
            # control directions
            if config[DIRECTION] == UP_RIGHT:
                config[X] += 2
                config[Y] -= 1
            elif config[DIRECTION] == UP_LEFT:
                config[X] -= 2
                config[Y] -= 1
            elif config[DIRECTION] == DOWN_RIGHT:
                config[X] += 2
                config[Y] += 1
            elif config[DIRECTION] == DOWN_LEFT:
                config[X] -= 2
                config[Y] += 1

            if config[DIRECTION] != loop_initial_direction:
                config[COLOR] = random.choice(COLORS)

        for config in words_config:
            bext.goto(config[X], config[Y])
            bext.fg(config[COLOR])
            print(word, end="")

        stdout.flush()
        bext.goto(0,0)
        sleep(FRAME_TIME)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        bext.goto(0,HEIGHT)
        bext.fg("white")
        print("Animation interrupted")
        exit()
