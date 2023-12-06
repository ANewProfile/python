import random
from time import sleep

def make_board(solution):
	board = ''
	for character in solution:
		if character == ' ':
			board += ' '
		else:
			board += '-'
	return board

def spin_wheel(possibilities):
	for i in range(1, 31):
		# print(i)
		print(random.choice(possibilities))
		sleep(i/120)
	amount = random.choice(possibilities)
	
	return amount

def guess_letter(letter, solution, board):
	board = list(board)
	list_solution = list(solution)
	print(list_solution)
	for character in list_solution:
		if letter == character:
			board[list_solution.index(letter)] = letter
			continue
		else:
			continue

	board = ''.join(board)
	return board

def main():
	bank = 0
	input('Press enter when you\'re ready to start: ')
	possible_answers = ['an apple a day keeps the doctor away', 'the quick brown fox jumps over the lazy dog']
	answer = 'an apple a day keeps the doctor away'
	# answer = random.choice(possible_answers)
	board = make_board(answer)
	print(board)
	possible_spins = ['bankrupt', 600, 400, 300, 800, 350, 450, 700, 300, 600, 2500, 'bankrupt', 300, 600, 300, 500, 800, 550, 400, 300, 900, 1500, 500, 900]
	while True:
		spin = None
		turn = input('Would you like to [s]pin, [b]uy a  vowel, or solve the [p]uzzle? ')
		if turn.lower() == 's':
			spin = spin_wheel(possible_spins)
			if spin == 'bankrupt':
				bank = 0
				print('Bankrupt!')
				continue
			print(f'{spin}!')
			while True:
				guess = input('Enter the consonant you would like to guess: ').lower()
				if guess in ['a', 'e', 'i', 'o', 'u']:
					print('No vowels please!')
					guess = None
				elif len(guess) > 1 or len(guess) < 1:
					print('Only one letter please!')
					guess = None
				elif guess not in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']:
					print('Only letters in the English alphabet please!')
					guess = None
				else:
					newboard = guess_letter(guess, answer, board)
					print(newboard)
					if newboard != board:
						bank += spin
						print(f'Your new balance is: {bank}!')
					board = newboard+'.'[:-1]
					break
		elif turn.lower() == 'b':
			raise Exception('This code hasn\'t been made yet!')
		elif turn.lower() == 'p':
			raise Exception('This code hasn\'t been made yet!')
		else:
			print('Invalid. Try again.')
			continue


if __name__ == "__main__":
	main()
