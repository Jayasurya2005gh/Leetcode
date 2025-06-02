class Solution {
public:
    bool isPalindrome(int x) {
        // Special cases: negative numbers and numbers ending with 0 (except 0 itself)
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        
        long long int originalNum = x;
        long long int reversedNum = 0;
        
        while (x > 0) {
            reversedNum = reversedNum * 10 + x % 10;
            x /= 10;
        }
        
        return originalNum == reversedNum;
    }
};