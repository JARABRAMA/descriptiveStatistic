from pandas import DataFrame


def get_absolute_frequency(values) -> list:
    absolute_frequency = []
    element = values[0]
    count = 1
    for i in range(1, len(values)):
        if element == values[i]:
            count += 1
        else:
            absolute_frequency.append(count)
            count = 1
            element = values[i]
    absolute_frequency.append(count)
    return absolute_frequency


def get_singles(values) -> list:
    singles = []
    for x in values:
        if x not in singles:
            singles.append(x)
    return singles


def get_relative_frequency(absolute_frequency: list) -> list:
    n = len(absolute_frequency)
    return [x / n for x in absolute_frequency]


def get_percentual_frequency(relative_frequency: list) -> list:
    return [x * 100 for x in relative_frequency]


def get_simple_table(values: list) -> DataFrame:
    frequency = get_absolute_frequency(values)
    relative_frequency = get_relative_frequency(frequency)
    table = {
        'x': get_singles(values),
        'fa': frequency,
        'fr': relative_frequency,
        'f%': get_percentual_frequency(relative_frequency)
    }
    return DataFrame(table)




