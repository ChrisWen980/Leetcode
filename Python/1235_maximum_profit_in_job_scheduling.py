# https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/

from bisect import bisect_left

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        memoizationTable = [0 for _ in range(len(startTime))]
        jobs = []
        
        # Create list of jobs and sort it
        for i in range(len(startTime)):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort()
        
        # Create second list to use for binary search
        for i in range(len(jobs)):
            startTime[i] = jobs[i][0]
            
        def find_next_largest(startTime, target):
            #  Binary search to find the first index where the value is >= target
            idx = bisect_left(startTime, target)
            
            # If idx is within the list range we have the next job
            if idx < len(startTime):
                return idx
            return len(startTime) # No value is larger than the target then we have reached end of jobs
        
        
        def findMaxProfit(jobs, startTime, numOfJobs, startPos):
            
            # If we have looped over every job
            if startPos == numOfJobs:
                return 0
            
            # If we have already found the maximum for this position just return it
            if memoizationTable[startPos] > 0:
                return memoizationTable[startPos]
            
            # Find the next smallest position you can take assuming you take the current job
            nextPos = find_next_largest(startTime, jobs[startPos][1])

            # Find the maximum profit between skipping or taking
            maxProf = max(findMaxProfit(jobs, startTime, numOfJobs, startPos + 1), jobs[startPos][2] + findMaxProfit(jobs, startTime, numOfJobs, nextPos))
            memoizationTable[startPos] = maxProf
            
            return maxProf
        
        return findMaxProfit(jobs, startTime, len(startTime), 0)
        
    
sol = Solution()
ans = sol.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70])
print(f'This is the ans: {ans}')