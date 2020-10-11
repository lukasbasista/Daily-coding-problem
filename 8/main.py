"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

"""


def foo(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr[0], arr[1])

    counter = [0 for _ in arr]
    counter[0] = max(0, arr[0])
    counter[1] = max(counter[0], arr[1])

    for i in range(2, len(arr)):
        x = arr[i]
        counter[i] = max(counter[i - 1], x + counter[i - 2])
    return counter[-1]


print(foo([2, 4, 6, 2, 5]))
print(foo([5, 1, 1, 5]))
