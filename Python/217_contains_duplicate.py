class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numsDict = {}
        for i in range(len(nums)):
            if nums[i] in numsDict:
                return True
            else:
                numsDict[nums[i]] = 0
        return False

sol = Solution()
result = sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
print(f'This is result: {result}')