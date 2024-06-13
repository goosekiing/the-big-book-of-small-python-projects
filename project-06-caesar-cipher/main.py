"""Caeser Cipher"""
import sys
import os
try:
    import pyperclip
except ImportError:
    print("Não foi possível importar a biblioteca pyperclip")

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main() -> None:
    """main execution function"""
    clear_terminal()
    while True:
        while True:
            action = input("\nDigite 'c' para cifrar uma mensagem ou 'd' para decifrar:\n> ").upper()
            if action in ["C", "D"]:
                break
            

        while True:
            key = input(f"\nDefina um número de 0 a {len(SYMBOLS)-1} para deslocar a mensagem:\n> ")
            if key.isdecimal() and 0<=int(key)<len(SYMBOLS):
                key = int(key)
                break

        sentence = input("\nDigite a mensagem:\n> ").upper()
        char_keeper = []

        if action == "C":
            for char in sentence:
                if char in SYMBOLS and action=="C":
                    i = (SYMBOLS.find(char) + key) % len(SYMBOLS)
                    char_keeper.append(SYMBOLS[i])
                else:
                    char_keeper.append(char)
            message = "".join(char_keeper)
            print("\nMensagem cifrada:\n", message)

        elif action == "D":
            for char in sentence:
                if char in SYMBOLS and action=="D":
                    i = (SYMBOLS.find(char) - key) % len(SYMBOLS)
                    char_keeper.append(SYMBOLS[i])
                else:
                    char_keeper.append(char)
            message = "".join(char_keeper)
            print("\nMensagem decifrada:\n", message)

        copy = input("\nDeseja copiar a mensagem? digite 's' para sim ou enter para não\n> ").upper()
        if copy == "S":
            try:
                pyperclip.copy(message)
                print("\nMensagem copiada com sucesso")
            except:
                print("\nInfelizmente não foi possível copiar a mensagem.")

def clear_terminal() -> None:
    """Clears the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExecução interrompida")
        sys.exit()
