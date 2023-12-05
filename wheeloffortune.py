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
	for i in range(1, 11):
		# print(i)
		print(random.choice(possibilities))
		sleep(i/10)
	amount = random.choice(possibilities)

def main():
	input('Press enter when you\'re ready to start: ')
	possible_answers = ['an apple a day keeps the doctor away', 'the quick brown fox jumps over the lazy dog']
	answer = random.choice(possible_answers)
	board = make_board(answer)
	print(board)
	possible_spins = ['Bankrupt!', 600, 400, 300, 800, 350, 450, 700, 300, 600, 2500, 'Bankrupt!', 300, 600, 300, 500, 800, 550, 400, 300, 900, 500, 900]
	while True:
		spin = None
		turn = input('Would you like to [s]pin, [b]uy a  vowel, or solve the [p]uzzle? ')
		if turn.lower() == 's':
			spin = spin_wheel(possible_spins)
		elif turn.lower() == 'b':
			raise Exception('This code hasn\'t been made yet!')
		elif turn.lower() == 'p':
			raise Exception('This code hasn\'t been made yet!')
		else:
			print('Invalid. Try again.')
			continue


if __name__ == "__main__":
	main()
