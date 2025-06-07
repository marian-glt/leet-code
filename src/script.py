"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "()[]{}"
Output: true
Example 3:
Input: s = "(]"
Output: false
Example 4:
Input: s = "([])"
Output: true
Example 5:
Input:s ="(((((]}))"""
from collections import deque
#create a dictionary of open-close pairs for each bracket
#iterate through the string
#if char is an open bracket add it to a stack
#if char is a closed bracket check if top of the stack is its matching open
#if stack is empty or stack item is not corresponding match exit
#return stack == empty

def validate_string(text: str) -> bool:
    pairsDict = {"(": ")", "[": "]", "{": "}"}
    bracketStack = deque()
    for char in text:
        if char in pairsDict:
            bracketStack.append(char)
        else:
            if(not bracketStack or char != pairsDict[bracketStack.pop()]):
                return False
    
    return not bracketStack

testArr = [
    "()", 
    "()[]{}", 
    "(]", 
    "([])", 
    "(((((]}))",
    "",                # empty string, should be True
    "([{}])",          # nested, should be True
    "([)]",            # incorrect nesting, should be False
    "{[()]}",          # nested, should be True
    "{[(])}",          # incorrect nesting, should be False
    "(((((((((())))))))))", # many nested, should be True
    "(((((((()",       # only opens, should be False
    "())",             # closes before open, should be False
    "[",               # single open, should be False
    "]",               # single close, should be False
    "({[]})[]{}",      # multiple valid groups, should be True
    "({[}])",          # wrong close, should be False
    "(([]){})",        # nested and sequential, should be True
    "(([]){})]",       # extra close, should be False
    "([[[[[[[[]]]]]]]])", # deep nesting, should be True
    "([[[[[[[[]]]]]]]])]", # deep nesting with extra close, should be False
]

for item in testArr:
    print(item + " " + str(validate_string(item)))