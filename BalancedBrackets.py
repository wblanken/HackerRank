"""
Stacks: Balanced Brackets
https://www.hackerrank.com/challenges/ctci-balanced-brackets

A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. 
There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. 
For example, {[(])} is not balanced because the contents in between { and } are not balanced. 
The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is considered to be balanced if the following conditions are met:
- It contains no unmatched brackets.
- The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.

Given n strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, print YES on a new line; otherwise, print NO on a new line.
"""
from collections import deque


def check_brackets(brackets):
    is_balanced = False
    front = brackets.popleft()
    back = brackets.pop()
    
    if front == '{' and back == '}':
        is_balanced = True
    elif front == '[' and back == ']':
        is_balanced = True
    elif front == '(' and back == ')':
        is_balanced = True

    if is_balanced == True and len(brackets) > 0:
        is_balanced = check_brackets(brackets)

    return is_balanced


def is_matched(expression):
    if len(expression) % 2 == 0:
        brackets = deque(expression)
        return check_brackets(brackets)        
    return False
    

# Test input and find failures
infile = open("test cases/Bracket_Test_In.txt", 'r')
outfile = open("test cases/Bracket_Test_Out.txt", 'r')

t = infile.readline()
inputs = infile.readlines()
answers = outfile.readlines()
for a0 in range(int(t.strip())):
    expression = inputs[a0].strip()
    expected_result = True if answers[a0] == "YES" else False
    if is_matched(expression) == expected_result:
        print(str(a0) + " PASS")
    else:
        print(str(a0) + " FAIL")

# t = int(input().strip())
# for a0 in range(t):
#     expression = input().strip()
#     if is_matched(expression) == True:
#         print("YES")
#     else:
#         print("NO")
