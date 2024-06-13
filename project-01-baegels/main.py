"""Jogo de adivinhar a senha"""

import random
import os

# Define o número de digitos a serem buscados
DIGITS = 3
TURNS = 10

def main():
    """função principal de execução do jogo"""
    clear_terminal()

    while True:

        secret_number = get_secret_number()
        attempt = 1

        print("Descrição do jogo")

        while True:
            
            print(f"tentativa n. {attempt}:")
            guess = str(input("> "))
            if number_validator(guess):
                print(get_clues(guess, secret_number))
                attempt += 1
                if guess == secret_number:
                    break
                if attempt > TURNS:
                    print(f"Que pena, você perdeu. O número secreto era {secret_number}")
                    break
            else:
                print(f"o numero deve ter {DIGITS} digitos e eles não podem ser repetidos. tente novamente")

        if not input("\nQuer jogar de novo?\nDigite 's' para sim ou 'n' para não\n> ").lower().startswith("s"):
            print("Obrigado por jogar!")
            break

def get_secret_number() -> str:
    """Gerador do numero secreto"""
    numbers = list(range(10))
    numbers = random.sample(numbers, DIGITS)
    secret_number = ""
    for n in numbers:
        secret_number = secret_number + str(n)
    return secret_number

def number_validator(guess:str) -> bool:
    """validaçao do numero digitado pelo usuario"""
    if len(guess) == DIGITS == len(set(guess)):
        validos = [str(n) for n in range(10)]
        guess = list(guess)
        for i in guess:
            if i not in validos:
                return False
        return True
    return False

def get_clues(guess:str, secret_number:str) -> str:
    """Gera pistas para ajudar o jogador a adivinhar o número secreto"""
    clues = []
    if guess == secret_number:
        return("Parabéns! Você acertou!")
    else:
        for guess_digit, secret_digit in zip(guess, secret_number):
            if guess_digit == secret_digit:
                clues.append("-!- ")
            elif guess_digit in secret_number:
                clues.append("-?- ")
            else:
                clues.append("-X- ")
    clues.sort()
    return(''.join(clues).strip())

def clear_terminal() -> None:
    """Clears the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
