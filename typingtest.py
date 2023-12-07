import time
import requests
import termcolor


def find_accuracy(prompt, typed, chars):
	correct = 0
	print(chars)
	if prompt == typed:
		return 100
	else:
		for out_char in prompt:
			in_char = typed[prompt.index(out_char)]
			if out_char == in_char:
				correct += 1

	return (correct/chars)

def main():
	input('Welcome! Remember: You MUST press enter when you finish the test. The game will start when you press enter: ')
	prompt = requests.get('https://zenquotes.io/api/random').json()[0]
	quote = prompt['q']
	author = prompt['a']
	num_words = len(quote.split(' '))
	print(num_words)
	num_chars = len(list(''.join(quote.split(' '))))
	print(num_chars)
	for i in range(3, 1, -1):
		print(f'The prompt will appear in {i} seconds!', end='\r')
		time.sleep(1)
	print('The prompt will appear in 1 second!!!')
	time.sleep(1)
	print('GO!')
	start_time = time.time()
	print(termcolor.colored(quote, 'green', attrs=['bold']), end='\r')
	typed = input('')
	time_taken = time.time() - start_time
	print(time_taken)
	accuracy = find_accuracy(''.join(quote.split(' ')), ''.join(typed.split(' ')), num_chars)
	print(f'speed_wpm = {num_words} / ({time_taken}/60) * {accuracy}')
	speed_wpm = num_words / (time_taken/60) * accuracy
	speed_wps = speed_wpm / 60
	speed_cpm = num_chars / (time_taken/60) * accuracy
	speed_cps = speed_cpm / 60
	print(f'Speed (WPM): {speed_wpm}')
Speed (WPS): {speed_wps},\n\
Speed (CPM): {speed_cpm},\n\
Speed (CPS): {speed_cpm}')
	print(f'\nQuote: {quote}\n\
Author: {author}')


if __name__ == "__main__":
	main()
