"""An animation of a deep cave that goes forever into the earth"""

import random
import os
from time import sleep

WIDTH = 120
STARTING_GAP = 20

def main() -> None:
    """Main execution function"""
    clear_terminal()
    gap = STARTING_GAP
    left = int(((WIDTH-2)/2)+(gap/2))

    while True:
        print("#" + (" "*gap).rjust(left, "#").ljust(WIDTH-2, "#") + "#")
        left += get_zero_plus_or_minus_one()
        gap += get_zero_plus_or_minus_one()
        if gap <= 0:
            gap += 1
        if (left + gap) > (WIDTH-2):
            gap -= 1
            left -= 1
        elif gap>left:
            gap -= 1
            left += 1
        sleep(0.02)

def get_zero_plus_or_minus_one()->int:
    """Randomly returns -1, 0 or 1"""
    return random.choice([-1, 0, 1])

def clear_terminal() -> None:
    """Clears the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_terminal()
        print("\n-------|-----|-------\nExecução Interrompida\n-------|-----|-------\n")