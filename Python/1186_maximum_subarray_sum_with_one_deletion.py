class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        max_with_del, max_without_del, max_val = arr[0], arr[0], arr[0]
        
        for num in arr[1:]:
            max_with_del = max(max_with_del + num, num, max_without_del)
            max_without_del = max(max_without_del + num, num)
            max_val = max(max_val, max_with_del, max_without_del)
        
        return max_val
    


sol = Solution()
ans = sol.maximumSum([1,-2,0,3])
print(f'This is the ans: {ans}')