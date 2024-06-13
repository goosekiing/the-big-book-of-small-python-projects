"""Generates a month calendar of a given year and month"""

from typing import Union
import datetime
import os
import sys

MONTHS = ["_", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
WEEKDAYS = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB", "DOM"]

def main() -> None:
    """Main execution function"""
    clear_terminal()
    while True:
        year, month = get_year_and_month()
        calendar = get_calendar(year=year, month=month)
        print(calendar)
        res = input("Deseja salvar o calendário em um arquivo txt?\nDigite 'salvar' para salvar ou aperte 'enter' para continuar:\n> ")
        if res.lower().strip() in ["s", "salvar"]:
            save_calendar(calendar, year, month)
        del year, month
        res = input("Digite um novo ano entre 1582 e 9999 para gerar um novo calendário ou 'sair' para sair:\n> ")
        if res.lower().strip() in ["s", "sair"]:
            print("\n-------|-----|-------\nExecução Finalizada\n-------|-----|-------\n")
            sys.exit()
        else:
            year = int(res) if res.isdecimal() else None

def get_year_and_month(year: Union[None, int] = None) -> tuple:
    """Returns a tuple containig the year and the month"""
    if not (str(year).isdecimal() and 1582 <= year <= 9999):
        while True:
            res = input("\nDigite o ano (entre 1582 e 9999):\n> ")
            if res.isdecimal() and 1582 <= int(res) <= 9999:
                year = int(res)
                break
    max_month = 12 if year < 9999 else 11
    while True:
        res = input(f"Digite o mês (entre 1 e {max_month}):\n> ")
        if res.isdecimal() and 1 <= int(res) <= max_month:
            month = int(res)
            del res
            break
    return (year, month)

def get_calendar(year: int, month: int) -> str:
    """Returns a string containing the calendar"""
    calendar = "\n"
    top_line = "+----------"*7+"+"
    empty_row = "|          "*7+"|"

    date = datetime.date(year, month, 1)
    while date.weekday() != 6:
        date -= datetime.timedelta(days=1)

    calendar_name = f"{MONTHS[month]} do ano {year}"
    calendar += (calendar_name.rjust(int(len(calendar_name)/2+39)).ljust(78)) + "\n\n"
    for weekday in WEEKDAYS:
        calendar += ("|" + f"{weekday}".rjust(6).ljust(10))
    calendar += "|" 
    while True:
        calendar += "\n" + top_line + "\n"
        for _ in range(7):
            if date.month == month:
                calendar += (f"| {str(date.day).ljust(9,' ')}")
            else:
                calendar += ("|          ")
            date += datetime.timedelta(days=1)
        calendar += "|\n" + empty_row + '\n' + empty_row
        if date.month != month:
            break
    calendar += "\n" + top_line + "\n"
    return calendar

def save_calendar(calendar: str, year: int, month:int) -> None:
    """Creates a txt file containing the calendar"""
    file_path = "project-08-calendar-maker\\txt-calendars\\"
    file_name = f"{year}-{month:02d}.txt"
    with open(file=(file_path+file_name), mode="w", encoding="utf-8") as txt:
        txt.write(calendar)
    print(f"arquivo {file_name} salvo com sucesso.\n")

def clear_terminal() -> None:
    """Clears the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n-------|-----|-------\nExecução Interrompida\n-------|-----|-------\n")
