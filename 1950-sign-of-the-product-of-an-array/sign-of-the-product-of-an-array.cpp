class Solution {
public:
    int arraySign(vector<int>& nums) {
        int sign = 1; // Start with a neutral sign

        for (int num : nums) {
            if (num == 0) {
                return 0; // If any number is zero, the product is zero
            }
            else if (num < 0) {
                sign *= -1; // Flip the sign for each negative number
            }
        }

        return sign; // Return the final sign
    }
};