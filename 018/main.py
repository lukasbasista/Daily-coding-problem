"""
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of
each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results.
You can simply print them out as you compute them.
"""

from collections import deque


def foo(arr, k):
    que = deque()
    for i in range(k):
        while que and arr[i] >= arr[que[-1]]:
            que.pop()
        que.append(i)

    for i in range(k, len(arr)):
        print(arr[que[0]])
        while que and que[0] <= i - k:
            que.popleft()
        while que and arr[i] >= arr[que[-1]]:
            que.pop()
        que.append(i)
    print(arr[que[0]])


foo([10, 5, 2, 7, 8, 7], 3)