"""Calculates numbers of the Fibonacci sequence"""

import os

def main()-> None:
	"""Main execution function"""
	clear_terminal()
	while True:
		n = input("Digite quantos elementos da sequencia de Fibonacci deseja calcular:\n> ")
		if n.isdecimal() and int(n)>=3:
			n = int(n)
			break
	fib = [0, 1, 1]
	while len(fib) < n:
		fib.append(fib[-1]+fib[-2])
	fib_str = []
	for number in fib:
		fib_str.append(f"{number:,}".replace(",", "."))
	fib_str = ", ".join(fib_str)
	print(fib_str)

def clear_terminal() -> None:
	"""Clears the terminal."""
	os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\n-------|-----|-------\nExecução Interrompida\n-------|-----|-------\n")
