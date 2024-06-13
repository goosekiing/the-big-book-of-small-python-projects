
"""Break Caeser Cipher with Brute Force Atack"""
import sys
import os

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main() -> None:
    """main execution function"""
    clear_terminal()
    while True:

        sentence = input("\nDigite a mensagem cifrada:\n> ").upper()
        print()
        
        for key in range(len(SYMBOLS)):
            char_keeper = []
            for char in sentence:
                if char in SYMBOLS:
                    i = (SYMBOLS.find(char) + key) % len(SYMBOLS)
                    char_keeper.append(SYMBOLS[i])
                else:
                    char_keeper.append(char)
            message = "".join(char_keeper)
            print(f"{key+1:02d}. {message}")

def clear_terminal() -> None:
    """Clears the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExecução interrompida")
        sys.exit()
