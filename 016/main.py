"""
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish
this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""


class Log(object):
    def __init__(self, n):
        self.n = n
        self._last = 0
        self._arr = []

    def record(self, id):
        if len(self._arr) == self.n:
            self._arr[self._last] = id
        else:
            self._arr.append(id)
        self._last = (self._last + 1) % self.n

    def get_last(self, i):
        return self._arr[self._last - i]


log = Log(3)
log.record("a")
log.record("b")
log.record("c")
log.record("d")
print(log.get_last(3))
