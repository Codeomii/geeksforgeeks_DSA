'''Palindrome Pairs:--

Given an array arr[] consisting of n strings. Determine whether there exists a pair of indices (i, j) such that i ≠ j and the concatenation arr[i] + arr[j] forms a palindrome.

Return true if such a pair exists; otherwise, return false.

Note: A string is considered a palindrome if it reads the same forward and backward.

Examples:

Input: arr[] = ["geekf", "geeks", "or", "keeg", "abc", "bc"]
Output: true
Explanation: There is a pair "geekf" and "keeg". Their concatenation "geekfkeeg" is a palindrome.
Input: arr[] = ["abc", "xyxcba", "geekst", "or", "bc"]
Output: true
Explanation: There is a pair "abc" and "xyxcba". Their concatenation "abcxyxcba" is a palindrome.
Input: arr[] = ["aa"]
Output: false
Explanation: There is only one string present, so the output is false.
Constraints:
1 ≤ n ≤ 2*104
1 ≤ |arr[i]| ≤ 10'''

# Solution:--

class Solution:
    def palindromePair(self, arr):
        pos = {w: i for i, w in enumerate(arr)}
        for i, w in enumerate(arr):
            for j in range(len(w) + 1):
                p, s = w[:j], w[j:]
                if p == p[::-1] and pos.get(s[::-1], i) != i: return True
                if s == s[::-1] and pos.get(p[::-1], i) != i: return True
        return False