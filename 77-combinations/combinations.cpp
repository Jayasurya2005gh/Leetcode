class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ans;
        int total_combinations = 1 << n; 
        for (int i = 0; i < total_combinations; i++) {
            vector<int> combination;
            for (int j = 0; j < n; j++) {
                if (i & (1 << j)) {
                    combination.push_back(j + 1);
                }
            }
            if (combination.size() == k) {
                ans.push_back(combination);
            }
        }
        
        return ans;
    }
};