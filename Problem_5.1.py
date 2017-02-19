"""
Compute the parity of a very large number of 64-bit words
"""


def parity(word):
    result = 0
    while word:
        result += word & 1
        word >>= 1
    return result % 2

if __name__ == '__main__':
    assert parity(8) == 1
    assert parity(3) == 0
    