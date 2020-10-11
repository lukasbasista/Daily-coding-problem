"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def foo(key: str):
    if key.startswith('0'):
        return 0
    elif len(key) <= 1:
        return 1

    count = 0
    if int(key[:2]) <= 26:
        count += foo(key[2:])

    count += foo(key[1:])
    return count


print(foo('111'))



