from collections import defaultdict, deque

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        adjaList = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected[i])):
                if isConnected[i][j] == 1:
                    adjaList[i].append(j)
                    adjaList[j].append(i)
        #print(adjaList)
        
        seen = [False] * len(isConnected)
        provs = 0
        
        def dfs(node):
            for nextNode in adjaList[node]:
                if seen[nextNode] == False:
                    seen[nextNode] = True
                    dfs(nextNode)
        
        for i in range(len(isConnected)):
            if seen[i] == False:
                provs += 1
                dfs(i)
        return provs
    
sol = Solution()
ans = sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]])
print(f'This is the ans: {ans}')