class Solution:
    def canJump(self, nums: list[int]) -> bool:
        dpList = [False] * len(nums)
        dpList[0] = True
        target, furthestJump = len(nums), 0
        print(dpList)
        for i in range(len(nums)):
            if dpList[i] == False:
                return False
            elif i+nums[i] >= target:
                print(i+nums[i], target)
                return True
            elif i+nums[i] > furthestJump:
                for j in range(furthestJump, i+nums[i]+1):
                    dpList[j] = True
                furthestJump = i+nums[i]
                print(dpList)
        return True
    
sol = Solution()
ans = sol.canJump([0])
print(f'This is the ans: {ans}')