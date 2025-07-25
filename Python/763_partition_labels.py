class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # This following line will overwrite dictionary entry any time a letter is added again, meaning the rightmost letter will be used.
        rightMost = {char: index for index, char in enumerate(s)} 
        partitions = [rightMost[s[0]]+1]
        partitionSum = rightMost[s[0]]+1
        for i in range(1, len(s)):
            print(f'This is partitions: {partitions}')
            if i+1 > partitionSum:
                partitions.append(rightMost[s[i]]+1 - partitionSum)
                partitionSum = rightMost[s[i]]+1
            elif rightMost[s[i]]+1 - (partitionSum - partitions[-1]) > partitions[-1] and i+1 < partitionSum:
                partitions[-1] = rightMost[s[i]]+1 - (partitionSum - partitions[-1])
                partitionSum = rightMost[s[i]]+1        
        return partitions
        
sol = Solution()
ans = sol.partitionLabels('ababcbacadefegdehijhklij')
print(f'This is the ans: {ans}')