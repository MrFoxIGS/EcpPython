def palindrome(word):
    chars = list(word)
    state = False
    end = len(chars) - 1

    for i in range(len(chars)):

        if chars[i] != chars[end]:
            state = False
            break
        elif i >= end:
            state = True
            break
        else:
            end -= 1
    return state
