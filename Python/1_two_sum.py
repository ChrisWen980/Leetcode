class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        remainder = 0
        hashMap = {}
        for i in range(len(nums)):
          #print(f'this is nums[i]: {nums[i]}')
          remainder = target - nums[i]
          if remainder in hashMap:
            return [i, hashMap[remainder]]
          if nums[i] not in hashMap:
            hashMap[nums[i]] = i

sol = Solution()
solList = sol.twoSum([4, 2, 3, 1], 5)
print(f'The solution is at indices: {solList[0]}, {solList[1]}')
