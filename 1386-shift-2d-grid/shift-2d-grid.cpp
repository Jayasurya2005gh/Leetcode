class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int n=grid.size();
        int m=grid[0].size();
        while(k--){
            vector<vector<int>>copyGrid(n,vector<int>(m));
            for(int i=0;i<n;i++){
                for(int j=0;j<m;j++){
                    if((i==n-1)&& (j==m-1)){
                        copyGrid[0][0]=grid[i][j];
                    }
                    else if(j==m-1){
                        copyGrid[i+1][0]=grid[i][j];
                    }
                    else{
                        copyGrid[i][j+1]=grid[i][j];
                    }
                }
            }
            grid=copyGrid;
        }
        return grid;
    }
};