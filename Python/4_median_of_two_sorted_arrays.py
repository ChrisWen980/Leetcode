class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) < len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        n1, n2 = len(nums1), len(nums2)
        if n1 == 0 and n2 == 0:
            return 0
        elif n1 == 0:
            print(n1)
            return nums2[(n2+1)/2 - 1] if n2 % 2 == 1 else (nums2[n2/2 - 1] + nums2[n2/2])/2
        elif n2 == 0:
            print(n2)
            return nums1[(n1+1)/2 - 1] if n1 % 2 == 1 else (nums1[n1/2 - 1] + nums1[n1/2])/2

        low = 0
        high = len(nums2)
        leftSize = (n1 + n2 + 1) // 2
        
        while low <= high:
            M2 = (low + high) // 2
            M1 = leftSize - M2
            
            L1, L2, R1, R2 = float('-inf'), float('-inf'), float('inf'), float('inf')
            
            if M1 < n1:
                R1 = nums1[M1]
            if M2 < n2:
                R2 = nums2[M2]
            if M1-1 >= 0:
                L1 = nums1[M1-1]
            if M2-1 >= 0:
                L2 = nums2[M2-1]
            
            if L1 <= R2 and L2 <= R1:
                if (n1 + n2) % 2 == 1:
                    return max(L1, L2)
                return (max(L1, L2) + min(R1, R2)) / 2.0
            elif L2 > R1:
                high = M2-1
            else:
                low = M2+1
        return 0
    
sol = Solution()
ans = sol.findMedianSortedArrays([], [1])
print(f'This is the ans: {ans}')