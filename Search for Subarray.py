'''Search for Subarray:--

You are given two integer arrays a[] and b[]. Return all the starting indexes of all the occurences of b[] as a subarray in a[].

Examples:

Input: a[] = [2, 4, 1, 0, 4, 1, 1], b[] = [4, 1]
Output: [1, 4]
Explanation: b[] occurs as a subarray in a[] from index 1 to 2 and from index 4 to 5.

Input: a[] = [2, 4, 1, 0, 0, 3], b[] = [0]
Output: [3, 4]
Explanation: b[] occurs as a subarray in a[] from index 3 to 3 and from index 4 to 4.

Input: a[] = [1, 3, 5, 3, 0], b[] = [1, 3, 0]
Output: []
Explanation: There is no subarray occurs as b[] in a[]

Constraints:
1 ≤ a.size() ≤ 106
1 ≤ b.size() ≤ a.size()
0 ≤ b[i], a[i] ≤ 104'''

# Solution:--

class Solution:
    def search(self,a,b):
        m=len(b);l=[0]*m;j=0
        for i in range(1,m):
            while j and b[i]!=b[j]:j=l[j-1]
            j+=b[i]==b[j];l[i]=j
        r=[];j=0
        for i in range(len(a)):
            while j and a[i]!=b[j]:j=l[j-1]
            j+=a[i]==b[j]
            if j==m:r.append(i-m+1);j=l[j-1]
        return r