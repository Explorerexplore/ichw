#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "WangTong"
__pkuid__  = "1700011771"
__email__  = "1700011771@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """

    for i in lines:
        if not(i.isalpha()):
            lines = lines.replace(i, ' ')
    words_list = lines.split()
    d = {}
    for word in words_list:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    alist = list(d.items())
    alist.sort(reverse = True, key = lambda t:t[1])
    for i in range(topn):
        print(alist[i][0], alist[i][1], sep = '\t')
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
