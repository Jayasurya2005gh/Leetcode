class Solution {
public:
    int localMax(vector<vector<int>>& grid, int row, int col)
    {
        int val = grid[row][col];
        for(int i=row; i<=row+2; i++)
        {
            for(int j=col; j<=col+2; j++)
            {
                val = max(val,grid[i][j]);
            }
        }
        return val;
    }
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>> maxLocal(n-2, vector<int>(n-2));
        for(int i=0; i<n-2; i++)
        {
            for(int j=0; j<n-2; j++)
            {
                maxLocal[i][j] = localMax(grid, i, j);
            }
        }
        return maxLocal;
    }
};