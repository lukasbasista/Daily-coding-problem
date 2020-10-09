"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def foo(arr):
    if len(arr) == 1:
        return [0]
    product = 1
    for n in arr:
        product *= n
    newarr = []
    for i in range(len(arr)):
        newarr.append(product // arr[i])
    return newarr


# Without division
def foo2(arr):
    if len(arr) == 1:
        return [0]
    leftarr = []
    rightarr = []
    newarr = []
    l = 1
    r = 1
    for i in range(len(arr)):
        l *= arr[i]
        r *= arr[len(arr) - i - 1]
        leftarr.append(l)
        rightarr.append(r)
    newarr.append(rightarr[len(rightarr) - 2])
    for n in range(1, len(arr) - 1):
        newarr.append(leftarr[n-1] * rightarr[len(rightarr) - n - 2])
    newarr.append(leftarr[len(leftarr) - 2])
    return newarr


print(foo([1, 2, 3, 4, 5]))
print(foo([3, 2, 1]))
print(foo2([1, 2, 3, 4, 5]))
print(foo2([3, 2, 1]))
