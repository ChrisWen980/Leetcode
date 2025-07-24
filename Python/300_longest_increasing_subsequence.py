class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        sortedNums = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > sortedNums[-1]:
                sortedNums.append(nums[i])
            elif nums[i] == sortedNums[-1]:
                continue
            else:
                L, R = 0, len(sortedNums)
                numNotFound = True
                while L != R and numNotFound:
                    M = (L + R) // 2
                    if nums[i] < sortedNums[M]:
                        R = M
                    elif nums[i] > sortedNums[M]:
                        L = M + 1
                    else:
                        numNotFound = False
                if L == R and nums[i] < sortedNums[L]:
                    sortedNums[L] = nums[i]
        return len(sortedNums)
    
sol = Solution()
ans = sol.lengthOfLIS([10,9,2,5,3,7,101,18])
print(f'This is the ans: {ans}')