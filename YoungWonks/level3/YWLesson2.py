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
    fake_turn = 1
    order = []
    old_top = (0, 0)
    top = (0, 0)
    last_passed = 0
    
    new_round = True
    while True:
        turn = (fake_turn%len(cards))+1
        
        if len(cards) <= 1:
            break
        
        if last_passed == turn:
            new_round = True
        
        if new_round:
            num_appeared, most_appeared = find_most_appeared(cards, turn)
            old_top = top
            top = (num_appeared, most_appeared)
            for _ in range(0, top[0]):
                cards[turn].remove(top[1])
                
            if cards[turn] == []:
                order.append(turn)
                cards.pop(turn)
                print(cards)
                fake_turn = 1
                new_round = False
                continue
                
            fake_turn += 1
            new_round = False
            
        next_options = find_appeared(cards, turn, top[0])
        for option in next_options:
            if option > top[1]:
                old_top = top
                top = (top[0], option)
                for _ in range(0, top[0]):
                    cards[turn].remove(top[1])
                
                if cards[turn] == []:
                    order.append(turn)
                    cards.pop(turn)
                    fake_turn = 0
                
                fake_turn += 1
                break
        
        if old_top == top:
            last_passed = turn
    
    
    return ' '.join(order)

print(main('3 \n\
            JC 6C QD AH 8H TS 5D JD 7D 8D 9C 6H QS 9H 4H KH KS \n\
            9D 7S JS 2S 8C TC JH 7C TD 4D 6D 4C 5S 3H 2D 3C 6S \n\
            QC 2H AC KC 5H TH KD AD AS 4S 3S 9S 8S 5C 2C QH 3D'))
