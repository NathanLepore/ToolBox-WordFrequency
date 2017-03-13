""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]
    words = "".join(lines)
    words = words.lower()
    words = "".join(words.splitlines())
    for char in string.punctuation:
        lists = words.split(char)
        for lines in lists:
            lines.replace(char, " ")
        words = "".join(lists)
    finallist = words.split()
    return finallist


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    d = dict()
    for word in word_list:
        d[word] = d.get(word, 0) + 1
    ordered_by_frequency = sorted(d, key=d.get, reverse=True)
    print(ordered_by_frequency[0: n])


list_of_words = get_word_list('pg32325.txt')
get_top_n_words(list_of_words, 100)

"""
if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(string.punctuation)
"""
