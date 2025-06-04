class Solution {
public:
    int sumOfGoodNumbers(vector<int>& nums, int k) {
        int sum = 0;
        int n = nums.size();
        
        for (int i = 0; i < n; i++) {
            // Check if both indices i-k and i+k are within bounds
            bool left_valid = (i - k >= 0);  // Check if i-k is valid
            bool right_valid = (i + k < n); // Check if i+k is valid
            
            // Check if the current number is greater than both nums[i-k] and nums[i+k] 
            // but only if the indices are valid
            if (left_valid && right_valid) {
                if (nums[i] > nums[i - k] && nums[i] > nums[i + k]) {
                    sum += nums[i];
                }
            } 
            // Handle cases when only one of the indices is valid
            else if (left_valid) {
                if (nums[i] > nums[i - k]) {
                    sum += nums[i];
                }
            } 
            else if (right_valid) {
                if (nums[i] > nums[i + k]) {
                    sum += nums[i];
                }
            }
        }
        
        return sum;
    }
};
