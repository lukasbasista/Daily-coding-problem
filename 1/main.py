""""
This problem was asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def foo(arr, k):
    seen = set()
    for n in arr:
        if k - n in seen:
            return True
        if n >= k:
            continue
        seen.add(n)


print(foo([10,15,3,7], 17))
