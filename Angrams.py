"""
Strings: Making Anagrams
https://www.hackerrank.com/challenges/ctci-making-anagrams

Alice is taking a cryptography class and finding anagrams to be very useful.
We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string.
In other words, both strings must contain the same exact letters in the same exact frequency.
For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on
the minimum number of character deletions required to make the two strings anagrams.
Can you help her find this number?

Given two strings, a and b, that may or may not be of the same length,
determine the minimum number of character deletions required to make a and b anagrams.
Any characters can be deleted from either of the strings.
"""

'''
def number_needed(a, b):
    if a == b:
        return 0
    a_list = list(a)
    a_list.sort()
    b_list = list(b)
    b_list.sort()
    b_index = 0
    rem_count = 0

    for i in range(len(a_list)):
        if a_list[i] == b_list[b_index]:
            b_index += 1
        else:
            if a_list[i] in b_list[b_index:]:
                next_index = b_list[b_index:].index(a_list[i]) + b_index
                rem_count += next_index - b_index
                b_index = next_index
            elif a_list[i] > b_list[b_index]:
                rem_count += 1
            else:
                rem_count += 1
                b_index += 1
        if b_index >= len(b_list):
            if i < len(a_list):
                rem_count += len(a_list[i:]) - 1
            return rem_count
        if i == len(a_list):
            rem_count += len(b_list[b_index:])
    return rem_count
'''

''' This is close but doesn't account for left over values
def number_needed(a, b):
    rem_count = 0
    if a != b:
        a_list = list(a)
        a_list.sort()
        b_list = list(b)
        b_list.sort()
        a_i = 0
        b_i = 0
        length = len(a_list) if len(a_list) > len(b_list) else len(b_list)

        for n in range(length):
            if a_list[a_i] == b_list[b_i]:
                a_i += 1
                b_i += 1
            else:
                if a_list[a_i] > b_list[b_i]:
                    if a_list[a_i] not in b_list[b_i:]:
                        rem_count += 1
                        a_i += 1
                    b_i += 1
                    rem_count += 1
                else:
                    if b_list[b_i] not in a_list[a_i:]:
                        rem_count += 1
                        b_i += 1
                    a_i += 1
                    rem_count += 1
    return rem_count
'''

# a = input().strip()
# b = input().strip()

# b = 'aafluhefuisfliusdjflzxackfj'
# a = 'faewfouifalkfjfawoigjfgaewgkljs'

from collections import Counter

def number_needed(a, b):
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    return sum(abs(i) for i in ct_a.values())

a = 'cde'
b = 'abc'

#a = 'fcrxzwscanmligyxyvym'
#b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

print(number_needed(a, b))

# a a a c d e f f f f f h i i j j k l l l s s u u u x z
# a a a a e e f f f f f f g g g i i j j j k k l l o o s u w w w

# 22
# a a a e f f f f f i i j j k l l s u
# a a a e f f f f f i i j j k l l s u
