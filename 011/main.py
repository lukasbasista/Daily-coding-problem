"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all
strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
"""


def foo(qs, arr):
    result = []
    for s in arr:
        if s.startswith(qs):
            result.append(s)
    return result


print(foo("de", ["dog", "deer", "deal"]))