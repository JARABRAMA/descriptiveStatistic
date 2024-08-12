def get_average(dta: list):
    return sum(dta) / len(dta)


def get_median(dta: list):
    n = len(dta)
    if n % 2 == 1:
        index = int((n + 1) / 2 - 1)
        return dta[index]
    else:
        return (dta[int(n / 2 - 1)] + dta[int(n / 2)]) / 2


def get_mode(dta: list):
    dta = sorted(dta)
    modes = []
    c = 0
    max_count = c
    element = dta[0]
    for x in dta:
        if x == element:
            c += 1
        else:
            if c > max_count:
                modes.clear()
                max_count = c
                modes.append(element)
            elif c == max_count:
                modes.append(element)
            c = 1
            element = x

    if c == max_count:
        modes.append(element)
    elif c > max_count:
        modes.clear()
        modes.append(element)
    return modes

