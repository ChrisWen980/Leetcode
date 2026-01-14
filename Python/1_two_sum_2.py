class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numDict = {}
        for i in range(len(nums)):
            if target - nums[i] in numDict:
                return numDict[target - nums[i]], i
            else:
                numDict[nums[i]] = i
        return

sol = Solution()
solList = sol.twoSum([4, 2, 3, 1], 5)
print(f'The solution is at indices: {solList[0]}, {solList[1]}')
