def letter_list(word):
    chars = word.lower()
    chars = chars.replace(' ', '')
    chars = list(chars)

    alpha = []
    for letter in chars:
        if letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y''z']:
            alpha.append(letter)
    return alpha


