"""
The defination of image encoding work flow.

@auth: FATESAIKOU
"""

def GetABC(data, index):
    return (data[index] if index > 0 else 0)

def BuildFromDiff(diffs, width, pmode):
    # A = d[i - 1]
    # B = d[i - w]
    # C = d[i - w - 1]
    build_funs = [
        lambda d, o, w, i: d[i],
        lambda d, o, w, i: d[i] + GetABC(o, i - 1),
        lambda d, o, w, i: d[i] + GetABC(o, i - w),
        lambda d, o, w, i: d[i] + GetABC(o, i - w - 1),
        lambda d, o, w, i: d[i] + (GetABC(o, i - 1) + GetABC(o, i - w) - GetABC(o, i - w - 1)),
        lambda d, o, w, i: d[i] + (GetABC(o, i - 1) + (GetABC(o, i - w) - GetABC(o, i - w - 1)) / 2),
        lambda d, o, w, i: d[i] + (GetABC(o, i - w) + (GetABC(o, i - 1) - GetABC(o, i - w - 1)) / 2),
        lambda d, o, w, i: d[i] + (GetABC(o, i - 1) + GetABC(o, i - w)) / 2
    ]

    
    ori_data = [0] * len(diffs)
    for index in range(len(diffs)):
        ori_data[index] = build_funs[pmode](diffs, ori_data, width, index)

    return ori_data
