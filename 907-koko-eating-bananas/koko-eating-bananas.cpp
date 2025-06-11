class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int count=0;
        int i;
        int low=1,high=*max_element(piles.begin(),piles.end());
        int ans=-1;
        while(low<=high)
        {
            int mid=low+((high-low)/2);
            long long sum=0;
            for(i=0;i<piles.size();i++)
            {
                if(piles[i]%mid==0)
                {
                 sum+=(piles[i]/mid);
                }
                else
                {
                    sum+=(piles[i]/mid)+1;
                }
            }
            if(sum==h)
            {
                ans=mid;
                high=mid-1;
            }
            if(sum>h)
            {
                low=mid+1;
            }
            else
            {
               high=mid-1;
            }

        }
         if(ans!=-1)
         {
             return ans;
         }
        return low;
    }
};