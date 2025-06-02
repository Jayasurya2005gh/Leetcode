class Solution {
public:
    int findComplement(int num) {
        // Edge case: If num is 0, its complement is 1 (since binary of 0 is "0" and its complement is "1")
        if (num == 0) return 1;
        
        // Initialize a variable `mask` with the same value as `num`
        int mask = num;

        // Create a mask that has all bits set to 1 for the number of bits in `num`
        mask |= (mask >> 1);
        mask |= (mask >> 2);
        mask |= (mask >> 4);
        mask |= (mask >> 8);
        mask |= (mask >> 16);

        // XOR `num` with `mask` to flip its bits
        return num ^ mask;
    }
};