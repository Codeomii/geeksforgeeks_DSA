'''Anagram Palindrome:--

Given a string s, determine whether its characters can be rearranged to form a palindrome. Return true if it is possible to rearrange the string into a palindrome; otherwise, return false.

Examples

Input: s = "baba"
Output: true
Explanation: Can be rearranged to form a palindrome "abba" 
Input: s = "geeksogeeks"
Output: true
Explanation: The characters of the string can be rearranged to form the palindrome "geeksoskeeg".

Input: s = "geeksforgeeks"
Output: false
Explanation: The given string can't be converted into a palindrome.
Constraints:
1 ≤ s.length ≤ 106
s consists of only lowercase English letters.

'''

# Solution:--

class Solution:
    def canFormPalindrome(self, s):
        seen = set()

        for ch in s:
            if ch in seen:
                seen.remove(ch)
            else:
                seen.add(ch)

        return len(seen) <= 1