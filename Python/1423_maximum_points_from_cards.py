class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        leftP, rightP = k - 1, len(cardPoints) - 1
        maxValue = sum(cardPoints[0:k])
        tempSum = maxValue
        
        for _ in range(k):
            tempSum = tempSum - cardPoints[leftP] + cardPoints[rightP]
            leftP -= 1
            rightP -= 1
            maxValue = max(maxValue, tempSum)
    
        return maxValue
    
sol = Solution()
ans = sol.maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3)
print(f'This is the ans: {ans}')