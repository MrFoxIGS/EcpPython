def list_largest(numbers):

    largest = numbers[0]

    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest
