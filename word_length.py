"""
Hayden Orth
Activity 4: word length
Project 1
CSCI 0242
"""
import argparse
import os.path
import matplotlib.pyplot as plt


def read_years_words(filename: str):
    """
    reads years from csv file and stores in two dictionaries: years and years_totalwords
    years:              year as key, lengths of words as value
    years_totalwords:   year as key, total number of words as value
    :param filename: csv file containing words, year, frequency
    :return: years, years_totalwords
    """
    years = dict()
    years_totalwords = dict()
    with open(filename) as f:
        for line in f:
            fields = line.split(', ')
            if int(fields[1]) not in years:
                years[int(fields[1])] = (len(fields[0]) * int(fields[2]))
                years_totalwords[int(fields[1])] = int(fields[2])
            else:
                years[int(fields[1])] += (len(fields[0]) * int(fields[2]))
                years_totalwords[int(fields[1])] += int(fields[2])
    return years, years_totalwords


def calculate_year_avg(years_lengths: dict, years_totalwords: dict):
    """
    takes values from years_lengths and years_totalwords dictionaries
    calculates average word length for each year and stores in a new, sorted dictionary.
    :param years_lengths: dictionary w/ years as key, total word lengths as value
    :param years_totalwords: dictionary w/ years as key, total number of words as value
    :return: years_avg: sorted dictionary w/ years as key, average word length as value
    """
    averages = dict()
    # calculates average word length
    for year in years_lengths:
        averages[year] = years_lengths[year] / years_totalwords[year]
    # sorts average dictionary by year
    sorted_averages = dict()
    for Y in sorted(averages):
        sorted_averages[Y] = averages[Y]
    return sorted_averages


def main():
    """
    main function. reads command line using argparse and runs word length
    :return: none
    """
    # argparse to read command line parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='display the average word lengths over years',
                        action='store_true')
    parser.add_argument('-p', '--plot', action='store_true', help='the average word lengths over years')
    parser.add_argument('start', type=int, help='the starting year range')
    parser.add_argument('end', type=int, help='the ending year range')
    parser.add_argument('filename', help='a comma separated value unigram file')
    args = parser.parse_args()
    start = args.start
    end = args.end
    filename = args.filename

    # error check start and end year arguments
    if start > end:
        exit('ERROR: start year must be less than or equal to end year!')
    # error check file command line argument
    if not os.path.exists(filename):
        exit("ERROR: " + filename + " does not exist!")

    # read words and years
    years_lengths, years_totalwords = read_years_words(filename)

    # calculate average word length for each year and store in dict
    # get lists of years and corresponding averages
    years_avg = calculate_year_avg(years_lengths, years_totalwords)

    # display range of years if requested
    start2 = start  # start2 is used in the plotting section
    if args.output:
        while start <= end:
            print(str(start) + ': ' + str(years_avg[start]))
            start += 1

    # plot average length per year over range
    start3 = start2     # start3 is used in the plot title
    x, y = [], []
    while start2 <= end:
        x.append(start2)
        y.append(years_avg[start2])
        start2 += 1
    plt.plot(x, y)
    plt.title('Average word lengths from' + str(start3) + ' to ' + str(end) +': ' + filename)
    plt.xlabel('Year')
    plt.ylabel('Average word length')
    plt.show()


if __name__ == '__main__':
    main()