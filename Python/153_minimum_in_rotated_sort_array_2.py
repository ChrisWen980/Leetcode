class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        L, R = 0, len(nums)-1
        while L < R:
            M = (L + R) // 2
            print(L, R, M)
            if nums[M] < nums[R]:
                R = M
            else:
                L = M + 1
        print(L, R, M)
        return nums[L]
            
sol = Solution()
ans = sol.findMin([2, 1])
print(f'This is the ans: {ans}')