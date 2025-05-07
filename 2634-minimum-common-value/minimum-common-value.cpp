class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int i = 0, j = 0;

        // Two-pointer approach to find the smallest common value
        while (i < nums1.size() && j < nums2.size()) {
            if (nums1[i] == nums2[j]) {
                return nums1[i]; // Found the smallest common value
            } else if (nums1[i] < nums2[j]) {
                i++; // Move the pointer in nums1
            } else {
                j++; // Move the pointer in nums2
            }
        }

        // We should never reach here because a common element is guaranteed
        return -1; 
    }
};
