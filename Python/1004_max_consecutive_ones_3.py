from collections import deque

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        pointers = deque()
        maxsubstr, start = 0, 0
        
        for end in range(len(nums)):
            if nums[end] == 0:
                pointers.append(end)
            while len(pointers) > k:
                start = pointers.popleft() + 1  # even if this val was a 0 it will be another pointer
            
            maxsubstr = max(maxsubstr, end - start + 1)
        return maxsubstr
    
    
sol = Solution()
ans = sol.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3) # ans = 10
print(f'This is ans: {ans}')