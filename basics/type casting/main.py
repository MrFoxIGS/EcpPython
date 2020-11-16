if __name__ == "__main__":
    # data from input is type str, can use int() to change it to an integer

    numb1 = input("Input a number: ")
    numb2 = input("Input another number: ")

    # numb1 and numb2 are strings, the + joins the strings together
    print(numb1 + numb2)

    # typecasting numb1 and 2 as integers allows addition (and other mathematical operations) to be performed
    sumz = int(numb1) + int(numb2)

    print(sumz)

    # you can only join strings with other strings so to print the sum with some other text you need to typecast the integer as a string str

    print(numb1 + "+" + numb2 + "=" + str(sumz))
    pass
