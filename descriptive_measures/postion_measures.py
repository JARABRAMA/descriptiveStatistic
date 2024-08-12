def get_percentile(data: list, i: int):
    data = sorted(data)
    assert 1 <= i <= 100, 'percentile must be between 1 and 100'
    p = len(data) * i * 0.01
    if p.is_integer():
        return (data[int(p - 1)] + data[int(p)]) * 0.5
        # the equation differ because the position was translated to an index
    else:
        return data[int(p)]
