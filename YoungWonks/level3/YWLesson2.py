import time

def parse(input: str):
    new_input = input.split('\n')[1:]
    cards = {i+1: hand for i, hand in enumerate(new_input)}
    
    for player, hand in cards.items():
        new_hand = hand.split()
        new_hand = [card[0] for card in new_hand]
        for index in range(0, len(new_hand)):
            if new_hand[index] == 'T':
                new_hand[index] = '10'
            elif new_hand[index] == 'J':
                new_hand[index] = '11'
            elif new_hand[index] == 'Q':
                new_hand[index] = '12'
            elif new_hand[index] == 'K':
                new_hand[index] = '13'
            elif new_hand[index] == 'A':
                new_hand[index] = '14'
            elif new_hand[index] == '2':
                new_hand[index] = '15'

            new_hand[index] = int(new_hand[index])
        
        cards[player] = sorted(new_hand)

    return cards

def find_most_appeared(cards, turn):
    appearences = {}
    for card in cards[turn]:
        try:
            appearences[card] += 1
        except:
            appearences[card] = 1
    
    times_seen = max(appearences.values())
    max_seen = []
    for key in appearences.keys():
        if appearences[key] == times_seen:
            max_seen.append(key)
            
    return (times_seen, min(max_seen))

def find_appeared(cards, turn, inrow):
    appearences = {}
    for card in cards[turn]:
        try:
            appearences[card] += 1
        except:
            appearences[card] = 1
    
    seen = []
    for key in appearences.keys():
        if appearences[key] == inrow:
            seen.append(key)
            
    return seen


def main(input):
    cards = parse(input)
    fake_turn = 0
    playing = list(range(1, len(cards)+1))
    order = []
    
    old_top = (0, 0)
    top = (0, 0)
    
    passing = False
    first_pass = 0
    
    new_round = True
    while True:
        # turn = (fake_turn%len(cards))+1
        turn = playing[fake_turn%len(cards)]
        
        old_top = top
        
        if len(cards) <= 1:
            break
        
        if first_pass == turn and passing:
            new_round = True
            fake_turn = (first_pass+3)-2
            passing = False
            first_pass = 0
            continue
        
        if new_round:
            num_appeared, most_appeared = find_most_appeared(cards, turn)
            top = (num_appeared, most_appeared)
            print(f'{turn} sets {top}')
            for _ in range(0, top[0]):
                cards[turn].remove(top[1])
                # cards[playing[turn-1]].remove(top[1])
                
            if cards[turn] == []:
            # if cards[playing[turn-1]] == []:
                order.append(str(turn))
                cards.pop(turn)
                playing.remove(turn)
                
            fake_turn += 1
            new_round = False
            continue
        
        time.sleep(0.5)
        
        next_options = find_appeared(cards, turn, top[0])
        for option in next_options:
            if option > top[1]:
                top = (top[0], option)
                print(f'{turn} plays {top}')
                passing = False
                first_pass = 0
                
                for _ in range(0, top[0]):
                    cards[turn].remove(top[1])
                    # cards[playing[turn-1]].remove(top[1])
                
                if cards[turn] == []:
                # if cards[playing[turn-1]] == []:
                    order.append(str(turn))
                    print(turn)
                    cards.pop(turn)
                    playing.remove(turn)
                
                break
        fake_turn += 1
        
        if old_top == top:
            print('passed')
            if not passing:
                first_pass = turn
            passing = True
            fake_turn += 1
    
    
    return ' '.join(order) + ' ' + str(list(cards.keys())[0])

answer = main('4 \n\
6S 9C 9H QC 9S 5H KS TC 5C QH JS 5D JH \n\
3C 7S 5S JD 8H QD TD 2C 6D TS 2D 3S 8D \n\
TH AC 7H 6H 4D 4H 3D AD 7D 2H 8S 6C 4S \n\
KC 2S 9D AS 7C KD KH 3H JC 4C QS 8C AH')
print(answer)
