"""Projeto onde o usuario digita uma mensagem e é retornado um mapa bitmap com o a mensagem do usuario """

import os

BITMAP= """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""

def main():
    """função principal"""
    clear_terminal()

    while True:
        message = input("Digite a mensagem para aparecer no mapa: \n> ")
        if len(message.strip())>0:
            break

    for line in BITMAP.splitlines():
        for i, char in enumerate(line):
            if char == " ":
                print(" ", end="")
            else:
                print(message[i%len(message)], end="")
        print()

def clear_terminal() -> None:
    """Clears the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
