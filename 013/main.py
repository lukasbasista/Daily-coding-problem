"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""


def foo(s, k):
    if k == 0:
        return 0
    fromto = (0, 0)
    h = {}
    result = 0
    for i, j in enumerate(s):
        h[j] = i
        if len(h) > k:
            remove = min(h, key=h.get)
            left = h.pop(remove) + 1
        else:
            left = fromto[0]

        fromto = (left, fromto[1] + 1)
        result = max(result, fromto[1] - fromto[0])

    return result


print(foo("abcba", 2))