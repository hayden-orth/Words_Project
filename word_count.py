"""
Hayden Orth
Activity 1: word count
Project 1
CSCI 0242
"""
import argparse
import os.path


def read_words(filename: str) -> dict:
    """
    function reads words from a CSV file ans stores them in a dictionary
    key = word
    value = total occurrences
    :param filename: name of CSV file to read from
    :return: returns word dictionary
    """
    words = dict()

    with open(filename) as f:
        for line in f:
            fields = line.split(", ")
            if fields[0] not in words:
                words[fields[0]] = int(fields[2])
            else:
                words[fields[0]] += int(fields[2])
    return words


def main():
    """
    main function. takes command line parameters with argparse and runs word count functions
    :return: none
    """
    # argparse to read command line parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('word', help='a word to display the total occurances of')
    parser.add_argument('filename', help='a comma separated value unigram file')
    args = parser.parse_args()
    word = args.word
    filename = args.filename

    # error check file command line argument
    if not os.path.exists(filename):
        exit("ERROR: " + filename + " does not exist!")

    # read words from file
    words = read_words(filename)

    # error check word command line argument and print
    if word in words:
        # print output
        print(word + ": " + str(words[word]))
    else:
        exit("ERROR: " + word + " does not appear!")


if __name__ == '__main__':
    main()