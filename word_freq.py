"""
Hayden Orth
Activity 3: word frequency
Project 1
CSCI 0242
"""
import argparse
import os.path
import operator
# import read_words function from word_count file
from word_count import read_words
import matplotlib.pyplot as plt


def sort_by_value(words: dict) -> dict:
    """
    reverse sorts the word dictionary by value. the highest frequency is first, lowest is last
    :param words: unsorted dictionary of words
    :return: dictionary reverse sorted by value
    """
    sorted_words_temp = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
    sorted_d = dict()
    for element in sorted_words_temp:
        sorted_d[element[0]] = element[1]
    return sorted_d


def rank_as_value(words: dict):
    """
    creates a dictionary with words as keys and word rank as values
    creates a list of ranks
    creates a list of frequencies from sorted word dictionary
    :param words: words dictionary sorted from most to least frequent
    :return: rank dictionary, rank list, frequency list
    """
    rank_dict = dict()
    rank_list, freq_list = [], []
    count = 1
    for word in words:
        rank_dict[word] = count
        freq_list.append(words[word])
        rank_list.append(count)
        count += 1
    return rank_dict, rank_list, freq_list


def main():
    """
     main function. takes command line parameters and runs word frequency activity
     calls functions to sort word frequencies and ranks, prints and plots data if specified
     :return: none
     """
    # argparse to read command line parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='display the top OUTPUT ranked words by number of occurrences',
                        action='store_true')
    parser.add_argument('OUTPUT', type=int, help='number of ranked words to display')
    parser.add_argument('-p', '--plot', action='store_true', help='plot the word rankings from top to bottom based' +
                                                                  ' on occurrences')
    parser.add_argument('word', help='a word to display the overall ranking of')
    parser.add_argument('filename', help='a comma separated value unigram file')
    args = parser.parse_args()
    word = args.word
    filename = args.filename
    if args.OUTPUT:
        num = args.OUTPUT

    # error check file command line argument
    if not os.path.exists(filename):
        exit("ERROR: " + filename + " does not exist!")

    # read words from file using read_words
    words = read_words(filename)

    # sort words by value
    sorted_words = sort_by_value(words)

    # create dict with word ranks as values
    # creates lists or ranks and frequencies
    rank_dict, rank_list, freq_list = rank_as_value(sorted_words)

    # print selected word info from command line
    if word in sorted_words:
        print(word + ' is ranked #' + str(rank_dict[word]))
    else:
        exit(word + ' does not appear in ' + filename)

    # display output if requested
    rank = 1
    if args.output:
        for W in sorted_words:
            if rank <= num:
                print('#' + str(rank) + ': ' + W + ' -> ' + str(sorted_words[W]))
                rank += 1
            else:
                break

    # plot if requested
    if args.plot:
        plt.loglog(rank_list, freq_list, 'o')
        plt.plot(rank_dict[word], sorted_words[word], '*')
        plt.annotate(word, xy=(rank_dict[word], sorted_words[word]), xycoords='data')

        plt.title('Word Frequencies: ' + filename)
        plt.xlabel('Rank of word ("' + word + '" is rank ' + str(rank_dict[word]) + ')')
        plt.ylabel('Total number of occurrences')

        plt.show()


if __name__ == '__main__':
    main()
