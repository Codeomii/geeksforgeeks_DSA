'''
👩‍💻Print Diagonally:--

Difficulty: EasyAccuracy: 66.11%Submissions: 53K+Points: 2Average Time: 10m
Give a n * n square matrix mat[][], return all the elements of its anti-diagonals from top to bottom.

Examples :

Input: n = 2, mat[][] = [[1, 2],
                        [3, 4]]
Output: [1, 2, 3, 4]
Explanation: 

Input: n = 3, mat[][] = [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]]
Output: [1, 2, 4, 3, 5, 7, 6, 8, 9]
Explanation: 

Constraints:
1 ≤ n ≤ 103
0 ≤ mat[i][j] ≤ 106'''

# Solution:--

class Solution:
    def diagView(self, mat):
        n=len(mat);res=[]
        for c in range(n):
            i,j=0,c
            while i<n and j>=0:
                res.append(mat[i][j]);i+=1;j-=1
        for r in range(1,n):
            i,j=r,n-1
            while i<n and j>=0:
                res.append(mat[i][j]);i+=1;j-=1
        return res