from collections import defaultdict, deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        candidates = deque()
        leaving = defaultdict(int)
        output = []
        
        for i in range(len(nums)):
            while len(candidates) and nums[i] > candidates[-1]:
                rightval = candidates.pop()
                leaving[rightval] -= 1
            candidates.append(nums[i])

            if i >= k-1:
                output.append(candidates[0])
                leaving[nums[i-(k-1)]] += 1
                print(f'leaving: {leaving}, candidates: {candidates}, output: {output}')
            
            while len(candidates) and leaving[candidates[0]] > 0:
                leftval = candidates.popleft()
                leaving[leftval] -= 1
                
        return output
    

sol = Solution()
ans = sol.maxSlidingWindow(nums = [9,10,9,-7,-4,-8,2,-6], k = 5)   # [3,3,5,5,6,7]
print(f'This is the ans: {ans}')