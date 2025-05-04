class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int n = accounts.size();
        int m = accounts[0].size();
        int sum = 0;
        int maxSum = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                sum += accounts[i][j];
            }
            maxSum = max(maxSum, sum);
            sum = 0;
        }
        return maxSum;
    }
};