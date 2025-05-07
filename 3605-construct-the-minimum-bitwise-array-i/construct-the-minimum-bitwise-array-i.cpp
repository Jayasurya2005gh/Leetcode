class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& arr) {
        vector <int> ans;
        int n= arr.size();
        int i=0;
        bool flag= false;
        while(i<n){
            int res= arr[i];
            for(int j=1; j<1000; j++){
                int check= (j | (j+1));
                if(res == check){
                    ans.push_back(j);
                    break;
                }else if(j > arr[i]) break;
            }
            if(res==2)ans.push_back(-1);
            i++;
        }
        return ans;

    }
};