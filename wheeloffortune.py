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
	for i in range(1, 21):
		# print(i)
		print(random.choice(possibilities))
		sleep(i/30)
	amount = random.choice(possibilities)
	
	return amount

def guess_letter(letter, solution, board):
	board = list(board)
	list_solution = list(solution)
	fake_solution = list_solution.copy()
	items_correct = 0
	for character in list_solution:
		if letter == character:
			# print(f'{board[fake_solution.index(letter)]} (index {fake_solution.index(letter)}) was set to {letter}')
			board[fake_solution.index(letter)] = letter
			# print(f'Removing: {letter} (index {list_solution.index(letter)})
			fake_solution[fake_solution.index(letter)] = ' '
			items_correct += 1

	print(''.join(list_solution))
	board = ''.join(board)
	return board, items_correct

def guess_answer(guess, answer):
	correct = None
	if guess == answer:
		correct = True
	else:
		correct = False	

	return correct

def main():
	bank = 0
	input('Press enter when you\'re ready to start: ')
	possible_answers = ['an apple a day keeps the doctor away', 'the quick brown fox jumps over the lazy dog']
	answer = 'an apple a day keeps the doctor away'
	# answer = random.choice(possible_answers)
	board = make_board(answer)
	print(board)
	possible_spins = ['bankrupt', 600, 400, 300, 800, 350, 450, 700, 300, 600, 2500, 'bankrupt', 300, 600, 300, 500, 800, 550, 400, 300, 900, 1500, 500, 900]
	turns = 0
	while True:
		spin = None
		turn = input('Would you like to [s]pin, [b]uy a  vowel, or solve the [p]uzzle? ')
		if turn.lower() == 's':
			spin = spin_wheel(possible_spins)
			if spin == 'bankrupt':
				bank = 0
				print('Bankrupt!')
				print(f'Your balance is ${bank}!')
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
					newboard, num_items_correct = guess_letter(guess, answer, board)
					print(newboard)
					if newboard != board:
						bank += spin * num_items_correct
						print(f'Your balance is ${bank}!')
					board = newboard+'.'[:-1]
					turns += 1
					break
		elif turn.lower() == 'b':
			while True:
				guess = input('Enter the vowel you would like to guess: ').lower()
				
				if bank < 250:
					print('You don\'t have enough money!')
					guess = None
					break
				elif guess in ['b', 'c', 'd', 'f' 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y', 'z']:
					print('No consonants please!')
					guess = None
				elif len(guess) > 1 or len(guess) < 1:
					print('Only one letter please!')
					guess = None
				elif guess not in ['a', 'e', 'i', 'o', 'u']:
					print('Only letters in the English alphabet please!')
					guess = None
				else:
					newboard, num_items_correct = guess_letter(guess, answer, board)
					print(newboard)
					bank -= 250
					print(f'Your balance is ${bank}!')
					board = newboard+'.'[:-1]
					turns += 1
					break
		elif turn.lower() == 'p':
			guess = input('Enter your guess: ').lower()
			is_correct = guess_answer(guess, answer)
			if is_correct is True:
				print(f'You got it right! It took you a total of {turns} turns and you had ${bank} remaining!')
				break
			elif is_correct is False:
				print('Incorrect!')
			else:
				raise Exception('YOU SHOULD NEVER SEE THIS')
		else:
			print('Invalid. Try again.')
			continue


if __name__ == "__main__":
	main()
