from collatz_sequence import collatz_sequence


def test_collatz():
    results = list()
    result = collatz_sequence.collatz(3)
    results.append(result)

    while result != 1:
        result = collatz_sequence.collatz(result)
        results.append(result)

    sequence_values = (10, 1, 16, 4, 8, 2, 5)
    for element in results:
        assert element in sequence_values
    for element in sequence_values:
        assert element in results
