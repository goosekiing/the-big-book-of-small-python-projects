"""DESCREPTION"""

import os

STARTING_NUMBER = 0
TOTAL_NUMBERS = 100

def main()-> None:
    """Main execution function"""
    clear_terminal()
    for decimal in range(STARTING_NUMBER, STARTING_NUMBER + TOTAL_NUMBERS):
        hex_n = hex(decimal)
        bin_n = bin(decimal)
        print(f"DEC: {decimal} | HEX: {hex_n[2:]} | BIN: {bin_n[2:]}")

def clear_terminal() -> None:
    """Clears the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n-------|-----|-------\nExecução Interrompida\n-------|-----|-------\n")
