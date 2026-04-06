'''Given a string s of distinct characters and their corresponding frequency f[ ] i.e. character s[i] has f[i] frequency. You need to build the Huffman tree and return all the huffman codes in preorder traversal of the tree.
Note: While merging if two nodes have the same value, then the node which occurs at first will be taken on the left of Binary Tree and the other one to the right, otherwise Node with less value will be taken on the left of the subtree and other one to the right.

Examples:

Input: s = "abcdef", f[] = {5, 9, 12, 13, 16, 45}
Output: [0, 100, 101, 1100, 1101, 111]
Explanation:

HuffmanCodes will be:
f : 0
c : 100
d : 101
a : 1100
b : 1101
e : 111
Constraints:
1 ≤ s.size() = f.size() ≤ 26'''

# Solution:--

import heapq

class Node:
    def __init__(self, val=None, sum_=0, idx=-1):
        self.val = val
        self.sum = sum_
        self.idx = idx
        self.left = None
        self.right = None

    # needed for heap comparison
    def __lt__(self, other):
        if self.sum != other.sum:
            return self.sum < other.sum
        return self.idx < other.idx

def preorder(root, path, mp):
    if not root:
        return
    
    if root.val is not None:
        mp[root.val] = path if path != "" else "0"
    
    preorder(root.left, path + '0', mp)
    preorder(root.right, path + '1', mp)


class Solution:
    def huffmanCodes(self, s, f):
        # code here
        pq = []
        
        for i in range(len(s)):
            heapq.heappush(pq, Node(s[i], f[i], i))
        
        while len(pq) > 1:
            t1 = heapq.heappop(pq)
            t2 = heapq.heappop(pq)
            
            temp = Node(None, t1.sum + t2.sum, min(t1.idx, t2.idx))
            temp.left = t1
            temp.right = t2
            
            heapq.heappush(pq, temp)
        
        mp = {}
        preorder(pq[0], "", mp)
        
        return sorted([mp[ch] for ch in s])