class Solution {
public:
    void permutations(vector<int>& nums, vector<int>& curr,
                      vector<bool>& visited, vector<vector<int>> &ans) {
        if (curr.size() == nums.size()) { // base case
            ans.push_back(curr);
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (visited[i]) {
                continue;
            }

            curr.push_back(nums[i]);
            visited[i] = true;

            permutations(nums, curr, visited, ans);
            visited[i] = false;
            curr.pop_back();
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> curr;
        vector<bool> visited(nums.size(), false);


        permutations(nums, curr, visited, ans);

            return ans;
    }
};