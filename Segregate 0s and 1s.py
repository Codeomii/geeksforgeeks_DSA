''' Segregate 0s and 1s----

Given an array arr[] consisting of only 0's and 1's. Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.

Examples :

Input: arr[] = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
Explanation:  After segregation, all the 0's are on the left and 1's are on the right. Modified array will be [0, 0, 0, 0, 0, 1, 1, 1, 1, 1].
Input: arr[] = [1, 1]
Output: [1, 1]
Explanation: There are no 0s in the given array, so the modified array is [1, 1]
Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 1'''

# Solution:--

class Solution:
    def segregate0and1(self, arr):
        l, r = 0, len(arr) - 1
        while l < r:
            if arr[l] == 1 and arr[r] == 0:
                arr[l], arr[r] = arr[r], arr[l]
            if arr[l] == 0: l += 1
            if arr[r] == 1: r -= 1