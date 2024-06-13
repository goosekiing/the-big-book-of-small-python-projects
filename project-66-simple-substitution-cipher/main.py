"""DESCREPTION"""

import os
import random
import pyperclip

CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,!? "

def main()-> None:
    """Main execution function"""
    clear_terminal()
    print("Gerador de mensagem cifrada iniciado.\nPara interromper o programa aperte 'Ctrl-C a qualquer momento'\n")
    while True:
        while True:
            response = input("Deseja (c)ifrar ou (d)ecifrar uma mensagem?\n> ").lower().strip()
            if response in ["c", "d"]:
                encrypt = True if response == "c" else False
                break

        key = get_random_key(CHARACTERS) if encrypt else request_key()
        message = input("\nDigite a mensagem:\n> ").upper().strip()
        translation = translate_message(message, key, encrypt)

        print(f"\nSua mensagem é:\n{translation}\n")
        copy_key_and_translation(key, translation, encrypt)
        input("Aperte 'enter' para continuar.\n")
        print("-"*25+"|"+"-"*15+"|"+"-"*25+"\n")

def get_random_key(characters: str) -> str:
    "Returns a string containig the characters in a random order"
    key = list(characters)
    random.shuffle(key)
    key = "".join(key)
    print("\nSua chave é: ", key)
    return key

def request_key() -> str:
    """Keeps asking the user to enter a type a valid key"""
    while True:
        key = input("\nDigite a chave para decifrar a mensagem:\n> ")
        if all(char in CHARACTERS for char in key):
            if len(key) == len(CHARACTERS):
                return key

def translate_message(message: str, key: str, encrypt: bool = True) -> str:
    """Returns a string containing the encrypted or decrypted message. If encrypt = True, it encrypts the message. If encrypt = False, it decrypts the message."""
    chars_a, chars_b = (CHARACTERS, key) if encrypt else (key, CHARACTERS)
    response = []
    for char in message:
        if char in chars_a:
            response.append(chars_b[chars_a.index(char)])
        else:
            response.append(char)
    response = "".join(response)
    return response

def copy_key_and_translation(key:str, translation: str, encrypt: bool)->None:
    if encrypt:
        try:
            pyperclip.copy(f"Chave:\n{key}\n\nMensagem:\n{translation}")
            print("A chave e a mensagem foram copiadas para área de transferencia.")
        except:
            print("Não foi possível copiar a chave e a mensagem para área de transferencia.")

def clear_terminal() -> None:
    """Clears the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n-------|-----|-------\nExecução Interrompida\n-------|-----|-------\n")
