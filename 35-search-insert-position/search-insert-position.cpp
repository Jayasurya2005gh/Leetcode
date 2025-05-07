class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        int mid;
        int ans = nums.size(); // Default insert position at the end

        while (left <= right) {
            mid = (left + right) / 2;
            if (nums[mid] >= target) {
                ans = min(ans, mid); // Update potential insert position
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return ans;
    }
};