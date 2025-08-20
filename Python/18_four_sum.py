class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        ans = []
        #print(f'nums: {nums}')
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k, l = j+1, len(nums)-1
                currTotal = nums[i] + nums[j]
                while k < l:
                    #print(i, j, k, l)
                    if currTotal + nums[k] + nums[l] == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                    if currTotal + nums[k] + nums[l] >= target:
                        l -= 1
                        while l > k and nums[l] == nums[l+1]:
                            l -= 1
                    else:
                        k += 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
        return ans
    
sol = Solution()
solList = sol.fourSum([1,0,-1,0,-2,2], 0)
print(f'This is the solution: {solList}')