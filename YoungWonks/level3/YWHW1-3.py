def get_vowels(word, vowels=0):
    if len(word) <= 1:
        if word[0] in ('a', 'e', 'i', 'o', 'u'):
            vowels += 1
        return vowels
    if word[0] in ('a', 'e', 'i', 'o', 'u'):
        return get_vowels(word[1:], vowels+1)
    else:
        return get_vowels(word[1:], vowels)

print(get_vowels('hello'))