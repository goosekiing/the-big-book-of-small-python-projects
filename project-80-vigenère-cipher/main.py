"""VIGENÈRE CIPHER"""

import os
try:
    import pyperclip
except ImportError:
    print("Não foi possível importar a biblioteca 'pyperclip'")

CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,!?ÁÉÍÓÚÂÊÎÔÛÀÃÕ"

def main()-> None:
    """Main execution function."""
    clear_terminal()
    print("Gerador de mensagem cifrada iniciado.\nPara interromper o programa aperte 'Ctrl-C' a qualquer momento")
    while True:
        encrypt = request_encryption_or_decrytion()
        key = request_key(encrypt).upper()
        message = input("\nDigite a mensagem:\n> ").upper()
        translation = translate_message(message=message, key=key, encrypt=encrypt)
        display_and_copy_translation(translation, encrypt)

def request_encryption_or_decrytion()->bool:
    """Asks the user if he wants to encrypt or decrypt a message. Returns True for encrypt and False for decrypt"""
    while True:
        res = input("\nVocê deseja (c)ifrar ou (d)ecifrar a mensagem?\n> ").lower()
        if res in ["c", "d"]:
            encrypt = True if res == "c" else False
            return encrypt

def request_key(encrypt:bool)->str:
    """Asks the user to enter a key and returns a string containig it."""
    cifrar_ou_decifrar = "cifrar" if encrypt else "decifrar"
    while True:
        key = input(f"\nDigite uma chave válida para {cifrar_ou_decifrar} a mensagem:\n> ").upper().replace(" ", "")
        if validate_key(key, CHARACTERS):
            return key

def validate_key(key:str, valid_characters: str)->bool:
    """Asks the user to enter a key and returns a string containig it."""
    for char in key:
        if char not in valid_characters:
            return False
    return True

def translate_message(message:str, key:str, encrypt:bool)->str:
    """Returns a string containing the encrypted or decrypted message. If encrypt = True, it encrypts the message. If encrypt = False, it decrypts the message."""
    translation = []
    for i, char in enumerate(message):
        if char in CHARACTERS:
            index_key = CHARACTERS.find(key[i%len(key)]) + 1
            char_index = CHARACTERS.find(char)
            translated_char_index = (char_index + index_key) if encrypt else (char_index - index_key)
            translated_char = CHARACTERS[translated_char_index%len(CHARACTERS)]
            translation.append(translated_char)
        else:
            translation.append(char)
    return "".join(translation)

def display_and_copy_translation(translation:str, encrypt:bool)->None:
    """Prints the translated message in the terminal and copies it to the copyboard if the user wants to"""
    cifrada_ou_decifrada = "cifrada" if encrypt else "decifrada"
    print(f"\nA mensagem {cifrada_ou_decifrada} é:\n{translation}")
    res = input(f"\nDigite 'c' para copiar a mensagem {cifrada_ou_decifrada} para área de trasnferencia ou aperte 'enter' para continuar.\n> ").lower()
    if res == "c":
        try:
            pyperclip.copy(translation)
            print(f"Mensagem {cifrada_ou_decifrada} copiada para a área de transferencia com sucesso.")
        except:
            print(f"Não foi possível copiar a mensagem {cifrada_ou_decifrada} para a área de transferencia.")

def clear_terminal() -> None:
    """Clears the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n-------|-----|-------\nExecução Interrompida\n-------|-----|-------\n")
