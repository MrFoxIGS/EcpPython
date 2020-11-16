if __name__ == "__main__":
    house = input("Please enter your house: ")
    house = house.lower() # converts all letters to lower case
    if house == "sherwood":
        print("GO SHERWOOD!!!!")
    else:
        print("That's unfortunate")

    word = input("Enter a word: ")
    word = word.lower()

    vowel = 0
    cons = 0
    for letter in word:
        if letter in ['a','e','i','o','u']:
            vowel += 1

        else:
            cons += 1
    print("The number of vowels in "+ word + " is "+ str(vowel))
    print("The number of consonants in "+ word + " is "+ str(cons))

    number = int(input("Please enter an integer: "))
    if number %3 == 0:
        print(str(number)+ " is divisible by 3")
        if number %5 == 0:
            print(str(number)+ " is divisible by 5")

    elif number %5 == 0:
        print(str(number)+ " is divisible by 5")

    else:
        print(str(number)+ " is not divisible by 3 or 5")

    pass
