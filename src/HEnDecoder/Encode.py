"""
The defination of image decoding work flow.

@auth: FATESAIKOU
"""

import collections 
import sys
import heapq
from bitarray import bitarray

from pprint import pprint

def GetDiffCount(data, width, pmode):
    # A = d[i - 1]
    # B = d[i - w]
    # C = d[i - w - 1]
    pred_funs = [
        lambda d, w, i: d[i],
        lambda d, w, i: d[i] - d[i - 1],
        lambda d, w, i: d[i] - d[i - w],
        lambda d, w, i: d[i] - d[i - w - 1],
        lambda d, w, i: d[i] - (d[i - 1] + d[i - w] - d[i - w - 1]),
        lambda d, w, i: d[i] - (d[i - 1] + (d[i - w] - d[i - w - 1]) / 2),
        lambda d, w, i: d[i] - (d[i - w] + (d[i - 1] - d[i - w - 1]) / 2),
        lambda d, w, i: d[i] - (d[i - 1] + d[i - w]) / 2
    ]
   
    def CountDiff(v, diff_table):
        diff_table[v] = diff_table[v] + 1

    diff_count = {k: 0 for k in range(-255, 511)}

    map(lambda k: CountDiff( pred_funs[pmode](data, width, k), diff_count ), range(len(data)))

    return [(c, k) for (k, c) in diff_count.items() if c > 0]

def GenCodeTable(diff_count):
    # heap queue
    h = []

    # create heap queue & initialize code_table
    code_table = {}
    for item in diff_count:
        heapq.heappush(h, item)
        code_table[item[1]] = (bitarray(), item[0])

    # define how to update code table
    def UpdateCodeTable(v, item, table):
        if isinstance(item, int):
            table[item][0].append(v)
        elif isinstance(item, collections.Iterable):
            for i in item:
                UpdateCodeTable(v, i, table)
        else:
            print 'Encode Error!!'
            pprint((v, item))
            sys.exit(0)

    # coding
    while len(h) > 1:
        a = heapq.heappop(h)
        b = heapq.heappop(h)

        UpdateCodeTable(0, a[1], code_table)
        UpdateCodeTable(1, b[1], code_table)

        heapq.heappush(h, (a[0] + b[0], (a[1], b[1])))

    code_tree = h[0][1]

    return (code_table, code_tree)
