"""Gerador aleatorio de aniversários para calcular em um grupo de n pessoas, qual a probabilidade de pelo menos duas fazerem aniversario no mesmo dia"""

import datetime
import random
import os

def main():
    """funçao principal"""
    clear_terminal()
    print("""\n\n
------------------------------|--------------------|------------------------------\n
A ideia desse código é testar a probabilidade de ter pelo menos duas pessoas que
fazem aniversário no mesmo dia em um grupo de n pessoas.\n
------------------------------|--------------------|------------------------------""")
    while True:
        while True:
            n_birthdays = input("\nDefina um numero de 2 a 100 para gerar 'n' datas de aniversario aleatórias:\n> ")
            if n_birthdays.isdecimal() and 2 <= int(n_birthdays) <= 100:
                n_birthdays = int(n_birthdays)
                break
        birthdays = birthdays_generator(n_birthdays)
        print(f"\nAs {n_birthdays} datas aleatórias geradas são:")
        print_birthdays(birthdays)
        repeated_birthdays = get_matched_birthdays(birthdays)
        print(f"Das {n_birthdays} datas aleatórias, as datas repetidas são:")
        print_birthdays(repeated_birthdays)
        
        print(f"""------------------------------|--------------------|------------------------------\n
Agora vamos gerar 100.000 vezes {n_birthdays} datas aleatórias e verificar em
quantas dessas vezes vamos ter pelos menos duas datas iguais\n
------------------------------|--------------------|------------------------------\n""")
        input("Pressione enter para iniciar\n")
        loops = 100000
        repeat_count = 0
        for i in range(loops):
            birthdays = birthdays_generator(n_birthdays)
            if there_is_repeated_birthdays(birthdays):
                repeat_count += 1 
            if i%(loops/10) == 0:
                print(f"{int(i/loops*100):03d}% concluido")
        print("100% concluído")
        print(f"""\n------------------------------|--------------------|------------------------------\n
Haviam datas repetidas em {repeat_count/loops*100:.2f}% das 100.000 vezes em que foram geradas {n_birthdays} datas.\n
------------------------------|--------------------|------------------------------\n""")

        again = input("Quer brincar novamente? Digite 's' para sim ou 'n' para não.\n> ")
        if not again == "s".lower():
            break

def birthdays_generator(n_birthdays:int) -> list:
    """função para gerar uma lista com aniversarios aleatórios"""
    birthdays = []
    initial_date = datetime.date(2000,1,1)
    for _ in range(n_birthdays):
        random_birthday = initial_date + datetime.timedelta(random.randint(0,365))
        birthdays.append(random_birthday)
    return birthdays

def there_is_repeated_birthdays(birthdays:list) -> bool:
    return False if len(birthdays) == len(set(birthdays)) else True

def get_matched_birthdays(birthdays:list) -> list:
    """função para retornar umas lista com os aniversarios repetidos"""
    if not there_is_repeated_birthdays(birthdays):
        return None
    else:
        counter = {}
        repeated_birthdays = []
        for birthday in birthdays:
            if birthday not in counter:
                counter[birthday] = 1
            else:
                counter[birthday] += 1
    
    for birthday, count in counter.items():
        if count > 1:
            repeated_birthdays.append(birthday)
    
    repeated_birthdays.sort()
    return repeated_birthdays

def print_birthdays(birthdays_list: list):
    """função para imprimir as datas no formato '01 de Jan'"""
    MONTHS = ["_", "Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    if birthdays_list:
        birthdays_print_list = []
        for i, birthday in enumerate(birthdays_list):
            birthdays_print_list.append(f"{birthday.day:02d} de {MONTHS[birthday.month]} | ")
        print("".join(birthdays_print_list)[:-3],"\n")
    else:
        print("Não tem aniversários em datas repetidas\n")

def clear_terminal() -> None:
    """Clears the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
