import numpy


def tokens_to_types():

    tokens = ['a', 'a', 'b', 'c', 'a']

    types, token_ids = numpy.unique(tokens, return_inverse=True)

    print 'Tokens:', tokens
    print 'Vocabulary:', types
    print 'Token indices:', token_ids


if __name__ == '__main__':
    tokens_to_types()
