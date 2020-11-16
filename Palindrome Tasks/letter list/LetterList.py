def letter_list(words):
    chars = words.lower()
    chars = chars.replace(' ', '')
    chars = list(chars)

    letters = []
    for letter in chars:
        if letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y','z']:
            letters.append(letter)
    return letters


