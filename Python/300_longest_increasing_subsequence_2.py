class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        sortedNums = [nums[0]]
        
        for i in range(len(nums)):
            # add to the stack
            if nums[i] > sortedNums[-1]:
                sortedNums.append(nums[i])
            # if its equal to the last value just skip the replace search
            elif nums[i] == sortedNums[-1]:
                continue
            # if its less than we can replace the smallest value possible with nums[i], maintaining old equality in array and allowing for a larger stack to possibly be formed
            else:
                # binary search for smallest possible value to replace
                L, R = 0, len(sortedNums)
                numNotFound = True
                  
                while L != R and numNotFound:
                    M = (L + R) // 2
                    if nums[i] < sortedNums[M]:
                        R = M
                    # moves in case it gets stuck
                    elif nums[i] > sortedNums[M]:
                        L = M + 1
                    else:
                        numNotFound = False
                # If number already exists we don't need to replace as we only account for strictly increasing
                if L == R and nums[i] < sortedNums[L]:
                    sortedNums[L] = nums[i]
        
        return len(sortedNums)
    
sol = Solution()
ans = sol.lengthOfLIS([1, 3, 5, 7, 9, 4])
print(f'This is the ans: {ans}')