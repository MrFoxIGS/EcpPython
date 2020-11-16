

def palindrome2(word):
    from palindrome import palindrome
    from LetterList import letter_list
    chars = letter_list(word)
    state = palindrome(chars)
    return(state)


