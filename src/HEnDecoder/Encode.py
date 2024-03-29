"""
The defination of image decoding work flow.

@auth: FATESAIKOU
"""

import heapq
from bitarray import bitarray

def GetABC(data, index):
    return (data[index] if index > 0 else 0)

def GetDiffCount(data, width, pmode):
    # A = d[i - 1]
    # B = d[i - w]
    # C = d[i - w - 1]
    pred_funs = [
        lambda d, w, i: d[i],
        lambda d, w, i: d[i] - GetABC(d, i - 1),
        lambda d, w, i: d[i] - GetABC(d, i - w),
        lambda d, w, i: d[i] - GetABC(d, i - w - 1),
        lambda d, w, i: d[i] - (GetABC(d, i - 1) + GetABC(d, i - w) - GetABC(d, i - w - 1)),
        lambda d, w, i: d[i] - (GetABC(d, i - 1) + (GetABC(d, i - w) - GetABC(d, i - w - 1)) / 2),
        lambda d, w, i: d[i] - (GetABC(d, i - w) + (GetABC(d, i - 1) - GetABC(d, i - w - 1)) / 2),
        lambda d, w, i: d[i] - (GetABC(d, i - 1) + GetABC(d, i - w)) / 2
    ]
   
    def CountDiff(v, diff_table):
        diff_table[v] = diff_table[v] + 1
        return v

    diff_count = {k: 0 for k in range(-255, 511)}

    diff_data = map(lambda k: CountDiff( pred_funs[pmode](data, width, k), diff_count ), range(len(data)))

    return (diff_data, [(c, k) for (k, c) in diff_count.items() if c > 0])

def GenCodeTable(diff_count):
    # heap queue
    h = []

    # create heap queue & initialize code_table
    code_table = {}
    code_count = {}
    for (c, k) in diff_count:
        heapq.heappush(h, (c, (k,)))
        code_table[k] = bitarray()
        code_count[k] = c

    # define how to update code table
    def UpdateCodeTable(v, item, table):
        for k in item:
            table[k].append(v)

    # coding
    while len(h) > 1:
        a = heapq.heappop(h)
        b = heapq.heappop(h)

        UpdateCodeTable(0, a[1], code_table)
        UpdateCodeTable(1, b[1], code_table)

        heapq.heappush(h, (a[0] + b[0], a[1] + b[1]))

    # reverse all
    for k in code_table:
        code_table[k].reverse()

    return (code_table, code_count)
