if __name__ == "__main__":
    # Gets input from the user, saves it in variables and then uses the user information

    name = input("What is your name?: ")
    age = input("How old are you " + name + "?")
    print("Hello, " + name)
    print("What a coincidence I am " + age + " years old too")

    # Overwriting variables

    fruit = "apple"
    print(fruit)
    fruit = "pear"
    print(fruit)
    pass
