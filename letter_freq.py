"""
Hayden Orth
Activity 2: letter frequency
Project 1
CSCI 0242
"""
import argparse
import os.path
# import read_words function from word_count file
from word_count import read_words
# import mathplotlib
import numpy as np
import matplotlib.pyplot as plt


def plot_data(data: dict, filename: str, total: int):
    """
    plots the letter data in a bar graph using mathplotlib
    :param data: sorted letter dictionary
    :param filename: name of file
    :param total: total number of letters
    :return: none
    """
    x_labels = data.keys()
    y_pos = np.arange(len(data.keys()))
    freq = []
    for point in data:
        freq.append(data[point] / total)

    plt.bar(y_pos, freq, align='center', alpha=0.5)
    plt.xticks(y_pos, x_labels)
    plt.ylabel('Frequency')
    plt.title('Letter frequencies: ' + filename)

    plt.show()


def count_letters(words: dict):
    """
    takes a word dictionary and returns an alphabetical dictionary:
    each letter of alphabet is its own key, total appearances is its value
    :param words: dictionary of words
    :return: dictionary sorted alphabetically, total number of letters(for frequency calculation)
    """
    letters = dict()
    total_letters = 0
    # iterate through word dictionary
    for word in words:
        for letter in word:
            if letter not in letters:
                letters[letter] = words[word]
                total_letters += words[word]
            else:
                letters[letter] += words[word]
                total_letters += words[word]

    # add letters that didn't appear to letters
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alpha:
        if letter not in letters:
            letters[letter] = 0

    # sort letters (s)
    s = dict()
    for letter in sorted(letters):
        s[letter] = letters[letter]

    return s, total_letters


def main():
    """
        main function. takes command line parameters with argparse and runs letter frequency activity
        :return: none
        """
    # argparse to read command line parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='a comma separated value unigram file')
    parser.add_argument("-o", "--output", action='store_true', help='display letter frequencies to standard output')
    parser.add_argument('-p', '--plot', action='store_true', help='plot letter frequencies using matplotlib')
    args = parser.parse_args()
    filename = args.filename

    # error check file command line argument
    if not os.path.exists(filename):
        exit("ERROR: " + filename + " does not exist!")

    # read in words from file
    words = read_words(filename)

    # calculate letter frequency and total letter occurrences
    letters, total = count_letters(words)

    # if -o is specified
    if args.output:
        # print each letter and letter frequency to standard output
        for letter in letters:
            print(letter + ': ' + str(letters[letter] / total))

    # if -p is specified
    if args.plot:
        # plot data
        plot_data(letters, filename, total)


if __name__ == '__main__':
    main()