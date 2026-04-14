''' Next Smallest Palindrome

Given a number, in the form of an array num[] containing digits from 1 to 9(inclusive). Find the next smallest palindrome strictly larger than the given number.

Examples:

Input: num[] = [9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2]
Output: [9, 4, 1, 8, 8, 0, 8, 8, 1, 4, 9]
Explanation: Next smallest palindrome is 9 4 1 8 8 0 8 8 1 4 9.
Input: num[] = [2, 3, 5, 4, 5]
Output: [2, 3, 6, 3, 2]
Explanation: Next smallest palindrome is 2 3 6 3 2.
Constraints:
1 ≤ n ≤ 105
1 ≤ num[i] ≤ 9'''

# Solution:--

class Solution:
    def nextPalindrome(self, num):
        n=len(num)
        if all(x==9 for x in num): return [1]+[0]*(n-1)+[1]
        res=num[:]
        for i in range(n//2): res[n-i-1]=res[i]
        if res>num: return res
        i=(n-1)//2
        while i>=0 and res[i]==9: res[i]=res[n-i-1]=0; i-=1
        res[i]+=1; res[n-i-1]=res[i]
        return res