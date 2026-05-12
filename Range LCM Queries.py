'''Range LCM Queries:--

Given an array arr[]  and a list of queries queries[][]. Each query can be one of the following two types:

Update Query: [1, index, value] --> Update the element at position index in the array to the given value.
Range Query: [2, L, R] --> Compute and return the Least Common Multiple (LCM) of all elements in the subarray from index L to R (inclusive).
Process all queries sequentially and return a list containing the results of all Type 2 queries.

Note: All operations follow 0-based indexing.

Examples :

Input: arr[] = [2, 3, 4, 6, 8, 16], queries[][] = [[2, 0, 2], [1, 3, 8], [2, 2, 5]]
Output: [12, 16]
Explanation: The queries are processed sequentially, updating the array when required.
[2, 0, 2]: LCM of [2, 3, 4] = 12
[1, 3, 8]: array becomes [2, 3, 4, 8, 8, 16]
[2, 2, 5]: LCM of [4, 8, 8, 16] = 16
Input: arr[] = [1, 2, 3, 4],  queries[][] = [[2, 0, 3], [1, 0, 5], [2, 0, 1]]
Output: [12, 10]
Explanation: The queries are processed sequentially, updating the array when required.
[2, 0, 3]: LCM of [1, 2, 3, 4] = 12
[1, 0, 5]: array becomes [5, 2, 3, 4]
[2, 0, 1]: LCM of [5, 2] = 10
Constraints:
1 ≤ arr.size() ≤ 104
1 ≤ queries.size() ≤ 105
0 ≤ L ≤ R ≤ arr.size() - 1
0 ≤ index ≤ arr.size() - 1
1 ≤ arr[i], value ≤ 104'''

# Solution:--

import math

class Solution:
    def RangeLCMQuery(self, arr, queries):
        n = len(arr)
        tree = [0] * (4 * n)
        
        def lcm(a, b):
            if a == 0 or b == 0: return a + b
            return (a * b) // math.gcd(a, b)

        def build(node, start, end):
            if start == end:
                tree[node] = arr[start]
                return
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            tree[node] = lcm(tree[2 * node + 1], tree[2 * node + 2])

        def update(node, start, end, idx, val):
            if start == end:
                tree[node] = val
                return
            mid = (start + end) // 2
            if idx <= mid: update(2 * node + 1, start, mid, idx, val)
            else: update(2 * node + 2, mid + 1, end, idx, val)
            tree[node] = lcm(tree[2 * node + 1], tree[2 * node + 2])

        def query(node, start, end, l, r):
            if r < start or end < l: return 1
            if l <= start and end <= r: return tree[node]
            mid = (start + end) // 2
            return lcm(query(2 * node + 1, start, mid, l, r), 
                       query(2 * node + 2, mid + 1, end, l, r))

        build(0, 0, n - 1)
        res = []
        for q in queries:
            if q[0] == 1: update(0, 0, n - 1, q[1], q[2])
            else: res.append(query(0, 0, n - 1, q[1], q[2]))
        return res