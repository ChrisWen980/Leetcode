class Solution:
    def search(self, nums: list[int], target: int) -> int:
        L, R = 0, len(nums)-1
        
        while L < R:
            M = (L + R) // 2
            print(L, R, M)
            if nums[M] < nums[R]:
                # M != R unless L = R
                if nums[R] >= target and target > nums[M]:
                    L = M+1
                else:
                    R = M
            else:
                # L = M is possible
                if nums[M] >= target and target >= nums[L]:
                    R = M
                else:
                    L = M+1
        print(L, R, M)
        if nums[L] == target:
            return L
        return -1
            
sol = Solution()
ans = sol.search([3, 1], 3)
print(f'This is the ans: {ans}')


