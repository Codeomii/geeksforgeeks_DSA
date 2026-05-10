'''Count Spanning Trees in a Graph:--

Given a connected undirected graph with n vertices and m edges, where each edge is represented as edges[i]=[u,v]  indicating an edge between vertices u and v.

Determine the total number of distinct spanning trees that can be formed from the graph.

Note: A spanning tree is a subgraph of the given graph that includes all n vertices, has exactly n-1 edges, is connected, and contains no cycles; therefore, every connected undirected graph always has at least one spanning tree.

Examples:

Input: n = 6, edges = [[0, 3], [0, 1], [1, 2], [1, 5], [3, 4]]
Output: 1
Explanation: The graph has 6 vertices and 5 edges, and it is connected, so it is already a tree (m = n-1). A tree has only one spanning tree, which is the graph itself, so the answer is 1.

Input: n = 3, edges = [[0, 1], [0, 2], [1, 2]]
Output: 3
Explanation: There are exactly 3 possible spanning trees for the given graph. 

Input: n = 1, edges = []
Output: 1
Explanation: With 1 vertex, a spanning tree needs 0 edges. The graph already satisfies this, so the answer is 1.
Constraints:
1 ≤ n ≤ 10
n -1  ≤ m ≤ n*(n-1)/2
0 ≤ edges[i][0], edges[i][1] ≤ n-1'''

# Solution:--

class Solution:
    def countSpanTree(self,n,e):
        a=[[0]*n for _ in range(n)]
        for u,v in e:a[u][u]+=1;a[v][v]+=1;a[u][v]-=1;a[v][u]-=1
        a=[r[1:] for r in a[1:]];d=1
        for i in range(n-1):
            for j in range(i+1,n-1):
                f=a[j][i]/a[i][i]
                for k in range(i,n-1):a[j][k]-=f*a[i][k]
            d*=a[i][i]
        return round(abs(d))