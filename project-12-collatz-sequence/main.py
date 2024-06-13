"""A sequência de Collatz é uma série de números onde você começa com qualquer número inteiro positivo e segue duas regras simples: se o número é par, divida-o por 2; se for ímpar, multiplique por 3 e some 1. A questão ainda não respondida é se, não importa o número inicial escolhido, essa sequência sempre termina em 1. Essa é uma pergunta em aberto na matemática."""

import os
import random

def main()-> None:
    clear_terminal()
    while True:

        print("Digite o número referente a opção que voce deseja:")
        print("1. Vizualizar o passo-a-passo da sequencia de Collatz\n2. Gerar números aleatórios e calcular o numero de iterações na sequencia de Collatz")
        while True:
            action = input("> ").strip().lower()
            if action in ["1", "2"]:
                break
        
        if action == "1":
            vizualize_collatz_sequence()
        else:
            generate_n_random_numbers_for_collatz_sequence()

        sair = input("\nDigite 'sair' para interromper ou aperte 'enter' para voltar ao menu inicial\n> ")
        print()
        if sair in ["s", "sair"]:
            print("\n-------|-----|-------\nExecução Finalizada\n-------|-----|-------\n")
            break

def vizualize_collatz_sequence() -> None:
    """Asks for a number and prints in the terminal the loops of the Collatz Sequence necessary for this number to reach 1"""
    while True:
        n = input("\nDigite um número maior que 1 para aplicar a sequencia de Collatz:\n> ")
        if n.isdecimal() and int(n)>1:
            n = int(n)
            break
    
    i = 0
    starting_n = n
    print("\nnumber:".ljust(16) + "|" + " operation:".ljust(20) + "|" + " new number:".ljust(15))
    while n > 1:
        i += 1
        if n%2 == 0:
            print(f"{int(n)}".ljust(15) + "|"+ f" {int(n)} / 2".ljust(20) + "| ", end="")
            n /= 2
            print(int(n))
        else:
            print(f"{int(n)}".ljust(15) + "|"+ f" ({int(n)} * 3) + 1".ljust(20) + "| ", end="")
            n = (n * 3) + 1
            print(int(n))
    print(f"\nForam necessários {i} loops para o número {starting_n} chegar no número 1 utilizando a Sequencia de Collatz")

def generate_n_random_numbers_for_collatz_sequence() -> None:
    """Generates and prints in the terminal random numbers and how many loops of Collatz Sequence are necessary to reach 1"""
    
    while True:
        n_max = input("\nDigite o valor máximo que um numero aleatório gerado pode assumir:\n> ")
        if n_max.isdecimal() and int(n_max)>1:
            n_max = int(n_max)
            break
    
    while True:
        n_loops = input("Digite quantos número aleatórios deseja gerar (máx 25):\n> ")
        if n_loops.isdecimal() and 1<=int(n_loops)<=25:
            n_loops = int(n_loops)
            break

    print("\nLoops para chegar no 1:  | Number:")
    for _ in range(n_loops):
        i = 0
        n = random.randint(2,n_max)
        starting_n = n
        while n > 1:
            i += 1
            if n%2 == 0:
                n /= 2
            else:
                n = (n * 3) + 1
        print(f"{i}".ljust(25)+f"| {starting_n}")

def clear_terminal() -> None:
    """Clears the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n-------|-----|-------\nExecução Interrompida\n-------|-----|-------\n")