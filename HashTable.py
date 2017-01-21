"""
Hash Tables: Ransom Note
https://www.hackerrank.com/challenges/ctci-ransom-note

A kidnapper wrote a ransom note but is worried it will be traced back to him. 
He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. 
The words in his note are case-sensitive and he must use whole words available in the magazine, meaning he cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
"""
from collections import Counter


def ransom_note(magazine, ransom):
    mag_ctr = Counter(magazine)    
    ran_ctr = Counter(ransom)
    mag_ctr.subtract(ran_ctr)
    for n in mag_ctr.values():
        if n < 0:
            return False
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
if m >= n:
    answer = ransom_note(magazine, ransom)
    if(answer):
        print("Yes")
    else:
        print("No")
else:
    print("No")