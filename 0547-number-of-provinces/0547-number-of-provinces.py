class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False]*n
        def DFS(node):
            visited[node]=True
            for nei in range(n):
                if isConnected[node][nei]==1 and not visited[nei]:
                    DFS(nei)
        count=0
        for i in range(n):
            if not visited[i]:
                DFS(i)
                count+=1
        return count