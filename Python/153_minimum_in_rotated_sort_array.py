class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i] > nums[i+1]:
                return nums[i+1]
            elif nums[len(nums)-i-1] < nums[len(nums)-i-2]:
                return nums[len(nums)-i-1]
            elif (i+1 == len(nums)-i-1 and nums[i] < nums[i+1]) or (i == len(nums)-i-1):
                return nums[0]
            
sol = Solution()
ans = sol.findMin([3, 4, 5, 1, 2])
print(f'This is the ans: {ans}')