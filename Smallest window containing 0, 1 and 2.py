'''Smallest window containing 0, 1 and 2:-- 

Given a string s consisting only of the characters '0', '1' and '2', determine the length of the smallest substring that contains all three characters at least once.

If no such substring exists, return -1.

Examples :

Input: s = "10212"
Output: 3
Explanation: The substring "102" is the shortest substring that contains all three characters '0', '1', and '2', so the answer is 3.
I
nput: s = "12121"
Output: -1
Explanation: The character '0' is not present in the string, so no substring can contain all three characters '0', '1', and '2'. Hence, the answer is -1.
Constraints:
1 ≤ s.size() ≤ 105'''

# Solution:--

class Solution:
    def smallestSubstring(self, s):
        i, ans = 0, 10**9
        c = {'0': 0, '1': 0, '2': 0}
        
        for j in range(len(s)):
            c[s[j]] += 1
            
            while c['0'] and c['1'] and c['2']:
                ans = min(ans, j - i + 1)
                c[s[i]] -= 1
                i += 1
                
        return ans if ans != 10**9 else -1