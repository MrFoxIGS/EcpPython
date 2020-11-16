if __name__ == "__main__":
    # uses the type function to print the type of data in the list

    datalist = [1452, 11.23, 1+2j, True, 'strings!!!', (0, -1), [5, 12],
    {"class":'V', "section":'A'}]
    for item in datalist:
        print ("Type of ",item, " is ", type(item))
    pass
