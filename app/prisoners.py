"""
This problem was asked by Bloomberg.

There are N prisoners standing in a circle, waiting to be executed.
The executions are carried out starting with the kth person, and removing every
successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.
"""


def order_of_execution(count: int, k: int):
    """
    This one is linear time.
    :param count:
    :param k:
    :return:
    """
    actions = 0
    r = [*range(1, 1 + count, 1)]
    removed = []
    pos = 0
    while len(r) != 0:
        pos = (pos + (k - 1)) % len(r)
        removed.append(r.pop(pos))
        actions += 1

    print(f"actions: {actions}")
    return removed


result = order_of_execution(5, 2)
print(f"last person: {result[-1]}, list: {result}")


