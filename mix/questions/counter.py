# 84. Write a program for counting the number of every character of a given text file.
import collections
import pprint

with open('someRandomWord.txt', 'r') as f:
    counter_char = collections.Counter(f.read().upper())
    # print(counter_char)
    count_value = pprint.pformat(counter_char)
    print(count_value)