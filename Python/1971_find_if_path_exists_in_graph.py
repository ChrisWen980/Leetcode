from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adjaList = defaultdict(list)
        for u, v in edges:
            adjaList[u].append(v)
            adjaList[v].append(u)
        print(adjaList)
        
        # def dfs(node, seen):
        #     if node == destination:
        #         return True
        #     seen.add(node)
        #     for nextNode in adjaList[node]:
        #         if nextNode not in seen:
        #             if dfs(nextNode, seen):
        #                 return True
        #     return False
        # return dfs(source, set())
        
        open = deque()
        seen = set()
        open.append(source)
        while open:
            currNode = open.popleft()
            if currNode == destination:
                return True
            elif currNode not in seen:
                for nextNode in adjaList[currNode]:
                    open.append(nextNode)
            seen.add(currNode)
        return False
    
sol = Solution()
ans = sol.validPath(3, [[0,1],[1,2],[2,0]], 0, 2)
print(f'This is the ans: {ans}')