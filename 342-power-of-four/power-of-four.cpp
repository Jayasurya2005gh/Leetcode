class Solution {
public:
    bool isPowerOfFour(int n) {
        
        int k=n;
        int x=0;

        if(n==1)
          return true;
        if(n==5)
          return false;
        while(n!=0)
        {
            if(n%4==0)
             x++;
            n=n/4;
        }

        if(k==pow(4,x))
          return true;
        else
          return false;
    }
};