# this script has the purpose of create table by intervals
import math
from pandas import DataFrame


def get_intervals(values: list) -> list[list, list]:
    r = max(values) - min(values)
    n = len(values)
    k = math.ceil((1 + 3.32 * math.log10(n)))
    a = math.ceil(r / k)
    inferior = []
    superior = []
    p = min(values)
    for _ in range(k):
        inferior.append(p)
        superior.append(p + a)
        p += a
    return [inferior, superior]


def get_class_mark(intervals: list[list, list]) -> list:
    return [(intervals[0][i] + intervals[1][i]) * 0.5 for i in range(len(intervals[0]))]


# @param data must be ordered
def get_absolute_frequency(inferior_limit: list, superior_limit: list, dta: list) -> list:
    frequencies = []
    count = 0
    i, f = inferior_limit[0], superior_limit[0]
    index = 0
    for x in dta:
        if i <= x < f:
            count += 1
        else:
            frequencies.append(count)
            index += 1
            count = 1
            if index == len(inferior_limit):
                break
            i, f = inferior_limit[index], superior_limit[index]
    frequencies.append(count)
    return frequencies


def get_relative_frequency(abs_frequency: list, n: int) -> list:
    return [x / n for x in abs_frequency]


def get_percentual_frequency(rlt_frequency: list) -> list:
    return [x * 100 for x in rlt_frequency]


def get_acc(lts: list) -> list:
    acc = 0
    return [acc := acc + x for x in lts]


def print_intervals_table(dta: list):
    dta = sorted(dta)
    intervals = get_intervals(dta)
    li = intervals[0]
    lf = intervals[1]
    class_mark = get_class_mark(intervals)
    absolute_frequency = get_absolute_frequency(li, lf, dta)
    relative_frequency = get_relative_frequency(absolute_frequency, len(dta))
    percentual_frequency = get_percentual_frequency(relative_frequency)
    table = {
        'li': li,
        'lf': lf,
        'mi': class_mark,
        'fa': absolute_frequency,
        'fr': relative_frequency,
        'f%': percentual_frequency,
        'Fa': get_acc(absolute_frequency),
        'Fr': get_acc(relative_frequency),
        'F%': get_acc(percentual_frequency)
    }
    print(DataFrame(table), end="\n\n")


def testing_intervals_generation(dta: list) -> None:
    print(get_intervals(dta))


if __name__ == '__main__':
    data = [18, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23,
            24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30,
            30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36,
            37]

    testing_intervals_generation(data)
