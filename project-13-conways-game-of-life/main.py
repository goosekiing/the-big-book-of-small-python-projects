"""O "Jogo da Vida", conhecido como "Game of Life" em inglês, é um modelo matemático onde células em uma grade evoluem segundo regras simples: sobrevivência com dois ou três vizinhos vivos, morte por solidão ou superpopulação e reprodução com três vizinhos vivos. É um exemplo de autômato celular e tem aplicações em computação e matemática recreativa."""

import os
import random
from time import sleep
from copy import deepcopy
from typing import Dict, Tuple

ALIVE = "•"
DEAD = " "
WIDTH = 120
HIGHT = 25

def main() -> None:
    """Main execution function."""
    cells: Dict[Tuple[int, int], str] = {}
    get_random_cells(cells)

    while True:
        print_cells(cells)
        get_new_cells_state(cells)
        sleep(0.3)

def get_random_cells(cells:dict)->None:
    """Generates random dead and alive cells"""
    for y in range(HIGHT):
        for x in range(WIDTH):
            if random.choice([True, False]):
                cells[(x,y)]=ALIVE
            else:
                cells[(x,y)]=DEAD

def print_cells(cells:dict)->None:
    clear_terminal()
    for y in range(HIGHT):
        for x in range(WIDTH):
            print(cells[(x,y)],end="")
        print()

def get_new_cells_state(cells:dict) -> None:
    cells_current_state = deepcopy(cells)
    for y in range(HIGHT):
        for x in range(WIDTH):
            right = (x+1) % WIDTH
            left  = (x-1) % WIDTH
            up    = (y-1) % HIGHT
            down  = (y+1) % HIGHT

            alive_neighbors = 0
            for y_cell in [up, y, down]:
                for x_cell in [left, x, right]:
                    if x_cell == x and y_cell == y:
                        continue
                    elif cells_current_state[(x_cell, y_cell)] == ALIVE:
                        alive_neighbors += 1

            if cells[(x,y)] == ALIVE:
                if alive_neighbors <= 1 or alive_neighbors >= 4:
                    cells[(x,y)] = DEAD
            elif cells[(x,y)] == DEAD and alive_neighbors == 3:
                cells[(x,y)] = ALIVE

def clear_terminal() -> None:
    """Clears the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n-------|-----|-------\nExecução Interrompida\n-------|-----|-------\n")
