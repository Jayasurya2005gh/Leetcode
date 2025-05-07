class Solution {
public:
    int minimumSum(int n) {
        vector<int>v;
        while(n!=0)
        {
            int rem = n%10;
            v.push_back(rem);
            n=n/10;

        }
        sort(v.begin(),v.end());
        return (v[0]*10+v[3])+(v[1]*10+v[2]);
    }
};