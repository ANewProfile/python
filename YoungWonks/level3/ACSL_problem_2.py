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

def start_new_round(cards, turn, order, playing):
    num_appeared, most_appeared = find_most_appeared(cards, turn)
    top = (num_appeared, most_appeared)
    print(f'{turn} starts with {top}')
    for _ in range(0, top[0]):
        cards[turn].remove(top[1])
        # cards[playing[turn-1]].remove(top[1])
        
    if cards[turn] == []:
    # if cards[playing[turn-1]] == []:
        order.append(str(turn))
        # cards.pop(turn)
        # playing.remove(turn)
    
    return cards, order, playing, top

def play_next_move(cards, turn, order, playing, top):
    next_options = find_appeared(cards, turn, top[0])
    for option in next_options:
        if option > top[1]:
            top = (top[0], option)
            print(f'{turn} plays {top}')
            
            for _ in range(0, top[0]):
                cards[turn].remove(top[1])
                # cards[playing[turn-1]].remove(top[1])
            
            if cards[turn] == []:
            # if cards[playing[turn-1]] == []:
                order.append(str(turn))
                # cards.pop(turn)
                # playing.remove(turn)
            
            break
    
    return cards, order, playing, top


def main(input):
    cards = parse(input)
    print(cards)
    fake_turn = 0
    playing = list(range(1, len(cards)+1)) # list of all players with players removed as we play
    order = []
    
    old_top = (0, 0)
    top = (0, 0)
    
    passing = False
    first_pass = 0
    
    new_round = True
    while True:
        # turn = (fake_turn%len(cards))+1
        print("cards are", cards, playing)
        cur_player_name = playing[fake_turn%len(cards)] # current player
        
        if cards[cur_player_name] == []:
            fake_turn += 1
            continue
        
        old_top = top
        
        still_in = 0
        for hand in cards.values():
            if hand != []:
                still_in += 1
        if still_in == 1:
            break
        
        if first_pass == cur_player_name and passing:
            new_round = True
            fake_turn = playing.index(first_pass)-1
            passing = False
            first_pass = 0
            print(cur_player_name, "already passed, start new round")
            continue
        
        if new_round:
            cards, order, playing, top = start_new_round(cards, cur_player_name, order, playing)
            fake_turn += 1
            new_round = False
            continue
            
        #time.sleep(0.5)
        
        cards, order, playing, top = play_next_move(cards, cur_player_name, order, playing, top)
        fake_turn += 1
        
        if old_top == top:
            print(cur_player_name, 'passed')
            if not passing:
                first_pass = cur_player_name
            passing = True
        else:
            passing = False
            first_pass = 0
    
    still_in = 0
    for player, hand in cards.items():
        if hand != []:
            still_in = player
    
    return ' '.join(order) + ' ' + str(still_in)

answer = main('4 \n\
6S 9C 9H QC 9S 5H KS TC 5C QH JS 5D JH \n\
3C 7S 5S JD 8H QD TD 2C 6D TS 2D 3S 8D \n\
TH AC 7H 6H 4D 4H 3D AD 7D 2H 8S 6C 4S \n\
KC 2S 9D AS 7C KD KH 3H JC 4C QS 8C AH')  # desired: 1 2 3 4

# 1 

# answer = main('''5
# 6C 8H 7C 5H 6H AD TC AC TD JH
# 7D KD 4C 5D 9H 8D 9D KH 8C KC
# 3D 5S QD JC 7S 4H JS 3S 8S 3C
# JD 7H 2C 4D AH TS 2D 6D AS 3H
# QC KS 2H 5C 6S QS TH 9C 2S 4S''')

print(answer)

# {1: [], first
# 2: [], second
# 3: [], 3
# 4: []} 4

