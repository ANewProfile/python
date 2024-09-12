def process_sentence(sentence: str):
    data = {'total': 0, 'vowels': 0, 'uppercase': 0, 'most_frequent': ['', 0], 'longest': [('', 0)]}
    
    for word in sentence.split():
        if word[-1].isalpha():
            if len(word) > data['longest'][0][1]:
                data['longest'] = [(word, len(word))]
            elif len(word) == data['longest'][0][1]:
                data['longest'].append((word, len(word)))
        else:
            if len(word[:-1]) > data['longest'][0][1]:
                data['longest'] = [(word[:-1], len(word[:-1]))]
            elif len(word[:-1]) == data['longest'][0][1]:
                data['longest'].append((word[:-1], len(word[:-1])))
            
            
        for letter in word:
            if not letter.isalpha():
                continue
            if letter in ('a', 'e', 'i', 'o', 'u'):
                data['vowels'] += 1
            if letter != letter.lower():
                data['uppercase'] += 1
                
            # if data[letter]:
            #     data[letter] += 1
            #     if letter == data['most_frequent'][0]:
            #         data['most_frequent'][1] += 1
            #     elif data[letter] > data['most_frequent'][1]:
            #         data['most_frequent'] = [letter, data[letter]]
            # else:
            #     data['total'] += 1
            #     data[letter] = 1
            
            try:
                if data[letter.lower()]:
                    pass
            
                data[letter.lower()] += 1
                if letter.lower() == data['most_frequent'][0]:
                    data['most_frequent'][1] += 1
                elif data[letter.lower()] > data['most_frequent'][1]:
                    data['most_frequent'] = [letter.lower(), data[letter.lower()]]
            except KeyError:
                data['total'] += 1
                data[letter.lower()] = 1

    data['longest'] = sorted(data['longest'])[0][0]
    data['most_frequent'] = data['most_frequent'][1]
    return f"1. {data['total']}\n2. {data['vowels']}\n3. {data['uppercase']}\n4. {data['most_frequent']}\n5. {data['longest']}"

print(process_sentence('The quick brown fox, named Roxanne, jumped over Bruno, a lazy dog.'))