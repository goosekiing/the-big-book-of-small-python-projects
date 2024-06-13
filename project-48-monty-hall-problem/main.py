"""DESCREPTION"""

import os
import random

TOTAL_OPTIONS = 3
OPTIONS_N_DROPS = TOTAL_OPTIONS - 2
N_LOOPS = 1000

def main()-> None:
    """Main execution function"""
    clear_terminal()
    hits_no_changing = make_selection(False)
    hits_changing = make_selection(True)
    print(hits_no_changing, hits_changing)

def make_selection(change:bool)->int:
    """Returns the number of hits for randomly choosing an option. You can or can't chage the option after the first selection"""
    hits = 0
    for _ in range(N_LOOPS):
        options = ["X" for x in range(TOTAL_OPTIONS-1)]+["C"]
        random.shuffle(options)
        choice = random.choice(options)
        for _ in range (OPTIONS_N_DROPS):
            options.remove("X")
        if change:
            if options.index(choice) == 0:
                choice = options[1]
            else:
                choice = options[0]
        if choice == "C":
            hits +=1
    return hits

def clear_terminal() -> None:
    """Clears the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n-------|-----|-------\nExecução Interrompida\n-------|-----|-------\n")
