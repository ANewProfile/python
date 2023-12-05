import random

def main():
	input('Press enter when you\'re ready to start: ')
	possible_answers = []
	answer = random.choice(possible_answers)
	# Create the board (e.g. --- -- --- --- (3 2 3 3))
	possible_spins = ['Bankrupt!', 600, 400, 300, 800, 350, 450, 700, 300, 600, 2500, 'Bankrupt!', 300, 600, 300, 500, 800, 550, 400, 300, 900, 500, 900]
	while True:
		spin = None
		turn = input('Would you like to [s]pin, [b]uy a  vowel, or solve the [p]uzzle? "
		if turn.lower() == 's':
			spin = spin_wheel(possible_spins)
		elif turn.lower() == 'b':
			...
		elif turn.lower() == 'p':
			...
		else:
			print('Invalid. Try again.')
			continue


if __name__ == "__main__":
	main()
