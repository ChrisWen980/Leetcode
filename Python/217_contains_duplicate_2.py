class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seenNums = set()
        for num in nums:
            if num not in seenNums:
                seenNums.add(num)
            else:
                return True
        return False


sol = Solution()
result = sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
print(f'This is result: {result}')