"""Implementação de um temporizador de contagem regressiva usando uma exibição de sete segmentos no terminal."""

import os
import time
import calendar
from sevseg import getSevSegStr

BOMB_EXPLOSION = """
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
"""

def main()-> None:
    """Main execution function"""

    clear_terminal()

    print("Defina as horas, minutos e segundos para iniciar o timer.")
    hours = request_number("\nHoras (máx 23)", 23)
    minutes = request_number("\nMinutos (máx 59)", 59)
    seconds = request_number("\nSegundos (máx 59)", 59)

    start_timer(hours, minutes, seconds)

def request_number(text: str, max_n: int, min_n: int = 0)-> int :
    """Prints a message with the text in the 'text' variable and returns the number the user has typed.\nIf the number is not in the limits, it keeps asking the user to type a number.\n'max_n' and 'min_n' are inclusive"""
    while True:
        res = input(text + "\n> ")
        if res.isdecimal() and min_n <= int(res) <= max_n:
            return int(res)

def start_timer(hours: int, minutes: int, seconds:int)-> None:
    """Prints the running timer in the terminal"""
    time_structure = time.strptime(f"1970-{hours}-{minutes}-{seconds}", "%Y-%H-%M-%S")
    total_secs = calendar.timegm(time_structure)
    
    while total_secs >= 0:
        clear_terminal()

        hours_rows = getSevSegStr(time_structure.tm_hour,2).splitlines()
        minutes_rows = getSevSegStr(time_structure.tm_min,2).splitlines()
        seconds_rows = getSevSegStr(time_structure.tm_sec,2).splitlines()

        print(f"{hours_rows[0]}   {minutes_rows[0]}   {seconds_rows[0]}")
        print(f"{hours_rows[1]} • {minutes_rows[1]} • {seconds_rows[1]}")
        print(f"{hours_rows[2]} • {minutes_rows[2]} • {seconds_rows[2]}")

        total_secs -= 1
        time_structure = time.gmtime(total_secs)
        time.sleep(0.5)

    clear_terminal()
    print(BOMB_EXPLOSION)

def clear_terminal() -> None:
    """Clears the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_terminal()
        print("\n-------|-----|-------\nExecução Interrompida\n-------|-----|-------\n")
