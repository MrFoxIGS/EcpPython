# todo: replace this with an actual task
def scrabble(word):
    score = 0
    word = word.lower()
    for letter in word:
        if letter in ['a','e','i','o','u','l','s','t','r']:
            score += 1
        elif letter in ['d','g']:
            score += 2
        elif letter in ['b','c','m','p']:
            score += 3
        elif letter in ['f','h','v','w','y']:
            score += 4
        elif letter == 'k':
            score += 5
        elif letter in ['j','x']:
            score += 7
        elif letter in ['q','z']:
            score += 10

    return score


