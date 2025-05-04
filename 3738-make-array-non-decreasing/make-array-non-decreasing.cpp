class Solution {
public:
    int maximumPossibleSize(vector<int>& nums) {
        int ans = 0, maxNum = INT_MIN;
        for (const int& num : nums) {
            if (num >= maxNum) {
                ++ans;
                maxNum = num;
            }
        }
        return ans;
    }
};