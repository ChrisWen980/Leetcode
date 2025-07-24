class Solution:
    def search(self, nums: list[int], target: int) -> int:
        startInd, midInd, endInd = 0, len(nums)//2, len(nums)-1
        while startInd <= endInd:
            if target == nums[midInd]:
                return midInd
            
            if nums[startInd] <= nums[midInd]:
                if nums[startInd] <= target and target <= nums[midInd]:
                    endInd = midInd - 1
                else:
                    startInd = midInd + 1
            else:
                if nums[midInd] <= target and target <= nums[endInd]:
                    startInd = midInd + 1
                else:
                    endInd = midInd - 1
            midInd = (startInd + endInd) // 2
                
        if nums[startInd] == target:
            return startInd
        return -1
            
sol = Solution()
ans = sol.search([4, 5, 6, 7, 0, 1, 2], 0)
print(f'This is the ans: {ans}')