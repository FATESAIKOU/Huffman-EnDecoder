"""
The defination of image decoding work flow.

@auth: FATESAIKOU
"""

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

    diff_count = {k: 0 for k in range(-255, 255)}

    map(lambda k: CountDiff( pred_funs[pmode](data, width, k), diff_count ), range(len(data)))

    return [(k, c) for (k, c) in diff_count.items() if c > 0]
