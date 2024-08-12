# in this place we are going to test all the created functions

from tables.intervals_tables import print_intervals_table
from descriptive_measures import central_tendency as mct
from descriptive_measures import postion_measures as mp
from descriptive_measures import dispersion_measures as dm


def get_analysis(dta: list) -> None:
    print(f"Hello, we are going to make an analysis of this data:\n{dta}", end="\n\n")
    print("This is the frequency table:", end="\n\n")
    print_intervals_table(dta)
    print(
        f"The central tendency measures\n\tmode: {mct.get_mode(dta)}\n\taverage: "
        f"{mct.get_average(dta)}\n\tmedian: {mct.get_median(dta)}",
        end="\n\n")
    print(f'The quartiles:\n\tquartile 25: {mp.get_percentile(dta, 25)}\n\t'
          f'quartile 50: {mp.get_percentile(dta, 50)}\n\tquartile 75: {mp.get_percentile(dta, 75)}',
          end="\n\n")
    print(f'the dispersion of the data in the 50 \npercent more central is: {dm .range_inter_quartile(dta)}')


if __name__ == '__main__':
    # modify the data
    data = [18, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23,
            24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30,
            30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36,
            37]

    get_analysis(data)
