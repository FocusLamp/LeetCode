class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = difualtdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        
        count = [1] * n
        res = [0] * n
        
        
        def first_DFS(node, parent):
            for child in graph[node]:
                if child != parent:
                    
                    first_DFS(child, node)
                    
                    count[node] += count[child]
                    res[node] += res[child] + count[child]
        
        
        def second_DFS(node, parent):
            for child in graph[node]:
                if child != parent:
                    res[child] = res[node] - count[child] + (n - count[child])
                    
                    second_DFS(child, node)
        
        
        first_DFS(0, -1)
        second_DFS(0, -1)
        
        
        return res
