if __name__ == "__main__":
    import random

    # loop counter i
    i = 0
    while i < 5:
        print("hello")
        i += 1  # increases the loop counter by 1
    print("I said hello " + str(i) + " times")

    # Using a while loop to simulate rolling a die over and over
    again = " "
    print("")
    print("Automatic dice roller, type q to quit")
    while again != "q":
        print(random.randint(1, 6))
        again = input("")
    print("goodbye")

    pass
