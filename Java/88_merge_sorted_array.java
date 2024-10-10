class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int backIndex = m + n - 1;
        m -= 1;
        n -= 1;

        while (n >= 0) {
            if (m >= 0 && nums1[m] > nums2[n]) {
                nums1[backIndex] = nums1[m];
                m -= 1;
            } else {
                nums1[backIndex] = nums2[n];
                n -= 1;
            }
            backIndex -= 1;
        }
    }
}