class Solution {
public:
    bool isThree(int n) {
        if(n<=2)return false;
        int s = sqrt(n);
        if(s*s==n && isPrime(s))return true;
        return false;
    }
private:
    bool isPrime(int num){
        if(num <= 1)return false;
        for(int i=2; i*i<=num; i++){
            if(num%i==0)return false;
        }
        return true;
    }
};