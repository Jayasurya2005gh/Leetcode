class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
          unordered_map<int, int> freq;
        int goodPairs = 0;

        for (int num : nums) {
            goodPairs += freq[num]; // Add the current frequency to the count
            freq[num]++; // Increment the frequency of the current number
        }

        return goodPairs;
    }
};