from descriptive_measures.postion_measures import get_percentile


def range_inter_quartile(data):
    return get_percentile(data, 75) - get_percentile(data, 25)
