'''Remove Invalid Parentheses:--

Given a string s consisting of lowercase letters and parentheses '(' and ')'.

A string is considered valid if:

Every opening parenthesis '(' has a corresponding closing parenthesis ')'.
Parentheses are properly nested.
Remove the minimum number of invalid parentheses from s so that the resulting string becomes valid.  Return all the possible distinct valid strings in lexicographically sorted order.

Examples :

Input:  = "()())()"
Output: ["(())()", "()()()"]
Explanation: 
The string "()())()" has one extra ')', making it invalid. By removing one ')', we can make it valid in two ways:
Remove the 3rd index ')' -> "(())()"
Remove the 4th index ')' -> "()()()"
Both are valid and require the minimum removals.

Input: s = "(a)())()"
Output: ["(a())()", "(a)()()"]
Explanation: 
We remove one ')' (minimum removals) to make it valid. Possible valid results:
Remove a ')' -> "(a())()"
Remove another ')' -> "(a)()()"

Input: s = ")("
Output: [""]
Explanation: The string ")(" is invalid. Removing both parentheses (minimum removals) gives an empty string "", which is valid.
Constraints:
1 ≤ |s| ≤ 20
s consists of lowercase English letters and parentheses '(' and ') only.'''

# Solution:--

class Solution:
    def validParenthesis(self, s):
        def is_valid(st):
            bal = 0
            for ch in st:
                if ch == '(':
                    bal += 1
                elif ch == ')':
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0
        
        level = {s}
        
        while True:
            valid = sorted([st for st in level if is_valid(st)])
            
            if valid:
                return valid
            
            nxt = set()
            
            for st in level:
                for i in range(len(st)):
                    if st[i] in '()':
                        nxt.add(st[:i] + st[i+1:])
            
            level = nxt