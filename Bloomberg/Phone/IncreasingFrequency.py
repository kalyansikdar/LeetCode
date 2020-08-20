"""
Given an array of numbers, output them in increasing frequency, and in descending order. For example: {3, 4, 2, 5,
2, 3, 4, 3, 6} which would give us {6, 5, 4, 4, 2, 2, 3, 3, 3}
"""
import collections


def output(elements):
    counts = collections.Counter(elements)
    sorted_arr = sorted(counts.items(), key= lambda x: (x[1], -x[0]))
    print (sorted_arr)

    result = []
    for element in sorted_arr:
        for i in range(element[1]):
            result.append(element[0])

    print (result)
    return result


assert output([3, 4, 2, 5, 2, 3, 4, 3, 6]) == [6, 5, 4, 4, 2, 2, 3, 3, 3]
assert output([7,7,7,7,2,2,3,3,1,1,9,6,6,6,6]) == [9, 3, 3, 2, 2, 1, 1, 7, 7, 7, 7, 6, 6, 6, 6]