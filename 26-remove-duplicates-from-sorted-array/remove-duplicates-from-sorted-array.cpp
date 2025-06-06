class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        unordered_set<int> uniqueSet(nums.begin(), nums.end());
        nums.assign(uniqueSet.begin(), uniqueSet.end());
        sort(nums.begin(),nums.end());
        return nums.size();
    }
};