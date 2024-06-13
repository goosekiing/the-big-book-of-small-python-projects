"""It rolls N dice one million times then displays the percentage chance of each sum"""

import os
import random

DIE_N_SIDES = 6
DICES_PER_ROLL = 2
ROLLS = 1000000 #one million

def main()-> None:
    """Main execution function"""
    clear_terminal()
    n_dices = DICES_PER_ROLL
    n_sides = DIE_N_SIDES
    results = {}
    for i in range(n_dices, (n_dices*n_sides)+1):
        results[i] = 0
    print(f"\nIniciando a rolagem de {n_dices}d{n_sides} {ROLLS} vezes.\n")
    for i in range(1, ROLLS+1):
        if i % (ROLLS/(100/10)) == 0:
            print(f"{int(i/(ROLLS)*100):3d}% dos dados rolados")
        total = 0
        for _ in range(n_dices):
            total += random.randint(1,n_sides)
        results[total] += 1

    max_len_rolls_string = len(str(max(results.values()))) if len(str(max(results.values()))) > len("ROLLS") else len("ROLLS")

    print("\nRESULTS:\n\n" + "SUM | " + "ROLLS".ljust(max_len_rolls_string, ' ') + " | PERCENTAGE")
    for face_sum, frequencie in results.items():
        print(f"{str(face_sum).ljust(3, ' ')} | {str(frequencie).ljust(max_len_rolls_string, ' ')} | {frequencie/ROLLS*100:5.2f}%")

def clear_terminal() -> None:
    """Clears the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n-------|-----|-------\nExecução Interrompida\n-------|-----|-------\n")
