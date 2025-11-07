class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numsSet = set(nums)
        maxLength = 0
        
        while numsSet:
            curr = numsSet.pop()
            low, high = curr-1, curr+1
            length = 1
            while low in numsSet:
                numsSet.remove(low)
                length += 1
                low -= 1
            
            while high in numsSet:
                numsSet.remove(high)
                length += 1
                high += 1
            maxLength = max(maxLength, length)
        return maxLength
        
    
sol = Solution()
ans = sol.longestConsecutive([100,4,200,1,3,2])
print(f'This is ans: {ans}')