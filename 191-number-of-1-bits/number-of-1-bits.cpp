class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ones = 0;
        int i = 1;
        while (i <=32)
        {
            if(n&1){
                ones++;

            }
            n = n >> 1;
            i++;
            

        }
        return ones;
        
        
        
        
    }
};
        
        