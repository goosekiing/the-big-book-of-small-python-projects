"""Este módulo contém a função getSevSegStr() para gerar representações de números em um display de sete segmentos. Ele é útil para projetos que envolvem a exibição de números de forma visualmente simples, como relógios digitais ou contadores."""

from typing import Union

def getSevSegStr(number: Union[str, int, float], n_digits: int = 0) -> str:
    """Returns a string representing a numerical display. The represntation will be filed with zeros if the number lenght is smaller than 'n_digits'"""

    if type(number) not in [str, int, float]:
        raise TypeError(f"{number} is not a valid object. The number must be a 'str', 'int' or 'float'")

    number = str(number).zfill(n_digits)
    rows = ['', '', '']
    for i, digit in enumerate(number):

        if digit not in "-.0123456789":
            raise ValueError(f"{number} is not a valid object. The parameter must contain only numbers")

        if digit == ".":
            rows[0] += " "
            rows[1] += " "
            rows[2] += "."
            continue
        elif digit == "-":
            rows[0] += "  "
            rows[1] += "__"
            rows[2] += "  "
        elif digit == "0":
            rows[0] += " __ "
            rows[1] += "|  |"
            rows[2] += "|__|"
        elif digit == "1":
            rows[0] += "    "
            rows[1] += "   |"
            rows[2] += "   |"
        elif digit == "2":
            rows[0] += " __ "
            rows[1] += " __|"
            rows[2] += "|__ "
        elif digit == "3":
            rows[0] += " __ "
            rows[1] += " __|"
            rows[2] += " __|"
        elif digit == "4":
            rows[0] += "    "
            rows[1] += "|__|"
            rows[2] += "   |"
        elif digit == "5":
            rows[0] += " __ "
            rows[1] += "|__ "
            rows[2] += " __|"
        elif digit == "6":
            rows[0] += " __ "
            rows[1] += "|__ "
            rows[2] += "|__|"
        elif digit == "7":
            rows[0] += " __ "
            rows[1] += "   |"
            rows[2] += "   |"
        elif digit == "8":
            rows[0] += " __ "
            rows[1] += "|__|"
            rows[2] += "|__|"
        elif digit == "9":
            rows[0] += " __ "
            rows[1] += "|__|"
            rows[2] += " __|"

        if i < len(number)-1:
            rows[0] += " "
            rows[1] += " "
            rows[2] += " "

    return "\n".join(rows)
