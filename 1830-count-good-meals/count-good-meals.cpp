class Solution {
public:
    int countPairs(vector<int>& deliciousness) {
        int N = deliciousness.size();
        unordered_map<int, int> mp;
        
        int count = 0, mod = 1000000007;
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= 21; j++) {
                int target = pow(2, j);
                
                if (mp.find(target - deliciousness[i]) != mp.end()) {
                    count = (count + mp[target - deliciousness[i]]) % mod;
                }
            }
            
            mp[deliciousness[i]]++;
        }
        
        return count;
    }
};