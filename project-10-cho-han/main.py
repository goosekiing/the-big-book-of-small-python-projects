"""Cho-Han é um jogo de dados japonês onde os jogadores apostam se o total dos pontos de dois dados será par (Cho) ou ímpar (Han)"""

import os
import random
from time import sleep

JAPANESE_NUMBERS = {1: "一 Ichi (1)", 2: "二 Ni (2)", 3: "三 San (3)", 4: "四 Yon (4)", 5: "五 Go (5)", 6: "六 Roku (6)"}
STARTING_STACK = 1000
DEALER_CUT = 0.1

def main() -> None:
    clear_terminal()
    print(f"Cho-Han é um jogo de dados japonês onde os jogadores apostam se o total dos pontos de dois dados será par (Cho) ou ímpar (Han). Você começa com ${STARTING_STACK}. Se voce perder, perde toda a aposta. Se ganhar o Dealer fica com {DEALER_CUT*100:.0f}% da sua aposta\n\n--- Para sair do jogo aperte 'Ctrl + C' a qualquer momento ---")
    stack = STARTING_STACK
    while True:
        bet = get_bet(stack)
        pot = int(bet * (1-DEALER_CUT))
        print("\nRolando os dados")
        print("...")
        sleep(1)
        n_1, n_2 = (random.randint(1,6), random.randint(1,6))
        while True:
            action = input("\nDigite 'Cho' (par) ou 'Han' (ímpar) para apostar qual será a soma dos dados\n> ").strip().lower()
            if action in ["cho", "c"]:
                action = "even"
                break
            elif action in ["han", "h"]:
                action = "odd"
                break
        print(f"\nSeus dados são: {JAPANESE_NUMBERS[n_1]} e {JAPANESE_NUMBERS[n_2]}")

        is_even = (n_1+n_2)%2 == 0
        if is_even:
            right_answer = "even"
        else:
            right_answer = "odd"
        win = action == right_answer
        
        if win:
            stack += pot
            print(f"\nVocê ganhou ${pot}! Seu stack atual agora é de ${stack}.")
        else:
            stack -= bet
            print(f"\nVocê perdeu ${bet}! Seu stack atual agora é de ${stack}.")

        if stack <= 0:
            print("Você perdeu tudo! Mais sorte na próxima vez")
            break

def get_bet(stack:int) -> int:
    """Returns an int with the bet's value"""
    while True:
        bet = input(f"\nQuanto deseja apostar? Seu stack atual é de ${stack}.\n> ")
        if bet.isdecimal() and 1<= int(bet) <= stack:
            return int(bet)

def clear_terminal() -> None:
    """Clears the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n-------|-----|-------\nExecução Interrompida\n-------|-----|-------\n")
