"""Vamos jogar Blackjack?"""

# imports:
import random
import os
from typing import Union

# constants:
HEARTS = chr(9829)
DIAMONDS = chr(9830)
CLUBS = chr(9827)
SPADES = chr(9824)
STARTING_STACK = 1000
REGRAS = """---------------|-----|---------------

Bem Vinde! Vamos jogar Black Jack!

---------------|-----|---------------

As resgras são:
Você deve tentar conseguir 21 pontos ou o mais perto disso. Mas se ultrapassar 21 VOCÊ PERDE!
J, Q e K valem 10 pontos cada
Cada ÁZ pode valer 1 ou 11 pontos, o que for mais vantajoso

Voce recebe duas cartas no início e pode escolher:
(P) Pedir - Você receberá mais uma carta.
(F) Ficar - Você NÃO receberá mais cartas.
(D) Dobrar - Disponível só na primeira rodada. Você dobra a aposta e recebe SÓ MAIS UMA CARTA.

Ao fim comparamos quem chegou mais perto de 21 sem estourar, você ou o Dealer.
Vamos jogar?
"""

def main():
    """função principal de execução do jogo"""
    clear_terminal()
    
    stack = STARTING_STACK

    print(REGRAS)

    while True:
        if stack == 0:
            print(f"\n---------------|-----|---------------\nPERDEU TUDO! Você começou com ${STARTING_STACK} e terminou com ${stack}.\nMais sorte na próxima vez\n---------------|-----|---------------\n")
            break
        
        bet = get_bet(stack)
        if bet is False:
            break

        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]
        turn = 1
            
        while get_hand_value(player_hand) <= 21:
            print_hands(dealer_hand, player_hand)
            action = get_player_action(turn, stack, bet)
            turn += 1

            if action == "D":
                bet = bet*2
                player_hand.append(deck.pop())
                if get_hand_value(player_hand) <= 21:
                    print_hands(dealer_hand, player_hand)
                    break

            if action == "P":
                player_hand.append(deck.pop())

            if action == "F":
                break

        if get_hand_value(player_hand) <= 21:
            while True:
                if get_hand_value(dealer_hand) < 17:
                    input("\npressione enter para o dealer realizar a jogada dele.")
                    dealer_hand.append(deck.pop())
                    print_hands(dealer_hand, player_hand, False)
                
                else:
                    input("\npressione enter para o dealer realizar a jogada dele.")
                    print_hands(dealer_hand, player_hand, True)
                    break
            
            if get_hand_value(player_hand) > get_hand_value(dealer_hand):
                print(f"\n-----|---|-----\nVocê ganhou ${bet}!\n-----|---|-----\n")
                stack += bet
            
            elif get_hand_value(player_hand) == get_hand_value(dealer_hand):
                print(f"\n-----|---|-----\nVocê e o dealer empataram!\nVocês dividem o pote de ${bet}.\nVocê ganha{int(bet/2)}\n-----|---|-----\n")
                stack += int(bet/2)
            
            else: 
                print(f"\n-----|---|-----\nVocê perdeu ${bet}!\n-----|---|-----\n")
                stack -= bet
        
        else:
            print_hands(dealer_hand, player_hand, True)
            print(f"\n-----|---|-----\nSua mão estourou 21 pts!\nVocê perdeu ${bet}!\n-----|---|-----\n")
            stack -= bet
    
def get_deck() -> list:
    """função para gerar um baralho, embaralhado de forma aleatória, com total de 52 cartas e 4 naipes"""
    deck = [(rank, suit) for suit in (HEARTS, DIAMONDS, CLUBS, SPADES) for rank in [n for n in range(2,11)]+["J", "Q", "K", "A"]]
    random.shuffle(deck)
    return deck

def get_hand_value(cards:list) -> int:
    """função que retorna o número de pontos de uma lista da cartas"""
    hand_value = 0
    n_aces = 0

    if cards:
        for card in cards:
            if card[0] in ["J", "Q", "K"]:
                hand_value += 10
            elif card[0] == "A":
                hand_value += 1
                n_aces += 1
            else:
                hand_value += card[0]
        
        for _ in range(n_aces):
            if (hand_value + 10) <= 21:
                hand_value += 10
    
    return hand_value

def print_cards(cards:list, actor: Union[None, str] = None, pts: Union[None, int, str] = None):
    """função com a logica para vizualização das cartas e da pontuação"""
    rows = ["", "", "", ""]
    for card in cards:
        rows[0] += (" ___  " )
        rows[1] += (f"|{str(card[0]).ljust(2, ' ')} | ")
        rows[2] += (f"| {card[1]} | ")
        rows[3] += (f"|_{str(card[0]).rjust(2, '_')}| ")
    
    if actor and pts:
        rows[2] += f"Mão do {actor}: {pts}pts."

    for row in rows:
        print(row)

def print_hands(dealer_hand: list, player_hand: list, show_dealer_first_card:bool = False):
    """função que imprime as mão do dealer e do jogador com suas respectivas pontuações"""
    dealer_points = get_hand_value(dealer_hand)
    player_points = get_hand_value(player_hand)
    if show_dealer_first_card == False:
        print_cards([("#", "#")]+dealer_hand[1:], "Dealer", "##")
    else:
        print_cards(dealer_hand, "Dealer", dealer_points)

    print_cards(player_hand, "Jogador", player_points)

def get_bet(stack: int) -> int:
    """função para controlar o as apostas do jogador"""
    while True:
        bet = input(f"Quanto você quer apostar?\nSeu stack atual é de ${stack} (digite QUIT para sair)\n> ")
        if bet.upper().strip() == "QUIT":
            if stack == STARTING_STACK:
                print(f"\n---------------|-----|---------------\nVocê começou com ${STARTING_STACK} e terminou com os mesmos ${stack}. Ficou no zero a zero.\nObrigado por jogar.\n---------------|-----|---------------\n")
                pass
            elif stack > STARTING_STACK:
                print(f"\n---------------|-----|---------------\nParabéns, você começou com {STARTING_STACK} e terminou com {stack}.\nNo total você ganhou ${stack-STARTING_STACK}!\nTe aguardamos na próxima.\n---------------|-----|---------------\n")
            else:
                print(f"\n---------------|-----|---------------\nQue azar, você começou com {STARTING_STACK} e terminou com {stack}.\nNo total você perdeu ${STARTING_STACK-stack}.\nMais sorte na próxima vez\n---------------|-----|---------------\n")
            return False
        
        elif not bet.isdecimal():
            continue
        elif 0 < int(bet) <= stack:
            return int(bet)

def get_player_action(turn: int, stack: int, bet: int):
    """função para capturar a ação do jogador"""
    while True:
        if turn == 1 and stack/bet >= 2:
            action = input("\nO que deseja fazer?\n(P) Pedir | (F) Ficar | (D) Dobrar\n> ").strip().upper()
            if action in ["P", "F", "D"]:
                return action
        else:
            action = input("\nO que deseja fazer?\n(P) Pedir | (F) Ficar\n> ").strip().upper()
            if action in ["P", "F"]:
                return action

def clear_terminal() -> None:
    """Clears the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
