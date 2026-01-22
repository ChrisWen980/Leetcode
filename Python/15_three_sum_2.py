class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = []
        
        for i in range(0, len(nums)-2):
            if nums[i] > 0:
                return triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j != k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return triplets
    
sol = Solution()
solList = sol.threeSum([-1,0,1,2,-1,-4])
print(f'This is the solution: {solList}')