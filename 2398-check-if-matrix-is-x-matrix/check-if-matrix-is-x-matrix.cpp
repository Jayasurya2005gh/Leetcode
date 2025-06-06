class Solution {
public:
    bool checkXMatrix(vector<vector<int>>& grid) 
    {
        int k=grid.size();
        for(int i=0;i<grid.size();i++)
        {
            k--;
            for(int j=0;j<grid.size();j++)
            {
                if(i==j && grid[i][j]==0)
                return false;
                
                else if(j==k && grid[i][k]==0)
                return false;
                
                else if(j!=k && i!=j && grid[i][j]!=0)
                return false;
                

            }
            
        }
        return true;
        
    }
};