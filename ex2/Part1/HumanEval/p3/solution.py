def func1(a: str, b: str) -> str:
    """ Perform binary XOR on two strings consisting only of 1s and 0s. """
    result = []
    for x, y in zip(a, b):
        result.append('1' if x != y else '0')
    return ''.join(result)

