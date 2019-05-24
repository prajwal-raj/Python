def comma_code(collection):
    if len(collection) == 0:
        return ''
    elif len(collection) == 1:
        return collection[0]

    # list comprehension used to explicitly cast items to str str() converts
    # slice to list of chars, this implementation allows for a mixed list
    return '{}, and {}'.format(', '.join([str(item) for item in collection[:-1]]),
                               str(collection[1]))


if __name__ == '__main__':
    test = ['cat', 'dog', 'bird', 'snake', 'rock']
    test2 = [3, 4, 5, 6]
    print(comma_code(test))
    print(comma_code(test2))
